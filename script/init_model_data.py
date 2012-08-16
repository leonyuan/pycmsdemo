#encoding=utf-8
from pycms.template.model import Template
from pycms.model.model import Model, Field, Relation
from pycms.db.util import DBSession


def init():
    session = DBSession()

    t1 = session.query(Template).filter_by(name=u'新闻模板').first()
    t2 = session.query(Template).filter_by(name=u'职位模板').first()

    job = Model(name='job', title=u'职位')
    job.template = t2

    indtype = Field(name='indtype', title=u'行业类别', type='select', length=16, required=True, props="{'options': [u'\u533b\u836f\u8bbe\u5907/\u5668\u68b0', u'\u4fdd\u5065/\u98df\u54c1', u'\u5236\u836f/\u751f\u7269\u5de5\u7a0b', u'\u533b\u7597/\u533b\u9662\u7ba1\u7406', u'\u5176\u4ed6'], 'is_multisel': False}")
    companykind = Field(name='companykind', title=u'公司性质', type='select', length=16, required=True, props="{'options': [u'\u72ec\u8d44(\u6b27\u7f8e)', u'\u72ec\u8d44(\u975e\u6b27\u7f8e)', u'\u5408\u8d44\u4f01\u4e1a', u'\u96c6\u56e2\u4e0a\u5e02\u516c\u53f8', u'\u4e0a\u5e02\u516c\u53f8', u'\u6c11\u8425\u4e0a\u5e02\u516c\u53f8', u'\u6c11\u8425\u4f01\u4e1a', u'\u56fd\u8425\u4f01\u4e1a', u'\u533b\u9662', u'\u5176\u4ed6'], 'is_multisel': False}")
    location = Field(name='location', title=u'工作地点', required=False, type='string', length=16)
    endate = Field(name='endate', title=u'截止日期', required=False, type='string', length=16)
    payment = Field(name='payment', title=u'薪资待遇', required=False, type='string', length=16)
    acount = Field(name='acount', title=u'招聘人数', required=False, type='string', length=8)
    responsibility = Field(name='responsibility', title=u'岗位职责', type='text', required=True, props="{'lines': u'5', 'editor': u'feature'}")
    qualification = Field(name='qualification', title=u'任职要求', type='text', required=True, props="{'lines': u'5', 'editor': u'feature'}")

    session.add(indtype)
    session.add(companykind)
    session.add(location)
    session.add(endate)
    session.add(payment)
    session.add(acount)
    session.add(responsibility)
    session.add(qualification)

    #job.fields.append(title)
    job.fields.append(indtype)
    job.fields.append(companykind)
    job.fields.append(location)
    job.fields.append(endate)
    job.fields.append(payment)
    job.fields.append(acount)
    job.fields.append(responsibility)
    job.fields.append(qualification)

    #r1 = Relation(name='user', title=u'创建者', type='many-to-one', target='User', backref='jobs')
    #r2 = Relation(name='categories', title=u'栏目', type='many-to-many', target='Category', backref='jobs')

    #session.add(r1)
    #session.add(r2)

    #job.relations.append(r1)
    #job.relations.append(r2)

    session.add(job)


    news = Model(name='news', title=u'新闻')
    news.template = t1

    #title = Field(name='title', title=u'标题', type='string', length=32, required=True)
    keywords = Field(name='keywords', title=u'关键词', type='string', length=64)
    summary = Field(name='summary', title=u'摘要', type='string', length=255)
    content2 = Field(name='content', title=u'内容', type='text')

    #session.add(title)
    session.add(keywords)
    session.add(summary)
    session.add(content2)

    #news.fields.append(title)
    news.fields.append(keywords)
    news.fields.append(summary)
    news.fields.append(content2)

    #r3 = Relation(name='user', title=u'创建者', type='many-to-one', target='User', backref='news')
    #r4 = Relation(name='categories', title=u'栏目', type='many-to-many', target='Category', backref='news')

    #session.add(r3)
    #session.add(r4)

    #news.relations.append(r3)
    #news.relations.append(r4)

    session.add(news)

    session.commit()

if __name__ == '__main__':
    init()
