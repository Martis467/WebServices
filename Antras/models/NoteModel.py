class Note:
    def __init__(self, obj):
        self.separationIndex = '*'
        self.title = obj['title']
        self.author = obj['author']
        self.comment = obj['comment']
        self.expiration = obj['expiration']

    def serialize(self):
        index = 0

        try:
            index = self.title.index(self.separationIndex)
        except ValueError as e:
            index = len(self.title)

        return {
            'title': self.title[0:index],
            'comment': self.comment,
        }
