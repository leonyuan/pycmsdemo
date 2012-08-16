#encoding=utf-8
import os
import os.path
import web
from web import config as cfg
from pycms.utils.admin import admin_login_required
from pycms.model.db import get_entities, get_entity, get_entitys_category_ancestors \
    ,info_record_query2, info_count_query2
from pycms.category.db import get_categories
from admin.publish.util import admin_render
from front.view import index as site_index, entity as site_entity, entlist as site_entlist, catindex as site_catindex
from admin.util import slug2url
from front.util import info_render


class index:
    @admin_login_required
    def GET(self):
        req = web.ctx.req
        return admin_render.publish_index(**req)

def writefile(path, content):
    try:
        f = open(path, 'w')
        try:
            f.write(content)
        finally:
            f.close()
    except IOError, ioe:
        web.debug('====IOError:%s' % ioe)

class homepage:
    @admin_login_required
    def GET(self):
        site_index_obj = site_index()
        html = site_index_obj.GET()
        if not os.path.exists(cfg.publish_dir):
            os.makedirs(os.path.abspath(cfg.publish_dir))

        path = os.path.join(cfg.publish_dir, 'index.html')
        writefile(path, html)

        raise web.seeother('/index')

def pub_entity_with_template(entity, template):
    model = entity.model
    info = getattr(entity, model.name)
    category_ancestors = get_entitys_category_ancestors(entity)
    req = web.ctx.req
    req.update({
        'base_entity': entity,
        'entity': info,
        model.name: info,
        'category_ancestors': category_ancestors,
        })
    return info_render.render(template, **req)


class entities:
    @admin_login_required
    def GET(self):
        base_entities = get_entities()

        pub_method_obj = site_entity()
        for base_entity in base_entities:
            html = pub_method_obj.GET('', base_entity.id)
            # publish html with yyyy/mm/dd/filename.html
            crtime = base_entity.created_time
            model_dir = os.path.join(cfg.publish_dir, base_entity.model.name)
            dir_path = reduce(os.path.join, [str(crtime.year), str(crtime.month), str(crtime.day)])
            dir_path = os.path.join(model_dir, dir_path)
            if not os.path.exists(dir_path):
                os.makedirs(os.path.abspath(dir_path))
            file_path = os.path.join(dir_path, '%d.html' % base_entity.id)
            writefile(file_path, html)
            if base_entity.slug:
                cats = base_entity.categories
                for cat in cats:
                    if cat.template and cat.template.display_file:
                        cat_dir = os.path.join(cfg.publish_dir, cat.slug)
                        if not os.path.exists(cat_dir):
                            os.makedirs(os.path.abspath(cat_dir))
                        html = pub_entity_with_template(base_entity, cat.template.display_file)
                        path = os.path.join(cat_dir, '%s.html' % slug2url(base_entity.slug))
                        writefile(path, html)

        raise web.seeother('/index')

class entlist:
    @admin_login_required
    def GET(self):
        cats = get_categories()
        pub_method_obj = site_entlist()
        for cat in cats:
            recnum = info_count_query2(cat.id).count()
            psize = web.config.default_page_size
            pnum = recnum / psize + (recnum % psize > 0 and 1 or 0)

            path = os.path.join(cfg.publish_dir, cat.slug)
            if not os.path.exists(path):
                os.makedirs(os.path.abspath(path))

            for i in range(1, pnum+1):
                html = pub_method_obj.GET(cat.slug, i)
                file_path = os.path.join(path, 'list_%d.html' % i)
                writefile(file_path, html)

        raise web.seeother('/index')

class catindex:
    @admin_login_required
    def GET(self):
        cats = get_categories()
        pub_method = site_catindex()
        for cat in cats:
            html = pub_method.GET(cat.slug)
            path = os.path.join(cfg.publish_dir, cat.slug)
            if not os.path.exists(path):
                os.makedirs(os.path.abspath(path))
            path = os.path.join(path, 'index.html')
            writefile(path, html)

        raise web.seeother('/index')
