from flask import Flask
from flask_restful import Api
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
apis = Api(app)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///timeServer.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)