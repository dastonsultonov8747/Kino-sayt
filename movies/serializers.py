from .models import Serial, Serial_item, Kinolar, Multfilm, Anime, Anime_item
from rest_framework import serializers


class SerialSerializer(serializers.ModelSerializer):
    class Meta:
        model = Serial
        fields = '__all__'


class SerialItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Serial_item
        fields = '__all__'


class KinolarSerializer(serializers.ModelSerializer):
    class Meta:
        model = Kinolar
        fields = '__all__'


class MultfilmSerializer(serializers.ModelSerializer):
    class Meta:
        model = Multfilm
        fields = '__all__'


class AnimeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Anime
        fields = '__all__'


class AnimeItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Anime_item
        fields = '__all__'
