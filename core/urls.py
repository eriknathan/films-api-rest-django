from django.contrib import admin
from django.urls import path
from genres.views import GenreCreateListView, GenreRetriveUpdateDestroyView
from actors.views import ActorCreateListView, ActorRetriveUpdateDestroyView
from movies.views import MovieCreateListView, MovieRetriveUpdateDestroyView


urlpatterns = [
    path('admin/', admin.site.urls),

    path('genres/', GenreCreateListView.as_view(), name='genre-create-list'),
    path('genres/<int:pk>/', GenreRetriveUpdateDestroyView.as_view(),
         name='genre-detail-view'),

    path('actors/', ActorCreateListView.as_view(), name='actors-create-list'),
    path('actors/<int:pk>/', ActorRetriveUpdateDestroyView.as_view(),
         name='actors-detail-view'),

    path('movies/', MovieCreateListView.as_view(), name='movies-create-list'),
    path('movies/<int:pk>/', MovieRetriveUpdateDestroyView.as_view(),
         name='movies-detail-view'),
]
