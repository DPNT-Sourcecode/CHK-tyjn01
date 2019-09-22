from collections import defaultdict
from enum import Enum, auto
from typing import Dict
from copy import deepcopy

INDIVIDUAL_ITEM_PRICES = {
    'A': 50,
    'B': 30,
    'C': 20,
    'D': 15,
    'E': 40,
    'F': 10,
}


class OfferTypes(Enum):
    multi_price = auto()
    get_one_free = auto()


SPECIAL_OFFERS = [
    {
        'sku': 'A',
        'offer_type': OfferTypes.multi_price,
        'quantity': 3,
        'price': 130  # unit price of 43.33 recurring
    },
    {
        'sku': 'A',
        'offer_type': OfferTypes.multi_price,
        'quantity': 5,
        'price': 200  # unit price of 40
    },
    {
        'sku': 'B',
        'offer_type': OfferTypes.multi_price,
        'quantity': 2,
        'price': 45
    },
    {
        'sku': 'E',
        'offer_type': OfferTypes.get_one_free,
        'quantity': 2,
        'free_gift': 'B'
    },
    {
        'sku': 'F',
        'offer_type': OfferTypes.get_one_free,
        'quantity': 2,
        'free_gift': 'F'
    }
]


def apply_offers(sku_counts: Dict[str, int]) -> (Dict[str, int], int):
    sku_counts = deepcopy(sku_counts)
    total = 0

    # sort offers by type and then quantity (biggest first)
    sorted_offers = sorted(
        SPECIAL_OFFERS,
        key=lambda o: (o['offer_type'] != OfferTypes.get_one_free, -o['quantity'])
    )
    for offer_details in sorted_offers:
        sku = offer_details['sku']
        sku_count = sku_counts[sku]

        if offer_details['offer_type'] == OfferTypes.get_one_free:
            if offer_details['free_gift'] == sku:
                num_multiples = sku_count // (offer_details['quantity'] + 1)
            else:
                num_multiples = sku_count // offer_details['quantity']

            sku_count_of_free_gift = sku_counts[offer_details['free_gift']]

            sku_counts[offer_details['free_gift']] = max(sku_count_of_free_gift - num_multiples, 0)

            # Assumption here that a given item can only be used for 1 offer at a time,
            # and that get_one_free offers have a higher precedence

            sku_counts[sku] = sku_counts[sku] % offer_details['quantity']
            total += (sku_count - sku_counts[sku]) * INDIVIDUAL_ITEM_PRICES[sku]

        elif offer_details['offer_type'] == OfferTypes.multi_price:
            num_multiples = sku_count // offer_details['quantity']

            total += num_multiples * offer_details['price']

            sku_counts[sku] = sku_count % offer_details['quantity']

    return sku_counts, total


# noinspection PyUnusedLocal
# skus = unicode string
def checkout(skus: str) -> int:
    sku_counts = defaultdict(int)

    for sku in skus:
        if sku not in INDIVIDUAL_ITEM_PRICES:
            return -1

        sku_counts[sku] += 1

    sku_counts_after_applying_offers, sub_total = apply_offers(sku_counts)

    total = sub_total
    for sku, count in sku_counts_after_applying_offers.items():
        total += count * INDIVIDUAL_ITEM_PRICES[sku]

    return total




