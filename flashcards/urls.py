from django.urls import path
from .views import add_flashcard

urlpatterns = [
    path("add/", view=add_flashcard, name="add_flashcard"),
]
