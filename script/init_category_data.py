#encoding=utf-8
from pycms.category.model import Category
from pycms.model.model import Model
from pycms.db.util import DBSession
from pycms.template.model import Template


def init():
    session = DBSession()

    t1 = session.query(Template).filter_by(name=u'新闻模板').first()
    t2 = session.query(Template).filter_by(name=u'职位模板').first()


    c1 = Category(name=u'新闻', slug='news')
    c1.template = t1

    c2 = Category(name=u'国内新闻', slug='natnews')
    c2.parent = c1
    c2.template = t1

    c3 = Category(name=u'猎头职位', slug='medicine_jobs')
    c3.template = t2

    session.add(c1)
    session.add(c2)
    session.add(c3)
    session.commit()

if __name__ == '__main__':
    init()
