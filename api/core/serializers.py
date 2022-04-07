from rest_framework import serializers

from movie.models import Movie, Serial, Person, Review


class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = '__all__'        


class MovieShortSerializer(serializers.ModelSerializer):
    genres = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Movie
        fields = ('id', 'name', 'genres')
    
    def get_genres(self, obj):
        return obj.genres_names


class SerialSerializer(serializers.ModelSerializer):
    class Meta:
        model = Serial
        fields = '__all__'


class PersonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Person
        fields = '__all__'


class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = '__all__'


class CreateReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = ('movie', 'author', 'text')