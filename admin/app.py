import web
from pycms.account import admin as account_admin
from pycms.category import admin as category_admin
from pycms.template import admin as template_admin
from pycms.file import admin as file_admin
from pycms.model import admin as model_admin
from admin import view, upload
from admin.publish.app import app_publish

urls = []
urls.extend(account_admin.urls)
urls.extend(category_admin.urls)
urls.extend(template_admin.urls)
urls.extend(file_admin.urls)
urls.extend(model_admin.urls)

urls.extend((
        '', view.reindex,
        '/', view.index,
        '/login', view.login,
        '/logout', view.logout,
        '/submenu', view.submenu,
        '/curpos', view.curpos,
        '/dashboard', view.dashboard,
        '/upload', upload.upload,
        '/browse', upload.browse,

        '/publish', app_publish,
))
urls = tuple(urls)


app_admin = web.application(urls)
