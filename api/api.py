from api import apis, database
from flask import Flask, request, send_from_directory
from flask_restful import Resource, reqparse, abort
import os

todos = {}

parser = reqparse.RequestParser()
parser.add_argument('name', type=str)
parser.add_argument('time', type=str)
parser.add_argument('what', type=str)


Loves = {
    'love1': {'what': 'your shining eyes'},
    'love2': {'what': 'your sweet voice'},
    'love3': {'waht': 'your charming smile'},
    'love4': {'waht': 'everything about you'},

}

class TodoSimple(Resource):
    def get(self, todo_id):
        return {todo_id: todos[todo_id]}

    def put(self, todo_id):
        todos[todo_id] = request.form['data']
        return {todo_id: todos[todo_id]}

class PostSimple(Resource):
    def get(self, love_id):
        abort_if_todo_doesnt_exist(love_id)
        return Loves[love_id]

    def delete(self, love_id):
        abort_if_todo_doesnt_exist(love_id)
        del Loves[love_id]
        return 'delete success', 204

    def post(self, love_id):
        abort_if_todo_doesnt_exist(love_id)
        # args = parser.parse_args()
        # love_id = int(max(Tasks.keys()).lstrip('love')) + 1
        # love_id = 'love%i' % love_id
        # Tasks[love_id] = {'what': args['what']}
        # print(args)
        return Loves, 201
    def put(self, love_id):
        args = parser.parse_args()
        what= {'what': args['what']}
        Loves[love_id] = what
        return Loves, 201

imageDir = os.path.dirname(__file__) + '/image'
#  获取图片链接
class Image(Resource):
    def get(self, imageName):
        imagePath = os.path.join(imageDir, imageName)
        if os.path.isfile(imagePath):
            print(imagePath)
            return send_from_directory(imageDir, imageName, as_attachment=True)
        return
print()

def abort_if_todo_doesnt_exist(t_id):
    if t_id not in Loves:
        abort(404, message="Todo {} doesn't exist".format(t_id))

apis.add_resource(TodoSimple, '/<string:todo_id>')
apis.add_resource(PostSimple, '/love/<love_id>')
apis.add_resource(Image, '/image/<imageName>')
