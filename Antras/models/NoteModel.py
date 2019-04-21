class Note:
    def __init__(self, obj):
        self.separationIndex = '*'
        self.title = obj['title']
        self.author = obj['author']
        self.comment = obj['comment']
        self.expiration = obj['expiration']

    def serialize(self):
        return {
            'title': self.title[self.title.index(self.separationIndex)],
            'comment': self.comment,
        }
