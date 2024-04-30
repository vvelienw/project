from flask import Flask, render_template, url_for, request, redirect
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

from sqlalchemy.orm import DeclarativeBase


class Base(DeclarativeBase):
    pass


db = SQLAlchemy(model_class=Base)

main = Flask(__name__)
main.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///blog.db'
main.config['SCLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(main)


class Article(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String(100), nullable=False)
    intro = db.Column(db.String(300), nullable=False)
    text = db.Column(db.Text, nullable=False)
    date = db.Column(db.DateTime, default=datetime.now())

    def __repr__(self):
        return '<Article %r>' % self.id


@main.route('/')
@main.route('/home')
def index():
    return render_template("index.html")


@main.route('/about')
def about():
    return render_template("about.html")

@main.route('/posts')
def posts():
    articles = Article.query.all()
    return render_template('posts.html', articles=articles)


@main.route('/posts/<int:id>')
def post_detail(id):
    article = Article.query.get(id)
    return render_template('post_detail.html', article=article)


@main.route('/posts/<int:id>/del')
def post_delete(id):
    article = Article.query.get_or_404(id)

    try:
        db.session.delete(article)
        db.session.commit()
        return redirect('/posts')
    except:
        return "При удалении статьи произошла ошибка"


@main.route('/posts/<int:id>/del', methods=['POST', 'GET'])
def post_update(id):
    article = Article.query.get(id)
    if request.method == "POST":
        article.title = request.form['title']
        article.intro = request.form['intro']
        article.text = request.form['text']

        try:
            db.session.commit()
            return redirect('/posts')


@main.route('/posts'):
    def posts():
        articles = Article.query.all()
        return render_template('posts.html', articles=articles)


@main.route('/posts/<int:id>')
    def post_detail(id):
        article = Article.query.get(id)
        return render_template('post_detail.html', article=article)


@main.route('/posts/<int:id>/del')
    def post_delete(id):
        article = Article.query.get_or_404(id)

        try:
            db.session.delete(article)
            db.session.commit()
            return redirect('/posts')
        except:
            return "При удалении статьи произошла ошибка"


@main.route('/posts/<int:id>/del', methods=['POST', 'GET'])
    def post_update(id):
        article = Article.query.get(id)
        if request.method == "POST":
            article.title = request.form['title']
            article.intro = request.form['intro']
            article.text = request.form['text']

            try:
                db.session.commit()
                return redirect('/posts')