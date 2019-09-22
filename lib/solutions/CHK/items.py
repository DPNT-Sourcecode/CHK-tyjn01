from enum import Enum, auto

class OfferTypes(Enum):
    multi_price = auto()
    get_one_free = auto()
    group_buy_discount = auto()

ITEMS = [
    {
        'sku': 'A',
        'unit_price': 50,
        'offers': [
            {
                'sku': 'A',
                'offer_type': OfferTypes.multi_price,
                'quantity': 3,
                'price': 130
            },
            {
                'sku': 'A',
                'offer_type': OfferTypes.multi_price,
                'quantity': 5,
                'price': 200
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
        'unit_price': 70,
        'offers': [
            {
                'sku': 'K',
                'offer_type': OfferTypes.multi_price,
                'quantity': 2,
                'price': 120
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
        'unit_price': 20,
        'offers': [
            {
                'skus': ['S', 'T', 'X', 'Y', 'Z'],
                'offer_type': OfferTypes.group_buy_discount,
                'quantity': 3,
                'price': 45
            }
        ]
    },
    'T': {
        'unit_price': 20,
        'offers': [
            {
                'skus': ['S', 'T', 'X', 'Y', 'Z'],
                'offer_type': OfferTypes.group_buy_discount,
                'quantity': 3,
                'price': 45
            }
        ]
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
            },
            {
                'sku': 'V',
                'offer_type': OfferTypes.multi_price,
                'quantity': 3,
                'price':  130
            }
        ]
    },
    'W': {
        'unit_price': 20,
        'offers': []
    },
    'X': {
        'unit_price': 17,
        'offers': [
            {
                'skus': ['S', 'T', 'X', 'Y', 'Z'],
                'offer_type': OfferTypes.group_buy_discount,
                'quantity': 3,
                'price': 45
            }
        ]
    },
    'Y': {
        'unit_price': 20,
        'offers': [
            {
                'skus': ['S', 'T', 'X', 'Y', 'Z'],
                'offer_type': OfferTypes.group_buy_discount,
                'quantity': 3,
                'price': 45
            }
        ]
    },
    'Z': {
        'unit_price': 21,
        'offers': [
            {
                'skus': ['S', 'T', 'X', 'Y', 'Z'],
                'offer_type': OfferTypes.group_buy_discount,
                'quantity': 3,
                'price': 45
            }
        ]
    },
}
