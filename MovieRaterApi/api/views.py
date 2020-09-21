from rest_framework import viewsets,status
from rest_framework.response import Response
from .models import Movie,Rating
from .serializers import MovieSerializer,RatingSerializer
from rest_framework.decorators import action
# Create your views here.

class MovieViewSet(viewsets.ModelViewSet):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer

    @action(detail=True,methods=['POST'])
    #detail=True 1 specific movie 
    def rate_movie(self,request):
        response = {'message':'itsworks'}
        return Response(response,status=status.HTTP_200_OK)
class RatingViewSet(viewsets.ModelViewSet):
    queryset = Rating.objects.all()
    serializer_class = RatingSerializer
    