from rest_framework import generics
from movies.models import Movie
from core.permissions import GlobalDefaultPermission
from rest_framework.permissions import IsAuthenticated
from movies.serializers import MovieModelSerializer


class MovieCreateListView(generics.ListCreateAPIView):
    permission_classes = (IsAuthenticated, GlobalDefaultPermission,)
    queryset = Movie.objects.all()
    serializer_class = MovieModelSerializer


class MovieRetriveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthenticated, GlobalDefaultPermission,)
    queryset = Movie.objects.all()
    serializer_class = MovieModelSerializer
