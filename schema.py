
from arango import ArangoClient

client = ArangoClient(
    protocol = 'http',
    host = '0.0.0.0',
    port = '8529',
    username = 'root',
    password = 'nosqlba2018',
    enable_logging = True
)

# open sys_db
sys_db = client.db('_system', username='root', password='nosqlba2018')
# if not exists autocoder db create it
if not sys_db.has_database('nosqlba2018'):
    sys_db.create_database(
        name='nosqlba2018',
        users=[
            {'username': 'root', 'password': 'nosqlba2018', 'active': True},
        ],
    )

# delete sys_db var

# open autocoder db
db = client.db('nosqlba2018', username='root', password='nosqlba2018')

collections = [
    'users',
    'blogs',
    'categories',
    'posts',
    'comments',
]

# create collections if not exists
for collection in collections:
    if not db.has_collection(collection):
        db.create_collection(collection)


class User:
    collection = 'users'
    def __init__(self, db):
        self.db = db
    def login(self, username, password):
        pass

class Blog:
    collection = 'categories'
    def __init__(self, db):
        self.db = db
    def all(self):
        pass
    def get(self):
        pass
    def insert(self):
        pass
    def update(self):
        pass
    def arquive(self):
        pass
    def delete(self):
        pass

class Category:
    collection = 'categories'
    def __init__(self, db):
        self.db = db
    def all(self):
        pass
    def get(self):
        pass
    def insert(self):
        pass
    def update(self):
        pass
    def arquive(self):
        pass
    def delete(self):
        pass

class Post:
    collection = 'posts'
    def __init__(self, db):
        self.db = db
    def all(self):
        pass
    def get(self):
        pass
    def insert(self):
        pass
    def update(self):
        pass
    def arquive(self):
        pass
    def delete(self):
        pass


class Comment:
    collection = 'comments'
    def __init__(self, db):
        self.db = db
    def all(self):
        pass
    def get(self):
        pass
    def insert(self):
        pass
    def update(self):
        pass
    def arquive(self):
        pass
    def delete(self):
        pass

