from django.urls import path
from . import views

urlpatterns = [
    path("notes/", views.NoteListCreateView.as_view(), name="note_list_create"),
    path("notes/<int:pk>/", views.NoteDetailView.as_view(), name="note_detail"),
    path("notes/<int:pk>/delete/", views.NoteDeleteView.as_view(), name="note_delete"), 
]
