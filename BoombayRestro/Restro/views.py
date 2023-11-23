from django.shortcuts import render ,HttpResponse
from rest_framework import viewsets
from .serializer import categorySerializer
from .models import category



def index(request):
    return HttpResponse("Hi Pooja")

class categoryView(viewsets.ModelViewSet):
    serializer_class = categorySerializer
    queryset = category.objects.all()
