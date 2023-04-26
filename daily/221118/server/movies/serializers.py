from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from django.contrib.auth import get_user_model
from .models import *

# from django.contrib.auth.models import User
User = get_user_model()

class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = ('id', 'name')

class DirectorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Director
        fields = ('id', 'name', 'role', 'img_url', 'description', 'movies')

class ActorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Actor
        fields = ('id', 'name', 'role', 'img_url', 'description', 'movies')

class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = ('id', 'title', 'title_en', 'rate', 'img_url', 'description', 'directors', 'actors', 'genres', 'open_date')

class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = ('id', 'content', 'score', 'movie', 'user')
    
class WorldcupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Worldcup
        fields = ('id', 'movies')

class UserCreationSerializer(serializers.ModelSerializer):
    # pass
    class Meta:
        model = User
        fields = ('id', 'username', 'nickname', 'password',)

class UserSerializer(serializers.ModelSerializer):
    review_set = ReviewSerializer(many=True)
    movies = MovieSerializer(many=True)
    class Meta:
        model = User
        fields = ('id', 'username', 'review_set', 'movies')

    