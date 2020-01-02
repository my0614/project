from flask import Flask, request, render_template
import pymysql

db = pymysql.connect(host='localhost',
port=3306, user='root',passwd = '1234',
db='work',  charset='utf8'
)

cursor = db.cursor()

app = Flask(__name__)

@app.route('/')
def run():
    return 'hello world'


@app.route('/start')
def start():
    return render_template('login.html')


@app.route('/join')
def join():
    return render_template('join.html')


@app.route('/home', methods=['POST'])
def home():
    id = request.form['myid']
    pw = request.form['mypw']
    name = request.form['myname']
    sql = "insert into work.info values('%s','%s','%s');" %(id,pw,name)
    cursor.execute(sql)
    #db 실행하기
    db.commit()
    return '성공'


@app.route('/login', methods=['POST'])
def login():
    id = request.form['myid']
    pw = request.form['mypw']
    sql = "select *  from work.info where id= '%s';" % id
    if cursor.execute(sql) == 0:
        return '아이디가 존재하지 않습니다.'
    else:
        result = cursor.fetchone()
        if pw == result[1]:
            return render_template('todo.html')
        else:
            return '죄송합니다. 비밀번호가 알맞지 않습니다.'



if __name__== '__main__':
    app.run(debug=True, port="4999")
    db.close()
