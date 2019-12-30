from flask import Flask , request, render_template
import pymysql

#데이터베이스 연결
db = pymysql.connect(host='localhost',
port =3306, user='root', passwd = '1234',
db = 'work', charset='utf8')

cursor = db.cursor()
# sql = "insert into work.hello values('min1',510,'sdlj');"
# cursor.execute(sql)
# db.commit()


app = Flask(__name__)

@app.route('/')
def hello():
    return 'hello'

@app.route('/test')
def test():
    return render_template('main.html')

@app.route('/join')
def join():
    return render_template('join.html')

@app.route('/register', methods=['POST'])
def register():
    id = request.form['id']
    pw = request.form['pw']
    name = request.form['name']
    sql = "insert into work.userdata values('%s' ,'%s', '%s',0);" %(id,pw,name)
    cursor.execute(sql)
    db.commit()
    return '완료'

@app.route('/login', methods=['POST'])
def post():
    id = request.form['id']
    pw = request.form['pw']
    sql = "select * from work.userdata where id = '%s';" % id
    if cursor.execute(sql) == 0:
        return '없어요'
    else:
        re = cursor.fetchone()
        if pw == re[1]:
            return re[2] + '님, 환영합니다.'
        else:
            return '비밀번호가 틀렸어요'

if __name__ == '__main__':
    app.run(debug=True)
    db.close()
