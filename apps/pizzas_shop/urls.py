from django.urls import path

from apps.pizzas_shop.views import PizzaCreateAddToPizzaShop, PizzaShopListCreateView

urlpatterns = [
    path('', PizzaShopListCreateView.as_view()),
    path('/<int:pk>/pizzas', PizzaCreateAddToPizzaShop.as_view())
]