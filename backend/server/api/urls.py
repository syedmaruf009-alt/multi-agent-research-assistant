"""Connects the HTTP request → Django view function"""

from django.urls import path
from .views import ask_question

#List of all routes for this app. If this variable does not exist, Django will error.
urlpatterns = [
    path("ask/", ask_question),
]