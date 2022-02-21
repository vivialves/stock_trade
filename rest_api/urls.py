from django.urls import path

from rest_framework.routers import SimpleRouter

from .views import (
    UserViewSet,
    TradeViewSet)

router = SimpleRouter()
router.register('users', UserViewSet)
router.register('trades',TradeViewSet)

urlpatterns = [
    path('users/', UserViewSet.as_view({'get':'list'}), name='users'),

    path('trades/', TradeViewSet.as_view({'get':'list'}), name='trades'),
    path('trade/<int:pk>/', TradeViewSet.as_view({'get':'list'}), name='trade'),

]
