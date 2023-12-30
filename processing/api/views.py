from rest_framework.response import Response
from rest_framework.decorators import api_view
from bookpedia.models import Autor, Livro
from .serializers import AutorSerializer, LivroSerializer

@api_view(['GET'])
def get_home(request):
    autor = Autor.objects.all()
    serializer = AutorSerializer(autor, many=True)
    return Response(serializer.data)

@api_view(['POST'])
def post_home(request):
    serializer = AutorSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)