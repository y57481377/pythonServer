from api import apis, db
from api.database import NEWS
from flask import Flask, request, send_from_directory
from flask_restful import Resource, reqparse, abort
import os


class News_api(Resource):
    def get(self, page):
        news = db.session.query(NEWS).all()
        # news = NEWS.query_filter()
        return



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
        News_api().get(page=0);
        args = report_parser.parse_args()
        return args, 201



def abort_if_todo_doesnt_exist(t_id):
    if t_id not in Loves:
        abort(404, message="Todo {} doesn't exist".format(t_id))


apis.add_resource(Image, '/image/<imageName>')
apis.add_resource(Report, '/api/report')
