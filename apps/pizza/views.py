from rest_framework.generics import ListAPIView, ListCreateAPIView, RetrieveUpdateDestroyAPIView

from apps.pizza.filter import filter_pizza
from apps.pizza.models import PizzaModel
from apps.pizza.serializer import PizzaSerializer


class PizzaListCreateView(ListAPIView):
    serializer_class = PizzaSerializer

    def get_queryset(self):
            return filter_pizza(self.request.query_params)

class PizzaRetrieveUpdateDestroyView(RetrieveUpdateDestroyAPIView):
    queryset = PizzaModel.objects.all()
    serializer_class = PizzaSerializer
    http_method_names = ['get', 'put', 'delete']
