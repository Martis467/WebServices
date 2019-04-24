import requests
from models.NoteModel import Note


class PauliusNoteService:

    def __init__(self):
        self.url = "http://usr:5009/"

    def get_all_notes(self):
        notes = []
        try:
            r = requests.get(self.url + 'notes')
            requests.RequestException()
            json_array = r.json()

            body = json_array['data']

            for obj in body:
                notes.append(Note(obj))

        except requests.exceptions.RequestException as e:
            print("paulius_service is down")

        return notes

    def get_single_note(self, title):
        try:
            r = requests.get(self.url + 'notes/' + title)
            json_array = r.json()

            body = json_array['data']

            if r.status_code == 200:
                return Note(body)

        except requests.exceptions.RequestException as e:
            print("paulius_service is down")

        return None

    def add_new_note(self, note):
        try:
            r = requests.post(self.url + 'notes', data=note)

            if r.status_code == 201:
                return True
            else:
                return False
        except requests.exceptions.RequestException as e:
            print("paulius_service is down")

        return None

    def update_note(self, title, note):
        try:
            r = requests.put(self.url + f'notes/{title}', data=note)

            return r.status_code
        except requests.exceptions.RequestException as e:
            print("paulius_service is down")

        return None

    def delete_note(self, title):
        try:
            r = requests.delete(self.url + f'notes/{title}')

            if r.status_code == 200:
                return True
            else:
                return False
        except requests.exceptions.RequestException as e:
            print("paulius_service is down")

        return None


