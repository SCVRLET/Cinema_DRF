from rest_framework import serializers

from movie.models import Movie, Serial, Person


class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = '__all__'        


class SerialSerializer(serializers.ModelSerializer):
    class Meta:
        model = Serial
        fields = '__all__'


class PersonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Person
        fields = '__all__'