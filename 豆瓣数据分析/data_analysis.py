from flask import Flask
from flask import render_template
import pymysql
import re

app = Flask(__name__, static_url_path='/static', static_folder='static', template_folder='templates')


# 404
@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html")


# 首页
@app.route('/')
@app.route('/index')
def index():
    return render_template("index.html")


# 电影
@app.route('/movie')
def movie():
    con = pymysql.connect(host="localhost", user='root', password='root', db='douban')
    cursor = con.cursor()
    sql = 'SELECT  * FROM MOVIE250'
    datalist = []
    cursor.execute(sql)
    data = cursor.fetchall()
    for item in data:
        datalist.append(item)
    cursor.close()
    con.close()
    return render_template("movie.html", datalist=datalist)


# 评分
@app.route('/score')
def score():
    con = pymysql.connect(host="localhost", user='root', password='root', db='douban')
    cursor = con.cursor()
    sql = 'SELECT  score,count(score) FROM MOVIE250 group by score'
    cursor.execute(sql)
    data = cursor.fetchall()
    score_list = []
    num_list = []
    for item in data:
        score_list.append(item[0])
        num_list.append(item[1])
    return render_template("score.html", score_list=score_list, num_list=num_list)


# 词云
@app.route('/word')
def word():
    return render_template("word.html")


# 团队
@app.route('/team')
def team():
    return render_template("team.html")
