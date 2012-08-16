#encoding=utf-8
import web

from pycms.form.widget import *
from pycms.form.validator import *


admin_login_form = web.form.Form(
    MyTextbox('username', vnotnull, required=True, size=20, description=u"用户名"),
    MyPassword('password', vnotnull, required=True, size=20, description=u"密码"),
)

