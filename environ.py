import os.path
import sys

import config

PROJECT_DIR = os.path.abspath(os.path.dirname(__file__))

def setup_environ():
    sys.path.append(os.path.join(PROJECT_DIR,'lib'))
    from pycms.utils.environ import setup_config
    setup_config(config)
    reload(sys)
    sys.setdefaultencoding('utf-8')

