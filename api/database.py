from api import db
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Column, Integer, String



class NEWS(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True, unique=True)
    title = db.Column(db.String(80))       #标题
    image = db.Column(db.String(200))       #图片地址
    content = db.Column(db.Text)     #内容
    createDate = db.Column(db.Integer)
    __tablename__ = 'news'

# class Users(db.Model):
#     id = db.Column(db.Integer, nullable=False, primary_key=True)
#     name = db.Column(db.String(20), nullable=False)
#
#     def __repr__(self):
#         return '<User %r>' % self.name

new = NEWS(
    title = '如今你的气质里，藏着你曾走过的路、读过的书和爱过的人',
    image = '/image/婧婧怡.jpeg',
    content = 'TextText',
    createDate = 123456
)

db.create_all()

db.session.add(new)
db.session.commit()