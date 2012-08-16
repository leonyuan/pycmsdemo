import web
from admin.publish import view

urls = (
        '/index', view.index,
        '/homepage', view.homepage,
        '/entities', view.entities,
        '/entlist', view.entlist,
        '/catindex', view.catindex,
)

app_publish = web.application(urls)
