from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from .models import Note

class NotesTests(APITestCase):
    def test_create_note(self):
        url = reverse('create-note')
        data = {'title': 'Test Title', 'body': 'Test Body'}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_fetch_note_by_id(self):
        note = Note.objects.create(title='Test', body='Test Body')
        url = reverse('fetch-note', kwargs={'pk': note.id})
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_query_notes_by_title_substring(self):
        Note.objects.create(title='Sample', body='Sample Body')
        url = reverse('query-notes') + '?title=Samp'
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertGreater(len(response.data), 0)

    def test_update_note(self):
        note = Note.objects.create(title='Test', body='Test Body')
        url = reverse('update-note', kwargs={'pk': note.id})
        data = {'title': 'Updated Title', 'body': 'Updated Body'}
        response = self.client.put(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
