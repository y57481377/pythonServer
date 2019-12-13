from api import db
#from flask_sqlalchemy import SQLAlchemy
#from sqlalchemy import Column, Integer, String



class NEWS(db.Model):
    # id = db.Column(db.Integer, primary_key=True, autoincrement=True, unique=True)
    # 文章id
    articleID = db.Column(db.String(40), primary_key=True, unique=True)
    # 标题
    title = db.Column(db.String(80))
    # 作者
    author = db.Column(db.String(20))
    # 图片地址
    image = db.Column(db.String(200))
    # 内容
    excerpt = db.Column(db.String(100))
    # 文章类型
    type = db.Column(db.Integer)
    # 创建时间
    createDate = db.Column(db.Integer)
    __tablename__ = 'news'

    def toJson(self):
        dic = self.__dict__
        if "_sa_instance_state" in dic:
            del dic["_sa_instance_state"]
        return dic

class ARTICLE(db.Model):
    # 文章id
    articleID = db.Column(db.String(40), primary_key=True, unique=True)
    # 内容
    content = db.Column(db.Text)
    __tablename__ = 'article'


    def toJson(self):
        dic = self.__dict__
        if "_sa_instance_state" in dic:
            del dic["_sa_instance_state"]
        return dic


# class Users(db.Model):
#     id = db.Column(db.Integer, nullable=False, primary_key=True)
#     name = db.Column(db.String(20), nullable=False)
#
#     def __repr__(self):
#         return '<User %r>' % self.name


db.create_all()

# db.session.add(new)
# db.session.commit()