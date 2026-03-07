from django.shortcuts import render
from rest_framework import viewsets
from .serializers import BookSerializer
from .models import BookData

# Create your views here.

class BookViewSet(viewsets.ModelViewSet):
    queryset = BookData.objects.all()
    serializer_class = BookSerializer


class FictionViewSet(viewsets.ModelViewSet):
    queryset = BookData.objects.filter(category='fiction')
    serializer_class = BookSerializer


class FantasyViewSet(viewsets.ModelViewSet):
    queryset = BookData.objects.filter(category='fantasy')
    serializer_class = BookSerializer


class MysteryViewSet(viewsets.ModelViewSet):
    queryset = BookData.objects.filter(category='mystery')
    serializer_class = BookSerializer


class RomanceViewSet(viewsets.ModelViewSet):
    queryset = BookData.objects.filter(category='romance')
    serializer_class = BookSerializer


class HorrorViewSet(viewsets.ModelViewSet):
    queryset = BookData.objects.filter(category='horror')
    serializer_class = BookSerializer


class ScienceFictionViewSet(viewsets.ModelViewSet):
    queryset = BookData.objects.filter(category='sci-fi')
    serializer_class = BookSerializer


class BiographyViewSet(viewsets.ModelViewSet):
    queryset = BookData.objects.filter(category='biography')
    serializer_class = BookSerializer


class HistoryViewSet(viewsets.ModelViewSet):
    queryset = BookData.objects.filter(category='history')
    serializer_class = BookSerializer


class PoetryViewSet(viewsets.ModelViewSet):
    queryset = BookData.objects.filter(category='poetry')
    serializer_class = BookSerializer


class KidsViewSet(viewsets.ModelViewSet):
    queryset = BookData.objects.filter(category='kids')
    serializer_class = BookSerializer