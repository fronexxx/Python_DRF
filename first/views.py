from rest_framework.views import APIView
from rest_framework.response import Response

class FirstView(APIView):
    def get(self, *args, **kwargs):
        print(self.request.query_params.dict())
        return Response('Hello from get')


    def post(self, *args, **kwargs):
        print(self.request.query_params.dict())
        print(self.request.data)
        return Response('Hello from get')

    def put(self, *args, **kwargs):
        return Response('Hello from get')

    def patch(self, *args, **kwargs):
        return Response('Hello from get')

    def delete(self, *args, **kwargs):
        return Response('Hello from get')

class SecondView(APIView):
    def get(self, *args, **kwargs):
        print(kwargs)
        return Response(kwargs['age'])
