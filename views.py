from django.shortcuts import render
from rest_framework import viewsets
from .models import Item
from .serializers import ItemSerializer
from django.http import HttpResponse


def home(request):
    return HttpResponse("Welcome to the Inventory API!")

class ItemViewSet(viewsets.ModelViewSet):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer

# Create your views here.
