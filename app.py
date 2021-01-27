from flask import Flask,render_template,request
import sqlite3
app = Flask( __name__ )


# @app.route( '/' )
# def hello_world() :
#     return 'Hello World!'

@app.route( '/',methods=['POST', 'GET'] )
def index() :
    return render_template("index.html")

@app.route( '/index',methods=['POST', 'GET'] )
def index1() :
    return render_template("index.html")

@app.route( '/movie',methods=['POST', 'GET'] )
def movie() :
    datalist = []
    con = sqlite3.connect("movie.db")
    cur = con.cursor()
    sql = "select * from movie250;"
    data = cur.execute(sql)
    for item in data:
        datalist.append(item)
    cur.close()
    con.close()

    return render_template("movie.html",movies=datalist)

@app.route( '/score',methods=['POST', 'GET'] )
def score() :
    score_list=[]
    num = []
    con = sqlite3.connect("movie.db")
    cur = con.cursor()
    sql = "select score,count(score) from movie250 group by score;"
    data = cur.execute(sql)
    for item in data:
        score_list.append(item[0])
        num.append(item[1])
    cur.close()
    con.close()
    return render_template("score.html",score=score_list,num=num)

@app.route( '/word',methods=['POST', 'GET'] )
def word() :
    return render_template("word.html")

@app.route( '/team',methods=['POST', 'GET'] )
def team() :
    return render_template("team.html")


if __name__ == '__main__' :
    app.run()
