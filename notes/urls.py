from django.urls import path
from . import views
urlpatterns = [
    path('', views.homepage),
    path('notes/',views.notes),
    path('notesview/',views.viewnotes),
]