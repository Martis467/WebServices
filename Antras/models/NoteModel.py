class Note:
    def __init__(self, obj):
        self.title = obj['title']
        self.author = obj['author']
        self.comment = obj['comment']
        self.expiration = obj['expiration']

    def serialize(self):
        return {
            'title': self.title,
            'comment': self.comment,
            'expiration': self.expiration
        }
