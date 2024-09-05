from django.shortcuts import render

from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status
from .models import Note
from .serializers import NoteSerializer

class CreateNoteView(generics.CreateAPIView):
    queryset = Note.objects.all()
    serializer_class = NoteSerializer

class FetchNoteView(generics.RetrieveAPIView):
    queryset = Note.objects.all()
    serializer_class = NoteSerializer

class QueryNotesView(generics.ListAPIView):
    serializer_class = NoteSerializer

    def get_queryset(self):
        title_substring = self.request.query_params.get('title', '')
        return Note.objects.filter(title__icontains=title_substring)

class UpdateNoteView(generics.UpdateAPIView):
    queryset = Note.objects.all()
    serializer_class = NoteSerializer

