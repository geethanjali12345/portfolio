from django.urls import path
from .views import HomeView,home_view

urlpatterns = [
    path('', home_view,name='home'),
]