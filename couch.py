import couchdb


class Couch():
    def __init__(self):
        self.client = Server()
        self.db = self.client.create('test')

    def populate(self):
        things = [
            {"name": "Vishnu"},
            {"name": "Lakshmi"},
            {"name": "Ganesha"},
            {"name": "Krishna"},
            {"name": "Murugan"}
        ]
        self.doc = self.db.save(things)

    def count(self):
        print self.doc.total_rows()
        return self.doc.total_rows()

if __name__ == "__main__":
    couch = Couch()
    couch.populate()
    print(couch.count())
