#encoding=utf-8
import web
from pycms.model.db import *
from pycms.category.db import get_category_by_slug, get_category_ancestors
from pycms.utils.paging import Pagination
from front.util import render, info_render, template_exist


class index:
    def GET(self):
        req = web.ctx.req
        req.update({
            'get_latest_entities': get_latest_entities,
            'get_entity': get_entity,
            })

        return render.index(**req)

class reindex:
    def GET(self): raise web.seeother('/')

class entity:
    def GET(self, mname, id):
        base_entity = get_entity(id)
        model = base_entity.model
        entity = getattr(base_entity, model.name)
        category_ancestors = get_entitys_category_ancestors(base_entity)
        req = web.ctx.req
        req.update({
            'base_entity': base_entity,
            'entity': entity,
            model.name: entity,
            'category_ancestors': category_ancestors,
            'get_latest_entities': get_latest_entities,
            })
        template = model.template.display_file
        return info_render.render(template, **req)

class entlist:
    def GET(self, catslug, pgno=1):
        cat = get_category_by_slug(catslug)
        pagination = Pagination(info_record_query2(cat.id), info_count_query2(cat.id), pgno)
        qs = pagination.queryset
        entities = qs.all()

        #import pdb
        #pdb.set_trace()

        category_ancestors = get_category_ancestors(cat)

        req = web.ctx.req
        req.update({
            'entities': entities,
            'category_ancestors': category_ancestors,
            'thecat': cat,
            'pagination': pagination,
            'get_latest_entities': get_latest_entities,
            })

        template = cat.template and cat.template.list_file or None
        if not template or not template_exist(template):
            template = web.config.default_category_list
        return info_render.render(template, **req)

class catindex:
    def GET(self, slug):
        cat = get_category_by_slug(slug)
        req = web.ctx.req
        req.update({
            'thecat': cat,
            'get_latest_entities': get_latest_entities,
            'get_entity': get_entity,
            })
        template = cat.template and cat.template.index_file or None
        #if template:
        #    web.debug("111 cat:%s 's template:%s" % (cat.slug, template))
        if not template or not template_exist(template):
            template = web.config.default_category_index
        #if template:
        #    web.debug("222 cat:%s 's template:%s" % (cat.slug, template))
        return info_render.render(template, **req)

class search:
    def GET(self):
        data = web.input(p=1, q='', type='')
        if data.type == u'news':
            mname = 'news'
            cslug = None
        elif data.type == u'yylt' or data.type == u'yllt':
            mname = 'job'
            cslug = data.type
        elif data.type == u'bqrc' or data.type == u'nqrc':
            mname = 'elite'
            cslug = data.type

        model = get_model_by_name(mname)

        req = web.ctx.req
        pagination = Pagination(search_record_query(model, data.q, cslug) \
                     , search_count_query(model, data.q, cslug), data.p)
        qs = pagination.queryset
        entities = qs.all()

        req.update({
            'entities': entities,
            'model': model,
            'pagination': pagination,
            'q': data.q,
            'type': data.type,
            })

        return render.search_result(**req)

