from django.urls import path
from . import views

urlpatterns = [
    path('', views.PostSentence.as_view())
]
