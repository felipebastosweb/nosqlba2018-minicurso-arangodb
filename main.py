
from weppy import App, request, abort, redirect, session
from weppy.tools import service
from weppy.sessions import SessionFSManager

app = App(__name__)
app.pipeline = [SessionFSManager()]

# Load database connection
from services import *

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)
