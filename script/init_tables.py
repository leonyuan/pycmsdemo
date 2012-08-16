#!/bin/env python
import os.path
import sys

PROJECT_DIR = os.path.abspath(os.path.dirname(__file__))
sys.path.append(os.path.join(PROJECT_DIR,'..'))

from environ import setup_environ
setup_environ()

from pycms.db.util import Base, engine
from pycms.account.model import *
from pycms.category.model import *
from pycms.template.model import *
from pycms.model.model import *


if __name__ == '__main__':
    import sys
    if len(sys.argv) == 1:
        metadata.create_all(engine)
    elif sys.argv[1].lower() == 'drop':
        metadata.drop_all(engine)

