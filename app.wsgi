import os.path
import sys

sys.path.insert(0, os.path.abspath(os.path.dirname(__file__)))

from app import app
application = app.wsgifunc()
