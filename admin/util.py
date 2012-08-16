import os.path
import web
from pycms.utils.render import render_mako


admin_render = render_mako(
            directories=[web.config.admin_template_dir],
            input_encoding='utf-8',
            output_encoding='utf-8',
         )

def slug2url(slug):
    return '-'.join([s.lower() for s in slug.split()])
