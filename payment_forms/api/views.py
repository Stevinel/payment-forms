import os
import logging
import stripe
from django.shortcuts import get_object_or_404, render
from dotenv import load_dotenv
from rest_framework import status
from rest_framework.exceptions import APIException
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Item
from .utils import get_line_items_data

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
load_dotenv()


stripe.api_key = os.environ.get("STRIPE_API_KEY")
STRIPE_PUBLIC_API_KEY = os.environ.get("STRIPE_PUBLIC_API_KEY")
DOMAIN = os.environ.get("DOMAIN")


class StripeSessionIdView(APIView):
    """
    Getting session ID for products ADDED to stripe.
    See detailed documentation about products and prices:
    https://stripe.com/docs/products-prices/how-products-and-prices-work
    """

    http_method_names = ["get"]

    def get(self, request, item_id):
        try:
            item = Item.objects.get(id=item_id)
            session = stripe.checkout.Session.create(
                success_url=f"{DOMAIN}/success",
                cancel_url=f"{DOMAIN}/cancel",
                line_items=[get_line_items_data(item)],
                mode="payment",
            )
        except Exception as e:
            logger.error(e)
            raise APIException(e)
        return Response(session.id, status=status.HTTP_201_CREATED)


class BuyItemView(APIView):
    """
    """
    http_method_names = ["get"]

    def get(self, request, item_id):
        logger.error('debug info')
        item = get_object_or_404(Item, id=item_id)
        context = {
            'item': item,
            'DOMAIN': DOMAIN,
            'STRIPE_PUBLIC_API_KEY': STRIPE_PUBLIC_API_KEY,
        }
        return render(request, 'buy_item.html', context)