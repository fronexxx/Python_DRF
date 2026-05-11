from rest_framework import status
from rest_framework.generics import GenericAPIView, ListCreateAPIView
from rest_framework.response import Response

from apps.pizzas.serializer import PizzaSerializer
from apps.pizzas_shop.models import PizzaShopModel
from apps.pizzas_shop.serializer import PizzaShopSerializer


class PizzaShopListCreateView(ListCreateAPIView):
    """
    get:
        get all pizza shop list
    post:
        create new pizza shop
    """
    queryset = PizzaShopModel.objects.all()
    serializer_class = PizzaShopSerializer


class PizzaCreateAddToPizzaShop(GenericAPIView):
    def get_serializer(self):
        return None

    queryset = PizzaShopModel.objects.all()

    def post(self, *args, **kwargs):
        pizza_shop = self.get_object()
        data = self.request.data
        serializer = PizzaSerializer(data=data)
        serializer.is_valid(raise_exception=True)
        serializer.save(pizza_shop=pizza_shop)
        shop_serializer = PizzaShopSerializer(pizza_shop)
        return Response(shop_serializer.data, status.HTTP_201_CREATED)
