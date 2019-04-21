

class UserNotes:
    def __init__(self, user, notes):
        self.user = user
        self.notes = notes

    def serialize(self):
        user_with_notes = {'user': self.user.serialize()}
        user_with_notes.update({'notes': self.serialize_notes()})
        return user_with_notes

    def serialize_notes(self):
        note_list = []

        for note in self.notes:
            note_list.append(note.serialize())

        return note_list
