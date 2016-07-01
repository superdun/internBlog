from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask import render_template, url_for, request
import time
from flask.ext.paginate import Pagination
from sqlalchemy import desc

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
    tmstmp = db.Column(db.Integer)

    def __init__(self, id, title, body, authorId, date, status):
        self.id = id
        self.title = title
        self.body = body
        self.authorId = authorId
        self.date = date
        self.status = status


def pageControl(query):
    per_page = app.config["POST_PER_PAGE"]
    search = False
    total = len(query.all())
    q = request.args.get('q')
    if q:
        search = True
    try:
        page = int(request.args.get('page', 1))
    except ValueError:
        page = 1

    return [query.paginate(page, per_page, False).items, Pagination(page=page, total=total, bs_version=3,
                                                                    search=search, per_page=per_page)]


def make_post_by_date(Filter):
    post = []
    date_list = ['']
    # post=>[{},{},{}......]
    items, pagination = pageControl(
        Filter.order_by(desc(posts.tmstmp)))
    for item in items:
        if date_list[-1] != item.date:
            date_list.append(item.date)
            date = item.date
        else:
            date = ''
        user_info = users.query.filter_by(id=item.authorId).first()
        user_name = user_info.name
        user_department = user_info.department
        user_team = user_info.team
        # if date is new,date=the date.or date=''
        post.append({'date': date, 'id': item.id, 'body': item.body, 'title': item.title,
                     'authorId': item.authorId, 'user_name': user_name, 'user_department': user_department, 'user_team': user_team})
    return [post, pagination]


@app.route('/')
def index(page=1):
    post, pagination = make_post_by_date(posts.query.filter_by())
    return render_template('index.html', nav_status=1, post=post, pagination=pagination)


@app.route('/user/<authorId>')
def userPage(authorId):

    post, pagination = make_post_by_date(
        posts.query.filter_by(authorId=authorId))

    return render_template('user.html', post=post, nav_status=1, pagination=pagination)


@app.route('/date/<date>')
def datePage(date):
    items, pagination = pageControl(posts.query.filter_by(date=date).order_by(
        desc(posts.tmstmp)))
    post = items
    user_list = []
    for i in range(len(post)):
        user_info = users.query.filter_by(id=post[i].authorId).first()
        user_list.append(user_info.name)
    return render_template('date.html', post=post, user_list=user_list, pagination=pagination)


@app.route('/post/<postId>')
def postPage(postId):
    post = posts.query.filter_by(id=postId).first()
    user_info = users.query.filter_by(id=post.authorId).first()
    user_name = user_info.name
    return render_template('post.html', post=post, user_name=user_name)


if __name__ == '__main__':
    # app.run()
    app.run(host='0.0.0.0',port=8080)
