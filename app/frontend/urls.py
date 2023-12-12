from django.urls import path
from . import views

urlpatterns = [
    # gallery
    path('', views.home, name='home'),
]
