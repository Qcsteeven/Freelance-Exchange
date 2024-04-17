from typing import TypedDict, Any
from datetime import datetime
from .table import Table


class MessageInfo(TypedDict):
    chat: int
    owner: int
    date: datetime
    value: str

class MessageInfoTransformed(TypedDict):
    chat: int
    owner: int
    date: datetime
    value: str

class MessageRow(TypedDict):
    id: int
    chat: int
    owner: int
    date: datetime
    value: str

class MessagesTable(Table[MessageInfo, MessageInfoTransformed, MessageRow]):
    table = 'messages'
    _properties = ['chat', 'owner', 'date', 'value']
    _id = 'id'

    def _insert_before(self, con, info: MessageInfo) -> MessageInfoTransformed:
        return MessageInfoTransformed(
            chat=info['chat'],
            owner=info['owner'],
            date=info['date'],
            value=info['value']
        )

    def _update_before(self, con, identifier: int, info: MessageInfo) -> MessageInfoTransformed:
        return MessageInfoTransformed(
            chat=info['chat'],
            owner=info['owner'],
            date=info['date'],
            value=info['value']
        )

    def _get_values(self, info: MessageInfoTransformed) -> list[Any]:
        return [info['chat'], info['owner'], info['date'], info['value']]

    def _get_zero_row(self) -> MessageRow:
        return MessageRow(
            id = 0,
            chat=0,
            owner=0,
            date=datetime(year=2010, month=1, day=1),
            value='Not Found'
        )
