from typing import List

class CheckoutHelper:

    def __init__(self, items: List[dict]):
        self.items = {item['sku']: item for item in items}

        self.offers = [item['offers'] for item in items if offer['offers']]
