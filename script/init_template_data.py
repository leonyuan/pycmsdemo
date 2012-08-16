#encoding=utf-8
from pycms.template.model import Template
from pycms.db.util import DBSession


def init():
    session = DBSession()

    t1 = Template(name=u'新闻模板', index_file='category_index.html',\
            list_file='news_list.html', display_file='news_display.html')

    t2 = Template(name=u'职位模板', index_file='lietou_index.html',\
            list_file='job_list.html', display_file='job_display.html')

    session.add(t1)
    session.add(t2)
    session.commit()

if __name__ == '__main__':
    init()
