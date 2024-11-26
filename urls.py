
from django.urls import path
from . import views

urlpatterns = [
    path('', views.counter, name='counter'),  # The counter view is accessible at the root
]