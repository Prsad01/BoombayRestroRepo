from django.urls import path 
from Restro import views
from rest_framework.routers import DefaultRouter

router  = DefaultRouter(trailing_slash=False)

router.register('category', views.categoryView , basename='category')

urlpatterns = [
   path('index', views.index)
]+router.urls
