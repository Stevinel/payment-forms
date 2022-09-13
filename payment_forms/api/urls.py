from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import BuyItemView, BuyOrderItemsView, StripeSessionIdView, cancel, success

router_v1 = DefaultRouter()


urlpatterns_v1 = [
    path('buy/<int:id>/', StripeSessionIdView.as_view(), name="stripe_session"),
    path('item/<int:item_id>/', BuyItemView.as_view(), name="buy_item"),
    path('order/<int:order_id>/', BuyOrderItemsView.as_view(), name="buy_item"),
]

urlpatterns = [
    path('v1/', include(urlpatterns_v1)),
    path("success/", success, name="buy_success"),
    path("cancel/", cancel, name="buy_cancel")
]
