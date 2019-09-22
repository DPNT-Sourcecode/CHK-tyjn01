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
    'sku':
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
    'sku':
        'unit_price': 20,
        'offers': []
    },
    'D': {
        'sku':
        'unit_price': 15,
        'offers': []
    },
    'E': {
        'sku':
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
        'sku':
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
        'sku':
        'unit_price': 20,
        'offers': []
    },
    'H': {
        'sku':
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
        'sku':
        'unit_price': 35,
        'offers': []
    },
    'J': {
        'sku':
        'unit_price': 60,
        'offers': []
    },
    'K': {
        'sku':
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
        'sku':
        'unit_price': 90,
        'offers': []
    },
    'M': {
        'sku':
        'unit_price': 15,
        'offers': []
    },
    'N': {
        'sku':
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
        'sku':
        'unit_price': 10,
        'offers': []
    },
    'P': {
        'sku':
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
        'sku':
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
        'sku':
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
        'sku':
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
        'sku':
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
        'sku':
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
        'sku': 'V',
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
        'sku': 'W',
        'unit_price': 20,
        'offers': []
    },
    'X': {
        'sku': 'X',
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
        'sku': 'Y',
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
        'sku': 'Z',
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

