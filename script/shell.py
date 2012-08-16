#!/bin/env python
import os.path
import sys

PROJECT_DIR = os.path.abspath(os.path.dirname(__file__))
sys.path.append(os.path.join(PROJECT_DIR,'..'))

from environ import setup_environ
setup_environ()

from pycms.db.util import Base, engine, DBSession
from pycms.account.model import *
from pycms.category.model import *
from pycms.template.model import *
from pycms.model.model import *
from pycms.model.util import build_model
from pycms.utils.paging import Pagination


session = DBSession()

models = session.query(Model).filter_by(is_active=True).all()
for model in models:
    build_model(model, True)

def get_entities(cid=None, limit=None):
    if cid is None:
        return session.query(Entity).order_by(Entity.id.desc()).all()
    else:
        if limit is None:
            return session.query(Entity).filter(Entity.categories.any(id=cid)) \
                    .order_by(Entity.id.desc()).all()
        else:
            return session.query(Entity).filter(Entity.categories.any(id=cid)) \
                    .order_by(Entity.id.desc()).limit(limit).all()

def info_record_query(cid):
    search_query = session.query(Entity).filter(Entity.categories.any(id=cid)).order_by(Entity.id.desc())
    return search_query

def info_count_query(cid):
    search_query = session.query(Entity.id).filter(Entity.categories.any(id=cid)).order_by(Entity.id.desc())
    return search_query

cat = session.query(Category).filter_by(slug='yyhnqzw').first()
pagination = Pagination(info_record_query(cat.id), info_count_query(cat.id), 1)
qs = pagination.queryset
entities = qs.all()


import code
code.interact(local=locals())
