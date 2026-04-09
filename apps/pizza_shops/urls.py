from django.urls import path

from apps.pizza_shops.views import PizzaShopAddPizzaView, PizzaShopListCreateView

urlpatterns = [
    path('', PizzaShopListCreateView.as_view()),
    path('/<int:pk>/pizzas', PizzaShopAddPizzaView.as_view())
]