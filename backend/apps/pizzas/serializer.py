from rest_framework import serializers

from apps.pizzas.models import PizzaModel
from apps.pizzas_shop.models import PizzaShopModel


class PizzaSerializer(serializers.ModelSerializer):
    class Meta:
        model = PizzaModel
        fields = ('id', 'name', 'size', 'price', 'day', 'created_at', 'updated_at')

    def create(self, validated_data):
        pizza_shop = PizzaShopModel.objects.first()
        return PizzaModel.objects.create(**validated_data, pizza_shop_id=pizza_shop.id)


    # def validate_price(self, price):
    #     if price <= 0:
    #         raise serializers.ValidationError('Price must be grater than 0')
    #     return price
    #
    # def validate(self, attrs):
    #     price = attrs.get('price')
    #     size = attrs.get('size')
    #
    #     if price == size:
    #         raise serializers.ValidationError('Price can not be equal to size')
    #     return attrs


class PizzaPhotoSerializer(serializers.ModelSerializer):
    class Meta:
        model = PizzaModel
        fields = ('photo',)