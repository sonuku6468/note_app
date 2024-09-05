from django.urls import path
from .views import CreateNoteView, FetchNoteView, QueryNotesView, UpdateNoteView

urlpatterns = [
    path('notes/', CreateNoteView.as_view(), name='create-note'),
    path('notes/<int:pk>/', FetchNoteView.as_view(), name='fetch-note'),
    path('notes/search/', QueryNotesView.as_view(), name='query-notes'),
    path('notes/update/<int:pk>/', UpdateNoteView.as_view(), name='update-note'),
]
