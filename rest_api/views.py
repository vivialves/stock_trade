from django.http import HttpResponse
from rest_framework import generics

from .models import User, Trade
from .serializers import UserSerializer, TradeSerializer


class UsersAPIView(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class UserAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def update(self, request, *args, **kwargs):
        response = HttpResponse('Method not allowed')
        return response

    def destroy(self, request, *args, **kwargs):
        response = HttpResponse('Method not allowed')
        return response

class TradesAPIView(generics.ListCreateAPIView):
    queryset = Trade.objects.all()
    serializer_class = TradeSerializer

class TradeAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Trade.objects.all()
    serializer_class = TradeSerializer

    def update(self, request, *args, **kwargs):
        response = HttpResponse('Method not allowed')
        return response

    def destroy(self, request, *args, **kwargs):
        response = HttpResponse('Method not allowed')
        return response
