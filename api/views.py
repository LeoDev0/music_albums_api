from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import status
from .serializers import AlbumSerializer, BandSerializer
from .models import Album, Band
from rest_framework.views import APIView
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
import pdb


class BandList(APIView):

    def get(self, request):
        queryset = Band.objects.all()
        serializer = BandSerializer(queryset, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = BandSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(status=status.HTTP_400_BAD_REQUEST)
            

class BandDetails(APIView):

    def get(self, request, pk):
        queryset = get_object_or_404(Band, pk=pk)
        serializer = BandSerializer(queryset)
        return Response(serializer.data)

    def put(self, request, pk):
        queryset = get_object_or_404(Band, pk=pk)
        serializer = BandSerializer(queryset, request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(status=status.HTTP_202_ACCEPTED)
        return Response(status=status.HTTP_400_BAD_REQUEST)


class AlbumList(APIView):

    def get(self, request):
        # queryset = Album.objects.all().order_by('-id')
        queryset = Album.objects.all()
        serializer = AlbumSerializer(queryset, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = AlbumSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()

            # Adding +1 to counter (count number of albums associated with the band) on Bands
            band = Band.objects.get(pk=serializer.data['band'])
            band.counter += 1
            band.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class AlbumDetails(APIView):

    def get(self, request, pk):
        queryset = get_object_or_404(Album, pk=pk)
        serializer = AlbumSerializer(queryset)
        return Response(serializer.data)

    def delete(self, request, pk):
        queryset = get_object_or_404(Album, pk=pk)
        queryset.delete()

        # Adding -1 to counter (count number of albums associated with the band) on Bands
        serializer = AlbumSerializer(queryset, data=request.data)
        band = Band.objects.get(pk=serializer.initial_data['band'])
        band.counter -= 1
        band.save()

        return Response(status=status.HTTP_204_NO_CONTENT)

    def put(self, request, pk):
        queryset = get_object_or_404(Album, pk=pk)
        serializer = AlbumSerializer(queryset, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(status=status.HTTP_202_ACCEPTED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

