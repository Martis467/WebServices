import requests
from models.NoteModel import Note


class PauliusNoteService:

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
