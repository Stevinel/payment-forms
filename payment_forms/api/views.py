import logging
import os
from urllib import request

from django.shortcuts import render
from dotenv import load_dotenv
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.exceptions import APIException
from rest_framework.response import Response
from rest_framework.views import APIView

from .services import create_session, get_item_by_id, get_order_by_id

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
load_dotenv()

STRIPE_PUBLIC_API_KEY = os.environ.get("STRIPE_PUBLIC_API_KEY")
DOMAIN = os.environ.get("DOMAIN")


class StripeSessionIdView(APIView):
    def get(self, request, id):
        """
        Getting session ID for items/orders in your company.
        See detailed documentation about products and prices:
        https://stripe.com/docs/products-prices/how-products-and-prices-work
        """

        try:
            order = None
            item = None
            url_request_from = request.META["HTTP_REFERER"]

            if "item" in url_request_from:
                item = get_item_by_id(id)
            elif "order" in url_request_from:
                order = get_order_by_id(id)
            kwargs = {"item": item, "order": order}
            session = create_session(DOMAIN, **kwargs)
        except Exception as e:
            logger.error(e)
            raise APIException(e)
        return Response(session.id, status=status.HTTP_201_CREATED)


class BuyItemView(APIView):
    def get(self, request, item_id):
        """
        Renders the item purchase page
        """

        item = get_item_by_id(item_id)
        context = {
            "item": item,
            "DOMAIN": DOMAIN,
            "STRIPE_PUBLIC_API_KEY": STRIPE_PUBLIC_API_KEY,
        }
        return render(request, "buy_item.html", context)


class BuyOrderItemsView(APIView):
    def get(self, request, order_id):
        """
        Renders the order page
        """

        order = get_order_by_id(order_id)
        try:
            total_amount = sum([item.price for item in order.items.all()])
            context = {
                "order": order,
                "total_amount": total_amount,
                "DOMAIN": DOMAIN,
                "STRIPE_PUBLIC_API_KEY": STRIPE_PUBLIC_API_KEY,
            }
            return render(request, "make_an_order.html", context)
        except Exception as e:
            logger.error(e)
            raise APIException(e)


@api_view(['GET'])
def success(request):
    """
    Page about successful purchase
    """

    return render(request, "buy_success.html")


@api_view(['GET'])
def cancel(request):
    """
    Page about canceling a purchase
    """

    return render(request, "buy_cancel.html")