from rest_framework import viewsets
from .models import AllProducts
from .serializers import AllProductSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework.exceptions import APIException


class ProductViewSet(viewsets.ViewSet):
    def list(self, request):
        products = AllProducts.objects.all()
        ser = AllProductSerializer(products, many=True)
        return Response(ser.data)

    def create(self, request):
        product_data = AllProductSerializer(data=request.data)
        product_data.is_valid(raise_exception=True)
        product_data.save()
        return Response(product_data.data, status=status.HTTP_201_CREATED)

    def retrieve(self, request, pk=None):
        pass

    def update(self, request, pk=None):
        pass

    def destroy(self, request, pk=None):
        pass
