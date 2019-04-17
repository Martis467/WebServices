import requests
from models.NoteModel import Note
from enum import Enum


class PauliusNoteService:
    Status = Enum('Status','Success NoteExists NoteDoesNotExist')

    def __init__(self):
        self.url = "http://193.219.91.103:15983/"

    def get_all_notes(self):
        r = requests.get(self.url + 'notes')
        json_array = r.json()

        body = json_array['data']

        notes = []

        for obj in body:
            notes.append(Note(obj))

        return notes

    def add_new_note(self, note):
        r = requests.post(self.url + 'notes', data=note)

        if r.status_code == 201:
            return True
        else:
            return False

    def delete_note(self, title):
        r = requests.delete(self.url + f'notes/{title}')

        if r.status_code == 200:
            return True
        else:
            return False

