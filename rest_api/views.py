from django.db.models import query
from rest_framework import generics, serializers
from rest_framework.generics import get_object_or_404

from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import mixins

from .models import User, Trade
from .serializers import UserSerializer, TradeSerializer

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    
class TradeViewSet(viewsets.ModelViewSet):
    queryset = Trade.objects.all()
    serializer_class = TradeSerializer

    @action(detail=True, methods=['get'])
    def avaliacoes(self, request,pk=None):
        self.pagination_class.page_size = 1
        page = self.paginate_queryset(trade)

        if page is not None:
            serializer = TradeSerializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = TradeSerializer(trade, many=True)
        return Response(serializer.data)
