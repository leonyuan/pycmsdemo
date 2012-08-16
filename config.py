from os.path import abspath, dirname, join
import web


curdir = abspath(dirname(__file__))

# debug option
debug = False
dev_debug = False

# database settings
db_engine = 'mysql'
db_name = 'iyclt'
db_user = 'dev'
db_password = '1234'
db_host = 'localhost'

# template directory
template_dir = join(curdir, 'templates/')

# template directory
admin_template_dir = join(template_dir, 'admin/')

site_template_dir = join(template_dir, 'site/')

# session settings
session_tablename = 'session'

# default new user's password
default_password = 'pycms'

#publish html directory
publish_dir = join(curdir, 'static/html/')

homedomain = 'http://localhost:8080'

#static url
static_url = lambda: web.ctx.homedomain + '/static'

#default pagination record number
default_page_size = 30

#default front list page pagination record number
default_front_list_page_size = 15

#default category index html filename
default_category_index = 'category_index.html'

#default category list html filename
default_category_list = 'category_list.html'

upload_dir = join(curdir, 'static/upload/')

upload_url = homedomain + '/admin/upload'
browse_url = homedomain + '/admin/browse'

upload_media_url_prefix = homedomain + '/static/upload/'


try:
    from local_config import *
except ImportError:
    pass
