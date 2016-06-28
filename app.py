from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask import render_template, url_for,request
from flask_sqlalchemy import SQLAlchemy
import time
from flask.ext.paginate import Pagination

app = Flask(__name__, instance_relative_config=True)
app.config.from_object('config')

app.config.from_pyfile('localConfig.py')
db = SQLAlchemy(app)


class users(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    department = db.Column(db.String)
    team = db.Column(db.String)

    def __init__(self, id, name, department, team):
        self.id = id
        self.name = name
        self.department = department
        self.team = team


class posts(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String)
    body = db.Column(db.String)
    authorId = db.Column(db.Integer)
    date = db.Column(db.String)
    status = db.Column(db.String)

    def __init__(self, id, title, body, authorId, date, status):
        self.id = id
        self.title = title
        self.body = body
        self.authorId = authorId
        self.date = date
        self.status = status


@app.route('/')
def hello_world():
	#page
    search = False
    q = request.args.get('q')
    if q:
        search = True
    try:
        page = int(request.args.get('page', 1))
    except ValueError:
        page = 1

    

    post = {}
    for item in posts.query.all():
        if post.has_key(item.date):
            user_info = users.query.filter_by(id=item.authorId).first()
            user_name = user_info.name
            post[item.date].append(
                {'id': item.id, 'body': item.body, 'title': item.title, 'authorId': item.authorId, 'user_name': user_name})
        else:
            post[item.date] = []
        pagination = Pagination(page=page, total=len(post),per_page=2
                            search=search, record_name='users')
    return render_template('index.html', post=post,pagination=pagination)


@app.route('/user/<authorId>')
def userPage(authorId):
    post = posts.query.filter_by(authorId=authorId).all()
    user_info = users.query.filter_by(id=authorId).first()
    return render_template('user.html', post=post, user_info=user_info)


@app.route('/date/<date>')
def datePage(date):
    post = posts.query.filter_by(date=date).all()
    return render_template('date.html', post=post)


@app.route('/post/<postId>')
def postPage(postId):
    post = posts.query.filter_by(id=postId).first()
    return render_template('post.html', post=post)


if __name__ == '__main__':
    app.run()
