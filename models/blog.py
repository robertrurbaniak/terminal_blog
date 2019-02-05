import uuid

class Blog(object)
    def __init__(self, author, title, description, id=None):
        self.auther = author
        self.title = title
        self.description = description
        self.id = uuid.uuid4().hex if id is None else id

    def new_post(self):
        pass

    def get_post(self)
        :