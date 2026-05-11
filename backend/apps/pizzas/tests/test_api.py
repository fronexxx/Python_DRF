from django.contrib.auth import get_user_model
from django.urls.base import reverse

from rest_framework import status
from rest_framework.test import APITestCase

from core.dataclasses.user_dataclass import User

from apps.pizzas_shop.models import PizzaShopModel

from ..models import PizzaModel

UserModel  = get_user_model()


class PizzaAPITestCase(APITestCase):
    def setUp(self):
        pizza_shop = PizzaShopModel.objects.create(name='Pizza Shop')
        self.pizza1 = PizzaModel.objects.create(
            name='pizza1',
            size=33,
            price=300,
            day='Monday',
            pizza_shop=pizza_shop
        )

        self.pizza2 = PizzaModel.objects.create(
            name='pizza2',
            size=33,
            price=300,
            day='Monday',
            pizza_shop=pizza_shop
        )

        self.pizza3 = PizzaModel.objects.create(
            name='pizza3',
            size=33,
            price=300,
            day='Monday',
            pizza_shop=pizza_shop
        )

    def _authenticate(self):
        user: User = UserModel.objects.create_user(email='admin@gmail.com', password='admin')
        user.is_active = True
        user.save()
        res = self.client.post(reverse('auth_login'), {'email': user.email, 'password': 'admin'})
        self.client.credentials(HTTP_AUTHORIZATION='Bearer ' + res.data['access'])

    def test_get_all_pizzas(self):
        res = self.client.get(reverse('pizza_list_create'))
        self.assertEqual(res.status_code, status.HTTP_200_OK)
        self.assertEqual(len(res.data['data']), 3)
        pizza_names = list(reversed(['pizza1', 'pizza2', 'pizza3']))
        for i, pizza in enumerate(PizzaModel.objects.all()):
            self.assertEqual(pizza.name, pizza_names[i])

    def test_create_pizza_without_auth(self):
        count_before = PizzaModel.objects.count()
        res = self.client.post(
            reverse('pizza_list_create'),
            data={
                'name': 'asd',
                'size': 20,
                'price': 222,
                'day': 'Monday'
            }
        )
        self.assertEqual(res.status_code, status.HTTP_401_UNAUTHORIZED)
        count_after = PizzaModel.objects.count()
        self.assertEqual(count_after - count_before, 0)

    def test_create_pizza_with_auth(self):
        self._authenticate()
        count_before = PizzaModel.objects.count()
        res = self.client.post(
            reverse('pizza_list_create'),
            data={
                'name': 'Asd',
                'size': 20,
                'price': 222,
                'day': 'Monday'
            }
        )
        self.assertEqual(res.status_code, status.HTTP_201_CREATED)
        count_after = PizzaModel.objects.count()
        self.assertEqual(count_after - count_before, 1)
        self.assertEqual(res.data['name'], 'Asd')
