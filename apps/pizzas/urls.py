from django.urls import path

from apps.pizzas.views import PizzaListView, PizzaUpdateRetrieveDestroyView

urlpatterns = [
    path('', PizzaListView.as_view()),
    path('/<int:pk>', PizzaUpdateRetrieveDestroyView.as_view()),
]