from django.urls import path

from rest_framework.routers import SimpleRouter

from .views import (
    UserAPIView,
    UsersAPIView,
    TradeAPIView,
    TradesAPIView)

router = SimpleRouter()
router.register('users', UserAPIView)
router.register('trades', TradeAPIView)

urlpatterns = [
    path('users/', UsersAPIView.as_view(), name='users'),
    path('user/<int:pk>/', UserAPIView.as_view(), name='trade'),

    path('trades/', TradesAPIView.as_view(), name='trades'),
    path('trade/<int:pk>/', TradeAPIView.as_view(), name='trade'),

]
