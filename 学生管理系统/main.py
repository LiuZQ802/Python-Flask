import flask
from flask import Flask
from flask import request
import db_operate

app = Flask(__name__,
            static_url_path='/static',  # 静态文件路径
            static_folder='static',
            template_folder='templates'  # 模板文件
            )


@app.route('/')
def index():
    return flask.render_template('index.html')


login = {"status": 1}


@app.route('/login', methods=['POST'])
def login():
        #接受post请求
    if request.method == 'POST':
        uname = request.form.get('uname')
        passwd = request.form.get('passwd')
    flag='0'
    if db_operate.login_is_success(uname, passwd):
        #login['success'] = 1
        flag='1'
    else:
        #login['success'] = 0
        flag='0'
    return flag


def main():
    # sql = 'select * from users'
    # select(sql)
    '''
    sql = """
          INSERT INTO users(username,passwd)VALUES("zyj","123")
          """
    insert(sql)

    sql="""
        DELETE FROM users WHERE id=3
    """
    delete(sql)


    sql = """
        UPDATE users SET passwd="456" WHERE id=2
    """
    update(sql)
    '''


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=80, debug=True)
