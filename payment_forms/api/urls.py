from django.urls import path
from rest_framework.routers import DefaultRouter

from .views import BuyItemView, BuyOrderItemsView, StripeSessionIdView

router_v1 = DefaultRouter()


urlpatterns = [
    path('buy/<int:id>/', StripeSessionIdView.as_view(), name="stripe_session"),
    path('item/<int:item_id>/', BuyItemView.as_view(), name="buy_item"),
    path('order/<int:order_id>/', BuyOrderItemsView.as_view(), name="buy_item"),
]

urlpatterns += router_v1.urls
