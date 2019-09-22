from typing import List, Union


class CheckoutHelper:

    def __init__(self, items: List[dict]):
        self.items = {item['sku']: item for item in items}

        self.offers = [item['offers'] for item in items if item['offers']]

    def get_item_by_sku(self, sku: str) -> Union[dict, None]:
        return self.items.get(sku)

    def get_items_by_skus_sorted_by_price(self, skus: List[str]) -> List[dict]:


