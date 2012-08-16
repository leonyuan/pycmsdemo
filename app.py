#!/bin/env python
'''
This file is main application file. It includes some things, database and session and hook, etc.
A significant hook is defined,  The hook defines some http request scope object to used in template files.
'''

from environ import setup_environ
setup_environ()

import web
from pycms.db.util import load_sqla, dbstore
from pycms.utils.storage import context
from pycms.utils.text import yesorno
from pycms.account.app import app_account
from pycms.account.util import LazyUser
from pycms.model.util import init_model_class
from admin.app import app_admin
from front import view


#web.config.debug = debug

urls = (
    '', view.reindex,
    '/', view.index,
    '/search', view.search,
    '/account', app_account,
    '/admin', app_admin,

    '/(.+)/list', view.entlist,
    '/(.+)/list/(\d+)', view.entlist,
    '/(.+)/(\d+)', view.entity,
    #'/(.+)', view.catindex,
)

app = web.application(urls)

if web.config.get('_session') is None:
    session = web.session.Session(app, dbstore, initializer={'_userid': -1})
    web.config._session = session
else:
    session = web.config._session

def session_hook():
    web.ctx.session = session

def request_hook():
    req = context()
    req['homedomain'] = web.ctx.homedomain
    req['static_url'] = callable(web.config.static_url) and web.config.static_url() or web.config.static_url
    req['admin_url'] = web.ctx.homepath + '/admin'
    req['_userid'] = web.ctx.session._userid
    req['_s'] = web.net.websafe
    req['_yn'] = yesorno
    req['_uq'] = web.net.urlquote
    action = web.ctx.path.split('/')[-1]
    if action.find('_'):
        action = action.split('_')[-1]
    req['_ac'] = action
    web.ctx.__class__.user = LazyUser()
    req['_user'] = web.ctx.user
    web.ctx.req = req

app.add_processor(load_sqla)
app.add_processor(web.loadhook(session_hook))
app.add_processor(web.loadhook(request_hook))

# some system initiate activities
init_model_class()

if __name__ == '__main__':
    app.run()

