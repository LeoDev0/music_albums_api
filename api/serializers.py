from rest_framework import serializers
from api.models import Album, Band


class AlbumSerializer(serializers.ModelSerializer):
    class Meta:
        model = Album
        fields = '__all__'
        # fields = ['id', 'title', 'cover']


class BandSerializer(serializers.ModelSerializer):
    class Meta:
        model = Band
        fields = '__all__'