from rest_framework import serializers

from apps.pizzas.serializer import PizzaSerializer
from apps.pizzas_shop.models import PizzaShopModel


class PizzaShopSerializer(serializers.ModelSerializer):
    pizzas = PizzaSerializer(many=True, read_only=True)

    class Meta:
        model = PizzaShopModel
        fields = ('id', 'name', 'pizzas')
