from rest_framework.response import Response
from rest_framework.decorators import api_view
from base.models import Producto
from .serializers import ProductoSerializer

@api_view(['GET'])
def getData(request):
    productos = Producto.objects.all()
    serializer = ProductoSerializer(productos, many=True)
    return Response(serializer.data)


@api_view(['POST'])
def createProducto(request):
    serializer = ProductoSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)