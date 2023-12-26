from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="hello"),
    path('user/', views.user, name="user"),
    path('results/', views.results, name="results")
]
