from rest_framework import viewsets
from .models import AllProducts
from .serializers import AllProductSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework.authentication import SessionAuthentication
from rest_framework.permissions import IsAuthenticated


class ProductViewSet(viewsets.ViewSet):
    authentication_classes = [SessionAuthentication]
    permission_classes = [IsAuthenticated]

    def list(self, request):
        try:
            products = AllProducts.objects.all()
            ser = AllProductSerializer(products, many=True)
            return Response(ser.data)
        except:
            return Response({'message': 'something went wrong'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def create(self, request):
        try:
            product_data = AllProductSerializer(data=request.data)
            product_data.is_valid(raise_exception=True)
            product_data.save()
            return Response(product_data.data, status=status.HTTP_201_CREATED)
        except:
            return Response({'message': 'Bad Request'}, status=status.HTTP_400_BAD_REQUEST)

    def retrieve(self, request, pk=None):
        try:
            product = AllProducts.objects.get(pk=pk)
            ser = AllProductSerializer(product)
            return Response(ser.data)
        except:
            return Response({'message': 'Product not found'}, status=status.HTTP_404_NOT_FOUND)

    def update(self, request, pk=None):
        try:
            product = AllProducts.objects.get(id=pk)
            product_data = AllProductSerializer(
                product, data=request.data, partial=True)
            product_data.is_valid(raise_exception=True)
            product_data.save()
            return Response(product_data.data, status=status.HTTP_202_ACCEPTED)
        except:
            return Response({'message': 'Bad Request'}, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, pk=None):
        try:
            product = AllProducts.objects.get(id=pk)
            product.delete()
            return Response({'message': 'Success'}, status=status.HTTP_204_NO_CONTENT)
        except:
            return Response({'message': 'Product not found'}, status=status.HTTP_404_NOT_FOUND)
