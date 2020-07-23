from time import datetime
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
    'accounts',
    'blogs',
    'categories',
    'posts',
    'comments',
]

# create collections if not exists
for collection in collections:
    if not db.has_collection(collection):
        db.create_collection(collection)


class Account:
    collection = 'accounts'
    def __init__(self, db):
        self.db = db
    def find(self, username):
        return db.collection(self.collection).get({'username': username})
    # User Sign In
    def login(self, username, password):
        account = self.find(username)
        if not account:
            return False
        return account.password == password
    # User Logout
    def logout(self, doc):
        if not db.collection(self.collection).has(doc):
            return False
        account = db.collection(self.collection).get({'_key': _key})
    # Insert User
    def signup(self, _username, _password, _email):
        if db.collection(self.collection).get({'username': _username}):
            return False
        doc = dict(username = _username, password = _password, email = _email, created_at = datetime.now().isoformat())
        return db.collection(self.collection).insert(doc)
    # Update User
    def update(self, doc, **kwargs):
        password = kwargs.get('password')
        doc['password'] = password if password
        doc['email'] = email if email
        doc['updated_at'] = datetime.now().isoformat()
        return db.update_document(doc)
    # Arquive User
    def arquive(self, doc):
        password = kwargs.get('password')
        doc['arquived'] = True
        doc['arquived_at'] = datetime.now().isoformat()
        return db.update_document(doc)
    # Delete User
    def delete(self, doc):
        if not db.collection(self.collection).has(doc):
            return False
       return db.delete_document(doc)


class Event:
    collection = 'events'
    def __init__(self, db):
        self.db = db
    # Find Events
    def find(self, title):
        query = """
        FOR doc in events
            FILTER doc.title LIKE %@title%
                OR doc.description LIKE %@title%
            return doc
        """
        cursor = db.aql.execute(query, bind_vars={'title': title})
        docs = [doc for doc in cursor.batch()]
        return docs
    # Insert Event
    def insert(self, _author, _title, _description):
        if db.collection(self.collection).get({'author': author, 'title': title}):
            return False
        doc = dict(author = _author, title = _title, description = _description, created_at = datetime.now().isoformat())
        return db.collection(self.collection).insert(doc)
    # Update Event
    def update(self, doc, **kwargs):
        doc['author'] = kwargs.get('author') if kwargs.get('author')
        doc['title'] = kwargs.get('title') if kwargs.get('title')
        doc['description'] = kwargs.get('description') if kwargs.get('description')
        doc['updated_at'] = datetime.now().isoformat()
        return db.update_document(doc)
    # Arquive User
    def arquive(self, doc):
        password = kwargs.get('password')
        doc['arquived'] = True
        doc['arquived_at'] = datetime.now().isoformat()
        return db.update_document(doc)
    # Delete User
    def delete(self, doc):
        if not db.collection(self.collection).has(doc):
            return False
       return db.delete_document(doc)


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

