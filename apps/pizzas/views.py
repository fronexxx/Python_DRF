from rest_framework.generics import ListAPIView, ListCreateAPIView, RetrieveUpdateDestroyAPIView

from apps.pizzas.filter import filter_pizzas
from apps.pizzas.models import PizzaModel
from apps.pizzas.serializer import PizzaSerializer


class PizzaListView(ListAPIView):
    serializer_class = PizzaSerializer

    def get_queryset(self):
        return filter_pizzas(self.request.query_params)

class PizzaUpdateRetrieveDestroyView(RetrieveUpdateDestroyAPIView):
    queryset = PizzaModel.objects.all()
    serializer_class = PizzaSerializer
    http_method_names = ['get', 'put', 'delete']
