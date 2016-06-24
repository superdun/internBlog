from flask import Flask
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__, instance_relative_config=True)
app.config.from_object('config')

app.config.from_pyfile('localConfig.py')
print app.config['MYSQL_DATABASE_USER']
db = SQLAlchemy(app)

@app.route('/')
def hello_world():
    return 'index'


@app.route('/user/<username>')
def userPage(username):
    return 'page of %s' % username


@app.route('/date/<datetime>')
def datePage(datetime):
    return 'page of %d ' % datetime


@app.route('/post/<postname>')
def postPage(postname):
    return 'page of %s' % postname

if __name__ == '__main__':
    app.run()
