from django.shortcuts import get_object_or_404

from rest_framework import viewsets

from rest_framework.decorators import action

from rest_framework.response import Response

from rest_framework.mixins import RetrieveModelMixin

from .models import Movie, Person, Review, Serial

from core import serializers

from .viewsets import BaseGenericViewSet

from .mixins import CinemaMixin


class MovieViewSet(CinemaMixin, BaseGenericViewSet):
    queryset = Movie.objects.all()
    serializer_class = serializers.MovieSerializer

    def retrieve(self, request, pk):
        '''Детальная информация о фильме/сериале'''
        try:
            movie = get_object_or_404(Serial, id=pk)
            serialized_movie = serializers.SerialSerializer(movie)
        except:
            movie = get_object_or_404(Movie, id=pk)
            serialized_movie = serializers.MovieSerializer(movie)

        return Response(serialized_movie.data, status=200)

    @action(
        methods=['get'],
        detail=False,
        url_path=r'genre/(?P<pk>[^/.]+)',
        url_name='search by genre',
        serializer_class=serializers.MovieShortSerializer,
    )
    def search_by_genre(self, request, pk):
        '''Поиск фильмов/сериалов по жанру'''
        return super().search_by_genre(request, pk)

    @action(
            methods=['get'],
            detail=True,
            url_path='reviews',
            url_name='get all reviews',
            serializer_class=serializers.ReviewSerializer,
    )
    def get_all_reviews(self, request, *args, **kwargs):
        '''Поиск всех отзывов к фильму/сериалу'''
        return super().get_all_reviews(request)

    @action(
        methods=['post'],
        detail=True,
        url_path='create_review',
        url_name='create review',
        serializer_class=serializers.CreateReviewSerializer,
    )
    def create_review(self, request, pk):
        '''Создание отзыва к фильму/сериалу'''
        return super().create_review(request, id)

    @action(
        methods=['post'],
        detail=False,
        url_path=r'update_review/(?P<pk>[^/.]+)',
        url_name='search by genre',
        queryset=Review.objects.all(),
        serializer_class=serializers.CreateReviewSerializer,
    )
    def update_review(self, request, pk):
        '''Отредактировать отзыв к фильму/сериалу'''
        return super().update_review(request, pk)

    @action(
            methods=['post'],
            detail=False,
            url_path=r'delete_review/(?P<pk>[^/.]+)',
            url_name='delete review',
            queryset=Review.objects.all(),
    )
    def delete_review(self, request, pk):
        '''Удаление отзыва к фильму/сериалу'''
        return super().delete_review(request, pk)

    @action(
            methods=['get'],
            detail=False,
            url_path=r'genre/(?P<pk>[^/.]+)',
            url_name='search by genre',
            serializer_class=serializers.MovieShortSerializer
    )
    def search_by_genre(self, request, pk):
        '''Найти фильм/сериал по жанру'''
        return super().search_by_genre(request, pk)


class PersonViewSet(RetrieveModelMixin, viewsets.GenericViewSet):
    queryset = Person.objects.all()
    serializer_class = serializers.PersonSerializer