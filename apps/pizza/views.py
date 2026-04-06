from itertools import count

from django.db.models import Q
from django.db.models.aggregates import Min, Max, Count
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.request import Request
from apps.pizza.filter import filter_pizza
from apps.pizza.models import PizzaModel
from apps.pizza.serializer import PizzaSerializer
from rest_framework.generics import GenericAPIView, RetrieveUpdateDestroyAPIView, ListCreateAPIView
from rest_framework.mixins import ListModelMixin, CreateModelMixin, UpdateModelMixin, RetrieveModelMixin, DestroyModelMixin

# class PizzaListCreateView(APIView):
#
#     def get(self, request: Request, *args, **kwargs):
#         # pizzas = PizzaModel.objects.filter(Q(size=10) | Q(name='paperoni3')).exclude(price=300).order_by('size', '-price').reverse()
#         # pizzas = PizzaModel.objects.all().values('id', 'name', 'price')
#         # pizzas = PizzaModel.objects.aggregate(Min('size'), Max('price'))
#         # print(pizzas)
#         # annotate = PizzaModel.objects.values('name').annotate(count=Count('name'))
#         # print(annotate)
#         qs = filter_pizza(request.query_params)
#         serializer = PizzaSerializer(qs, many=True)
#         return Response(serializer.data, status.HTTP_200_OK)
#         # return Response('ok')

#     def post(self, *args, **kwargs):
#         data = self.request.data
#         serializer = PizzaSerializer(data=data)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         return Response(serializer.data, status.HTTP_201_CREATED)
#
# class PizzaRetrieveUpdateDestroyView(APIView):
#     def get(self, *args, **kwargs):
#         pk = kwargs['pk']
#         try:
#             pizza = PizzaModel.objects.get(pk=pk)
#         except PizzaModel.DoesNotExist:
#             return Response({'details': 'not found'}, status=status.HTTP_404_NOT_FOUND)
#
#         serializer = PizzaSerializer(pizza)
#         return Response(serializer.data, status.HTTP_200_OK)
#
#     def put(self, *args, **kwargs):
#         pk = kwargs['pk']
#         data = self.request.data
#
#         try:
#             pizza = PizzaModel.objects.get(pk=pk)
#         except PizzaModel.DoesNotExist:
#             return Response({'details': 'not found'}, status=status.HTTP_404_NOT_FOUND)
#
#         serializer = PizzaSerializer(pizza, data=data)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         return Response(serializer.data, status.HTTP_200_OK)
#
#     def delete(self, *args, **kwargs):
#         pk = kwargs['pk']
#
#         try:
#             PizzaModel.objects.get(pk=pk).delete()
#         except PizzaModel.DoesNotExist:
#             return Response({'details': 'not found'}, status=status.HTTP_404_NOT_FOUND)
#
#         return Response(status=status.HTTP_204_NO_CONTENT)

# class PizzaListCreateView(GenericAPIView, ListModelMixin, CreateModelMixin):
#     # queryset = PizzaModel.objects.all()
#     serializer_class = PizzaSerializer
#
#     def get_queryset(self):
#         return filter_pizza(self.request.query_params)
#
#     def get(self, request, *args, **kwargs):
#         return super().list(request, *args, **kwargs)
#
#     def post(self, request, *args, **kwargs):
#         return super().create(request, *args, **kwargs)

    # def get(self, request: Request, *args, **kwargs):
    #     qs = filter_pizza(request.query_params)
    #     serializer = PizzaSerializer(qs, many=True)
    #     return Response(serializer.data, status.HTTP_200_OK)
    #
    # def post(self, *args, **kwargs):
    #     data = self.request.data
    #     serializer = PizzaSerializer(data=data)
    #     serializer.is_valid(raise_exception=True)
    #     serializer.save()
    #     return Response(serializer.data, status.HTTP_201_CREATED)

# class PizzaRetrieveUpdateDestroyView(GenericAPIView, RetrieveModelMixin, UpdateModelMixin, DestroyModelMixin):
#     queryset = PizzaModel.objects.all()
#     serializer_class = PizzaSerializer
#
#     def get(self, request, *args, **kwargs):
#         return super().retrieve(request, *args, **kwargs)
#
#     def put(self, request, *args, **kwargs):
#         return super().update(request, *args, **kwargs)
#
#     def patch(self, request, *args, **kwargs):
#         return super().partial_update(request, *args, **kwargs)
#
#     def delete(self, request, *args, **kwargs):
#         return super().destroy(request, *args, **kwargs)

    # def get(self, *args, **kwargs):
    #     pizza = self.get_object()
    #     # pk = kwargs['pk']
    #     # try:
    #     #     pizza = PizzaModel.objects.get(pk=pk)
    #     # except PizzaModel.DoesNotExist:
    #     #     return Response({'details': 'not found'}, status=status.HTTP_404_NOT_FOUND)
    #
    #     serializer = PizzaSerializer(pizza)
    #     return Response(serializer.data, status.HTTP_200_OK)

    # def put(self, *args, **kwargs):
    #     pizza = self.get_object()
    #     # pk = kwargs['pk']
    #     #
    #     # try:
    #     #     pizza = PizzaModel.objects.get(pk=pk)
    #     # except PizzaModel.DoesNotExist:
    #     #     return Response({'details': 'not found'}, status=status.HTTP_404_NOT_FOUND)
    #
    #     data = self.request.data
    #     serializer = PizzaSerializer(pizza, data=data, partial=True)
    #     serializer.is_valid(raise_exception=True)
    #     serializer.save()
    #     return Response(serializer.data, status.HTTP_200_OK)

    # def delete(self, *args, **kwargs):
    #     # pk = kwargs['pk']
    #     #
    #     # try:
    #     #     PizzaModel.objects.get(pk=pk).delete()
    #     # except PizzaModel.DoesNotExist:
    #     #     return Response({'details': 'not found'}, status=status.HTTP_404_NOT_FOUND)
    #     self.get_object().delete()
    #     return Response(status=status.HTTP_204_NO_CONTENT)

class PizzaListCreateView(ListCreateAPIView):
    # queryset = PizzaModel.objects.all()
    serializer_class = PizzaSerializer

    def get_queryset(self):
            return filter_pizza(self.request.query_params)

class PizzaRetrieveUpdateDestroyView(RetrieveUpdateDestroyAPIView):
    queryset = PizzaModel.objects.all()
    serializer_class = PizzaSerializer
    http_method_names = ['get', 'put', 'delete']
