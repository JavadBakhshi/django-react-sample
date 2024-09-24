from django.urls import path, include
from .views import NoteListCreate, NoteListDelete

urlpatterns = [
    path("notes/", NoteListCreate.as_view(), name="note-list"),
    path("notes/<int:pk>/", NoteListDelete.as_view(), name="note-delete"),
    ]

