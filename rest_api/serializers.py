from rest_framework import serializers
from .models import User, Trade

class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = {
            'id',
            'name',
            'position',
        }

class TradeSerializer(serializers.ModelSerializer):

    class Meta:
        model = Trade
        fields = {
            'id',
            'type',
            'user_id',
            'symbol',
            'shares',
            'price',
            'timestamp',
        }

