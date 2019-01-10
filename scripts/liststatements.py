import os
import sys
import inspect

currentdir = os.path.dirname(os.path.abspath(
    inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0, parentdir)

from app import app, db
from app.models import Statement

if __name__ == "__main__":
    statements = Statement.query.all()
    for s in statements:
        print(str(s.id) + " | " + s.original)
