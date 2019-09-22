from collections import defaultdict
from copy import deepcopy

from lib.solutions.CHK.checkout_helper import CheckoutHelper
from .items import ITEMS, OfferTypes


checkout_helper = CheckoutHelper(ITEMS)


def _apply_group_discount_offer(offer_details: dict, sku_counts: dict) -> (dict, int):
    sku_counts = deepcopy(sku_counts)

    subtotal = 0

    qualifying_purchase_number = sum(
        sku_counts[sku_in_offer] for sku_in_offer in offer_details['skus']
    )

    num_multiples = qualifying_purchase_number // offer_details['quantity']
    subtotal += num_multiples * offer_details['price']

    number_of_items_used_in_offer = num_multiples * offer_details['quantity']

    # because we are fair to the customers we include expensive items first:
    for item in checkout_helper.get_items_by_skus_sorted_by_price(offer_details['skus']):
        item_sku_count = sku_counts[item['sku']]

        num_used_in_offer = min(item_sku_count, number_of_items_used_in_offer)

        number_of_items_used_in_offer -= num_used_in_offer
        sku_counts[item['sku']] -= num_used_in_offer

        if not number_of_items_used_in_offer:
            break

    return sku_counts, subtotal


def _apply_get_one_free_offer(offer_details: dict, sku_counts: dict) -> (dict, int):
    sku = offer_details['sku']
    sku_count = sku_counts[sku]

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

    subtotal = (num_multiples * offer_details['quantity']) * ITEMS[sku]['unit_price']

    return sku_counts, subtotal


def _apply_multiprice_discount(offer_details: dict, sku_counts: dict) -> (dict, int):
    sku = offer_details['sku']
    sku_count = sku_counts[sku]

    num_multiples = sku_count // offer_details['quantity']

    subtotal = num_multiples * offer_details['price']
    sku_counts[sku] = sku_count % offer_details['quantity']

    return sku_counts, subtotal


# noinspection PyUnusedLocal
# skus = unicode string
def checkout(skus: str) -> int:
    sku_counts = defaultdict(int)

    for sku in skus:
        if checkout_helper.get_item_by_sku(sku) is None:
            return -1

        sku_counts[sku] += 1

    total = 0
    for offer_details in checkout_helper.get_offers_in_apply_order():
        offer_type = offer_details['offer_type']

        if offer_type == OfferTypes.group_buy_discount:
            sku_counts, subtotal = _apply_group_discount_offer(offer_details, sku_counts)
        elif offer_type == OfferTypes.get_one_free:
            sku_counts, subtotal = _apply_get_one_free_offer(offer_details, sku_counts)
        elif offer_type == OfferTypes.multi_price:
            sku_counts, subtotal = _apply_multiprice_discount(offer_details, sku_counts)
        else:
            raise NotImplementedError(f'The offer type "{offer_type}" is not yet implemented')

        total += subtotal

    for sku, count in sku_counts.items():
        total += count * ITEMS[sku]['unit_price']

    return total

