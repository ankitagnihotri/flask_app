# @Author: ankit
# @Date:   2019-03-25T16:38:52+05:30
# @Email:  ankit@minance.com
# @Last modified by:   ankit
# @Last modified time: 2019-03-25T16:59:40+05:30
# @Copyright: Minance Technologies Private Limited

from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'

if __name__ == '__main__':
    app.run()
