import os.path
import web
from web import config as cfg
from pycms.utils.render import render_mako


render = render_mako(
            directories=[cfg.site_template_dir],
            input_encoding='utf-8',
            output_encoding='utf-8',
         )

info_render = render_mako(
            directories=[os.path.join(cfg.site_template_dir, 'info_template'), cfg.site_template_dir],
            input_encoding='utf-8',
            output_encoding='utf-8',
         )

def template_exist(template_filename):
    template_dir = os.path.join(cfg.site_template_dir, 'info_template')
    #web.debug("template_exist: template_dir:%s" % (template_dir,))
    return os.path.exists(os.path.join(template_dir, template_filename))
