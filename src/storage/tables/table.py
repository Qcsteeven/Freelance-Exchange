from abc import ABC, abstractmethod
from typing import TypeVar, Generic, Any
from psycopg import Connection
from ..storage_core import StorageCore
from ..exceptions import StorageException

TableInfoDict = TypeVar('TableInfoDict')
TableInfoTransformedDict = TypeVar('TableInfoTransformedDict')
TableRowDict = TypeVar('TableRowDict')

class Table(ABC, Generic[TableInfoDict, TableInfoTransformedDict, TableRowDict]):
    _db: StorageCore
    _table: str
    _properties: list[str]
    _id: str

    def __init__(self, core: StorageCore):
        self._db = core

    def select_raw(self) -> str:
        return f'SELECT {self._get_all_properties()} FROM {self._table}'

    def select(self) -> list[TableRowDict]:
        with self._db.get_select_cursor() as cursor:
            cursor.execute(self.select_raw())
            return cursor.fetchall()

    def select_one(self, identifier: int) -> None | TableRowDict:
        with self._db.get_select_cursor() as cursor:
            cursor.execute(f'{self.select_raw()} WHERE {self._id}=%s', [identifier])
            return cursor.fetchone()

    def insert(self, info: TableInfoDict) -> TableRowDict:
        with self._db.get_connection() as connection:
            return self.insert_with_con(connection, info)

    def insert_with_con(self, con: Connection, info: TableInfoDict) -> TableRowDict:
        info_transformed = self._insert_before(con, info)

        values = self._get_values(info_transformed)
        properties = self._get_properties()
        all_properties = self._get_all_properties()
        values_fragment = self._get_values_fragment()
        sql = f'INSERT INTO {self._table} ({properties}) VALUES ({values_fragment}) RETURNING {all_properties}'

        result = con.execute(sql, values).fetchone()
        return result if result else self._get_zero_row()

    def update(self, identifier: int, info: TableInfoDict) -> TableRowDict | None:
        with self._db.get_connection() as connection:
            return self.update_with_con(connection, identifier, info)

    def update_with_con(self, con: Connection, identifier: int, info: TableInfoDict) -> TableRowDict | None:
        info_transformed = self._update_before(con, identifier, info)

        values = self._get_values(info_transformed)
        values.append(identifier)
        set_fragment = self._get_set_fragment()
        sql = f'UPDATE {self._table} SET {set_fragment} RETURNING {self._get_all_properties()}'

        return con.execute(sql, values).fetchone()

    def delete(self, identifier: int) -> None | TableRowDict:
        sql = f'DELETE FROM {self._table} WHERE {self._id}=%s RETURNING {self._get_all_properties()}'

        with self._db.get_connection() as connection:
            with connection.cursor() as cursor:
                cursor.execute(sql, [identifier])
                result = cursor.fetchone()
                return result if result else self._get_zero_row()

    def _get_properties(self) -> str:
        return ', '.join(self._properties)

    def _get_all_properties(self) -> str:
        return self._id + ', ' + ', '.join(self._properties)

    def _get_set_fragment(self) -> str:
        return '=%s, '.join(self._properties) + '=%s'

    def _get_values_fragment(self) -> str:
        return ', '.join(['%s'] * len(self._properties))

    @abstractmethod
    def _insert_before(self, con: Connection, info: TableInfoDict) -> TableInfoTransformedDict:
        raise StorageException('Abstract method!!!')

    @abstractmethod
    def _update_before(self, con: Connection, identifier: int, info: TableInfoDict) -> TableInfoTransformedDict:
        raise StorageException('Abstract method!!!')

    @abstractmethod
    def _get_values(self, info: TableInfoTransformedDict) -> list[Any]:
        raise StorageException('Abstract method!!!')

    @abstractmethod
    def _get_zero_row(self) -> TableRowDict:
        raise StorageException('Abstract method!!!')
