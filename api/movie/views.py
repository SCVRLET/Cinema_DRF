from django.shortcuts import render, get_object_or_404

from rest_framework import viewsets

from rest_framework.decorators import action

from rest_framework.response import Response

from rest_framework.mixins import RetrieveModelMixin

from .models import Movie, Person, Serial

from core import serializers


class MovieViewSet(RetrieveModelMixin, viewsets.GenericViewSet):
    queryset = Movie.objects.all()
    serializer_class = serializers.MovieSerializer


class PersonViewSet(RetrieveModelMixin, viewsets.GenericViewSet):
    queryset = Person.objects.all()
    serializer_class = serializers.PersonSerializer