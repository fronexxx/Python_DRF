from django.urls.base import reverse

from rest_framework import status
from rest_framework.test import APITestCase

from apps.pizzas.models import PizzaModel
from apps.pizzas_shop.models import PizzaShopModel


class PizzaApiTestCase(APITestCase):
    def setUp(self):
        pizza_shop = PizzaShopModel.objects.create(name='Pizza Shop')

        PizzaModel.objects.create(
            name='Pizza1',
            size=40,
            price=330,
            day='Monday',
            pizza_shop=pizza_shop,
        )
        PizzaModel.objects.create(
            name='Pizza2',
            size=40,
            price=330,
            day='Monday',
            pizza_shop=pizza_shop,
        )

        PizzaModel.objects.create(
            name='Pizza3',
            size=40,
            price=330,
            day='Monday',
            pizza_shop=pizza_shop,
        )

    def test_get_all_pizzas(self):
        res = self.client.get(reverse('pizza_list_create'))
        self.assertEqual(res.status_code, status.HTTP_200_OK)
        self.assertEqual(len(res.data['data']), 3)
