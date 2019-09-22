from enum import Enum, auto


class OfferTypes(Enum):
    multi_price = auto()
    get_one_free = auto()
    group_buy_discount = auto()
