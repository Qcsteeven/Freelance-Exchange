from abc import ABC, abstractmethod
from typing import TypeVar, Generic, Any, TypedDict
from psycopg import Connection
from ..storage_core import StorageCore
from ..exceptions import StorageException

class TableFilter(TypedDict):
    where: str | None
    order: str | None

TableInfoDict = TypeVar('TableInfoDict')
TableInfoTransformedDict = TypeVar('TableInfoTransformedDict')
TableRowDict = TypeVar('TableRowDict')
# have keys where and order

class Table(ABC, Generic[TableInfoDict, TableInfoTransformedDict, TableRowDict]):
    _db: StorageCore
    table: str
    _properties: list[str]
    _id: str

    def __init__(self, core: StorageCore):
        self._db = core

    def select(self, query_filter: TableFilter | None = None) -> list[TableRowDict]:
        with self._db.get_select_cursor() as cursor:
            cursor.execute(self.get_select_sql(query_filter))
            return cursor.fetchall()

    def select_one(self, identifier: int) -> None | TableRowDict:
        sql = self.get_select_sql(TableFilter(where=self._id + '=%s', order=None))
        with self._db.get_select_cursor() as cursor:
            cursor.execute(sql, [identifier])
            return cursor.fetchone()

    def get_select_sql(self, query_filter: TableFilter | None = None) -> str:
        all_properties = self._get_all_properties_with_postfix()
        join_properties = self._get_join_properties()
        filter_fragment = self._get_filter_fragment(query_filter)
        join_fragment = self._get_join_fragment()

        if 0 < len(join_properties):
            join_properties = ', ' + join_properties

        return f'SELECT {all_properties}{join_properties} FROM {self.table} {join_fragment} {filter_fragment}'

    def insert(self, info: TableInfoDict) -> TableRowDict:
        with self._db.get_connection() as connection:
            return self.insert_with_con(connection, info)

    def insert_with_con(self, con: Connection, info: TableInfoDict) -> TableRowDict:
        info_transformed = self._insert_before(con, info)

        values = self._get_values(info_transformed)
        properties = self._get_properties()
        all_properties = self._get_all_properties()
        values_fragment = self._get_values_fragment()
        sql = f'INSERT INTO {self.table} ({properties}) VALUES ({values_fragment}) RETURNING {all_properties}'

        result = con.execute(sql, values).fetchone()

        if isinstance(result.get('id'), int):
            self._insert_after(con, result['id'], info)

        return result if result else self._get_zero_row()

    def update(self, identifier: int, info: TableInfoDict) -> TableRowDict | None:
        with self._db.get_connection() as connection:
            return self.update_with_con(connection, identifier, info)

    def update_with_con(self, con: Connection, identifier: int, info: TableInfoDict) -> TableRowDict | None:
        info_transformed = self._update_before(con, identifier, info)

        values = self._get_values(info_transformed)
        values.append(identifier)
        set_fragment = self._get_set_fragment()
        sql = f'UPDATE {self.table} SET {set_fragment} RETURNING {self._get_all_properties()}'

        return con.execute(sql, values).fetchone()

    def delete(self, identifier: int) -> None | TableInfoTransformedDict:
        with self._db.get_connection() as connection:
            self.delete_with_con(connection, identifier)

    def delete_with_con(self, con: Connection, identifier: int) -> None | TableInfoTransformedDict:
        sql = f'DELETE FROM {self.table} WHERE {self._id}=%s RETURNING {self._get_all_properties()}'
        self._delete_before(con, identifier)
        result = con.execute(sql, [identifier]).fetchone()

        if result is not None:
            self._delete_after(con, result)

        return result

    def _get_properties(self) -> str:
        return ', '.join(self._properties)

    def _get_all_properties(self) -> str:
        return self._id + ', ' + self._get_properties()

    def _get_properties_with_postfix(self) -> str:
        return ', '.join([f'{self.table}.{s}' for s in self._properties])

    def _get_all_properties_with_postfix(self) -> str:
        return f'{self.table}.{self._id}, {self._get_properties()}'

    def _get_set_fragment(self) -> str:
        return '=%s, '.join(self._properties) + '=%s'

    def _get_values_fragment(self) -> str:
        return ', '.join(['%s'] * len(self._properties))

    def _get_filter_fragment(self, query_filter: TableFilter | None) -> str:
        sql_filter = ''

        if query_filter is None:
            return sql_filter

        if isinstance(query_filter['where'], str):
            sql_filter += f'WHERE {query_filter['where']} '
        if isinstance(query_filter['order'], str):
            sql_filter += f'ORDER BY {query_filter['order']} '

        return sql_filter

    # may be overridden
    def _get_join_fragment(self) -> str:
        return ''

    # may be overridden
    def _get_join_properties(self) -> str:
        return ''

    @abstractmethod
    def _insert_before(self, con: Connection, info: TableInfoDict) -> TableInfoTransformedDict:
        raise StorageException('Abstract method!!!')

    def _insert_after(self, con: Connection, identifier: int, info: TableInfoDict):
        return

    @abstractmethod
    def _update_before(self, con: Connection, identifier: int, info: TableInfoDict) -> TableInfoTransformedDict:
        raise StorageException('Abstract method!!!')

    def _delete_before(self, con: Connection, identifier: int):
        return

    def _delete_after(self, con: Connection, row: TableInfoTransformedDict):
        return

    @abstractmethod
    def _get_values(self, info: TableInfoTransformedDict) -> list[Any]:
        raise StorageException('Abstract method!!!')

    @abstractmethod
    def _get_zero_row(self) -> TableInfoTransformedDict:
        raise StorageException('Abstract method!!!')
