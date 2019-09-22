from collections import defaultdict
from enum import Enum, auto
from typing import Dict
from copy import deepcopy


class OfferTypes(Enum):
    multi_price = auto()
    get_one_free = auto()


ITEMS = {
    'A': {
        'unit_price': 50,
        'offers': [
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
        ]
    },
    'B': {
        'unit_price': 30,
        'offers': [
            {
                'sku': 'B',
                'offer_type': OfferTypes.multi_price,
                'quantity': 2,
                'price': 45
            },
        ]
    },
    'C': {
        'unit_price': 20,
        'offers': []
    },
    'D': {
        'unit_price': 15,
        'offers': []
    },
    'E': {
        'unit_price': 40,
        'offers': [
            {
                'sku': 'E',
                'offer_type': OfferTypes.get_one_free,
                'quantity': 2,
                'free_gift': 'B'
            }
        ]
    },
    'F': {
        'unit_price': 10,
        'offers': [
            {
                'sku': 'F',
                'offer_type': OfferTypes.get_one_free,
                'quantity': 2,
                'free_gift': 'F'
            }
        ]
    },
    'G': {
        'unit_price': 20,
        'offers': []
    },
    'H': {
        'unit_price': 10,
        'offers': [
            {
                'sku': 'H',
                'offer_type': OfferTypes.multi_price,
                'quantity': 5,
                'price': 45
            },
            {
                'sku': 'H',
                'offer_type': OfferTypes.multi_price,
                'quantity': 10,
                'price': 80
            },
        ]
    },
    'I': {
        'unit_price': 35,
        'offers': []
    },
    'J': {
        'unit_price': 60,
        'offers': []
    },
    'K': {
        'unit_price': 80,
        'offers': [
            {
                'sku': 'K',
                'offer_type': OfferTypes.multi_price,
                'quantity': 2,
                'price': 150
            }
        ]
    },
    'L': {
        'unit_price': 90,
        'offers': []
    },
    'M': {
        'unit_price': 15,
        'offers': []
    },
    'N': {
        'unit_price': 40,
        'offers': [
            {
                'sku': 'N',
                'offer_type': OfferTypes.get_one_free,
                'quantity': 3,
                'free_gift': 'M'
            }
        ]
    },
    'O': {
        'unit_price': 10,
        'offers': []
    },
    'P': {
        'unit_price': 50,
        'offers': [
            {
                'sku': 'P',
                'offer_type': OfferTypes.multi_price,
                'quantity': 5,
                'price': 200
            }
        ]
    },
    'Q': {
        'unit_price': 30,
        'offers': [
            {
                'sku': 'Q',
                'offer_type': OfferTypes.multi_price,
                'quantity': 3,
                'price': 80
            }
        ]
    },
    'R': {
        'unit_price': 50,
        'offers': [
            {
                'sku': 'R',
                'offer_type': OfferTypes.get_one_free,
                'quantity': 3,
                'free_gift': 'Q'
            }
        ]
    },
    'S': {
        'unit_price': 30,
        'offers': []
    },
    'T': {
        'unit_price': 20,
        'offers': []
    },
    'U': {
        'unit_price': 40,
        'offers': [
            {
                'sku': 'U',
                'offer_type': OfferTypes.get_one_free,
                'quantity': 3,
                'free_gift': 'U'
            },
        ]
    },
    'V': {
        'unit_price': 50,
        'offers': [
            {
                'sku': 'V',
                'offer_type': OfferTypes.multi_price,
                'quantity': 2,
                'price':  90
            }
        ]
    },
    'W': {
        'unit_price': 20,
        'offers': []
    },
    'X': {
        'unit_price': 90,
        'offers': []
    },
    'Y': {
        'unit_price': 10,
        'offers': []
    },
    'Z': {
        'unit_price': 50,
        'offers': []
    },
}


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
                # Need to take into account that you to give away an F you need some
                # the offer quantity + 1, for example if 4 F's purchased then only 1 can be
                # given away as you have 2F + 1 for free, and 1 at the normal price.
                num_multiples = sku_count // (offer_details['quantity'] + 1)
            else:
                num_multiples = sku_count // offer_details['quantity']

            sku_count_of_free_gift = sku_counts[offer_details['free_gift']]

            sku_counts[offer_details['free_gift']] = max(sku_count_of_free_gift - num_multiples, 0)

            # To prevent a given item being counted multiple times the sku count must be reduced
            # by the number state in this offer, and then the "processed" items are simply added to
            # the bill at their individual item price.
            sku_counts[sku] -= num_multiples * offer_details['quantity']
            total += (num_multiples * offer_details['quantity']) * INDIVIDUAL_ITEM_PRICES[sku]

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




