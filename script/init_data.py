#!/bin/env python
import os.path
import sys

PROJECT_DIR = os.path.abspath(os.path.dirname(__file__))
sys.path.append(os.path.join(PROJECT_DIR,'..'))

from environ import setup_environ
setup_environ()

import init_perm_data, init_user_data, init_template_data, init_category_data, init_model_data


if __name__ == '__main__':
    init_perm_data.init()
    init_user_data.init()
    init_template_data.init()
    init_model_data.init()
    init_category_data.init()
