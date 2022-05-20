from posixpath import basename
from django.urls import path, include
from profiles_api import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register('hello-viewset', views.HelloViewSet,basename='hello-viewset')

urlpatterns = [
    path('hello-view/', views.HelloApiView.as_view()),
    path('', include(router.urls)),
]
