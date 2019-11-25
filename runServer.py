
from api import app, api

YHHServerIP = '0.0.0.0'
YHHServerPost = 5000

if __name__ == '__main__':
    app.run(YHHServerIP, YHHServerPost)