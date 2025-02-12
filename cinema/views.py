from rest_framework import viewsets

from cinema.models import (
    Movie,
    Actor,
    CinemaHall,
    Genre,
    MovieSession
)
from cinema.serializers import (
    MovieListSerializer,
    MovieDetailSerializer,
    GenreSerializer,
    ActorSerializer,
    CinemaHallSerializer,
    MovieSessionListSerializer,
    MovieSessionDetailSerializer, MovieSessionSerializer, MovieSerializer
)


class GenreViewSet(viewsets.ModelViewSet):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer


class ActorViewSet(viewsets.ModelViewSet):
    queryset = Actor.objects.all()
    serializer_class = ActorSerializer


class CinemaHallViewSet(viewsets.ModelViewSet):
    queryset = CinemaHall.objects.all()
    serializer_class = CinemaHallSerializer


class MovieViewSet(viewsets.ModelViewSet):
    queryset = Movie.objects.all()

    def get_queryset(self):
        queryset = self.queryset

        if self.action in (
            "list",
            "retrieve"
        ):
            queryset = queryset.prefetch_related("genres", "actors")
        return queryset

    def get_serializer_class(self):
        if self.action == "retrieve":
            return MovieDetailSerializer
        elif self.action == "list":
            return MovieListSerializer
        return MovieSerializer


class MovieSessionViewSet(viewsets.ModelViewSet):
    queryset = MovieSession.objects.all()

    def get_queryset(self):
        queryset = self.queryset

        if self.action in (
            "list",
            "retrieve"
        ):
            queryset = queryset.select_related(
                "movie",
                "cinema_hall"
            )
        return queryset

    def get_serializer_class(self):
        if self.action == "list":
            return MovieSessionListSerializer
        elif self.action == "retrieve":
            return MovieSessionDetailSerializer
        return MovieSessionSerializer
