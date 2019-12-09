from api import apis, db
from api.database import NEWS
from flask import send_from_directory
from flask_restful import Resource, reqparse, abort
import os

class News(Resource):
    def get(self):
        parse = reqparse.RequestParser()
        parse.add_argument("page", type=int, help="be  int", required=True)
        page = parse.parse_args().get("page")
        news = NEWS.query.all()

        news_j = []
        for new in news:
            news_j.append(new.toJson())
        return news_j



imageDir = os.path.dirname(__file__) + '/image'
#   获取图片链接
class Image(Resource):
    def get(self, imageName):
        imagePath = os.path.join(imageDir, imageName)
        if os.path.isfile(imagePath):
            print(imagePath)
            return send_from_directory(imageDir, imageName, as_attachment=False)
        return 500

# user_pareser = reqparse.RequestParser()
# user_pareser.add_argument("username", str)
# user_pareser.add_argument("id", str)

report_parser = reqparse.RequestParser()
report_parser.add_argument("type", type=int)
report_parser.add_argument("msg", type=str)
report_parser.add_argument("user", type=dict)

#   举报反馈接口
class Report(Resource):
    def post(self):
        args = report_parser.parse_args()
        return args, 201



def abort_if_todo_doesnt_exist(t_id):
    if t_id not in Loves:
        abort(404, message="Todo {} doesn't exist".format(t_id))

apis.add_resource(News, '/api/news')
apis.add_resource(Image, '/image/<imageName>')
apis.add_resource(Report, '/api/report')
