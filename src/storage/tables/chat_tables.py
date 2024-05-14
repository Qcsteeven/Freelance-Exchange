from typing import TypedDict, Any
from .table import Table


class ChatInfo(TypedDict):
    performer: int
    order_link: int

class ChatInfoTransformed(TypedDict):
    performer: int
    order_link: int

class ChatRow(TypedDict):
    id: int
    performer: int
    order_link: int

class ChatsTable(Table[ChatInfo, ChatInfoTransformed, ChatRow]):
    table = 'chats'
    _properties = ['performer', 'order_link']
    _id = 'id'

    def _insert_before(self, con, info: ChatInfo) -> ChatInfoTransformed:
        return ChatInfoTransformed(
            performer=info['performer'],
            order_link=info['order_link']
        )

    def _update_before(self, con, identifier: int, info: ChatInfo) -> ChatInfoTransformed:
        return ChatInfoTransformed(
            performer=info['performer'],
            order_link=info['order_link']
        )

    def _get_values(self, info: ChatInfoTransformed) -> list[Any]:
        return [info['performer'], info['order_link']]

    def _get_zero_row(self) -> ChatInfoTransformed:
        return ChatInfoTransformed(performer=0, order_link=0)
