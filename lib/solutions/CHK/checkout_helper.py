from typing import List, Iterable, Union
from .offer_types import OfferTypes


class CheckoutHelper:
    """ A Simple class that handles the item related functions """

    def __init__(self, items: List[dict]):
        self.items = {item['sku']: item for item in items}

        self.offers = []
        for item in items:
            if item['offers']:
                self.offers.extend(item['offers'])

    def get_item_by_sku(self, sku: str) -> Union[dict, None]:
        return self.items.get(sku)

    def get_items_by_skus_sorted_by_price(self, skus: List[str]) -> Iterable[dict]:
        """
        Returns an iterable of matching items sorted by price. Most expensive first
        :param skus: The skus to lookup
        :return: The sorted items
        """

        return sorted(
            filter(
                lambda i: i['sku'] in skus,
                self.items.values()
            ),
            key=lambda i: -i['unit_price']
        )

    def get_offers_in_apply_order(self) -> List[dict]:
        def _offers_sort_key(offer: dict) -> (int, int):
            # having to use .name here as I think the enum import paths weren't quite the same
            offer_types_order = {
                OfferTypes.group_buy_discount.name: -1,
                OfferTypes.get_one_free.name: 0,
                OfferTypes.multi_price.name: 1
            }

            return offer_types_order[offer['offer_type'].name], -offer['quantity']

        return sorted(
            self.offers,
            key=_offers_sort_key
        )




