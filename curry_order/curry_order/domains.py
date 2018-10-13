import enum
from typing import (
    List,
    Tuple,
    NamedTuple,
)


class Item(enum.Enum):
    chiken_curry = enum.auto()
    beef_curry = enum.auto()

    def value(self) -> int:
        return {
            Item.chiken_curry: 700,
            Item.beef_curry: 900,
        }[self]


class RecieptItem(NamedTuple):
    item: Item
    amount: int  # the number of the item


class Reciept(NamedTuple):
    items: List[Tuple[RecieptItem, int]]  # int is the total price of the item
    order_sum: int  # order_sum is the total price of the order


class Cacher:
    def times(self, reciept_item: RecieptItem) -> int:
        return reciept_item.item.value() * reciept_item.amount

    def order_sum(self, orders: List[RecieptItem]) -> Reciept:
        order_list = []
        order_sum = 0

        for order in orders:
            order_list.append((order, self.times(order)))
            order_sum += self.times(order)

        return Reciept(order_list, order_sum)
