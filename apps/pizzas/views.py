
from rest_framework.generics import ListAPIView, RetrieveUpdateDestroyAPIView

from apps.pizzas.filter import pizza_filter
from apps.pizzas.models import PizzaModel
from apps.pizzas.serializer import PizzaSerializer


class PizzaListCreateView(ListAPIView):
    serializer_class = PizzaSerializer

    def get_queryset(self):
        return pizza_filter(self.request.query_params)


class PizzaRetrieveUpdateDestroyView(RetrieveUpdateDestroyAPIView):
    queryset = PizzaModel.objects.all()
    serializer_class = PizzaSerializer
    http_method_names = ['get', 'put', 'delete']

