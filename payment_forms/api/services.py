import os

import stripe
from django.shortcuts import get_object_or_404

from .models import Item, Order
from .utils import get_line_items_data

stripe.api_key = os.environ.get("STRIPE_API_KEY")


def create_session(DOMAIN, **kwargs):
    line_items = [get_line_items_data(**kwargs)]
    session = stripe.checkout.Session.create(
        success_url=f"{DOMAIN}/success",
        cancel_url=f"{DOMAIN}/cancel",
        line_items=line_items,
        mode="payment",
    )
    return session


def get_item_by_id(item_id):
    return get_object_or_404(Item, id=item_id)


def get_order_by_id(order_id):
    return get_object_or_404(Order, id=order_id)
