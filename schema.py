
from arango import ArangoClient

client = ArangoClient(
    protocol = 'http',
    host = '0.0.0.0',
    port = '8529',
    username = 'root',
    password = 'nosqlba2018',
    enable_logging = True
)

db = client.database('nosqlba2018')
