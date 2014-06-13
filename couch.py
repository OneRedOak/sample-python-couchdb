import couchdbkit as couchdb
from couchdbkit import Server
from couchdbkit import Database

class Couch():
    def __init__(self):
        self.server = Server()
        self.server.delete_db('test')
        self.db = self.server.get_or_create_db('test')

    def populate(self):
        things = [
            {"name": "Vishnu"},
            {"name": "Lakshmi"},
            {"name": "Ganesha"},
            {"name": "Krishna"},
            {"name": "Murugan"}
        ]
        self.db.save_docs(things)

    def count(self):
        print self.db.all_docs().count()
        return self.db.all_docs().count()

if __name__ == "__main__":
    couch = Couch()
    couch.populate()
    print(couch.count())
