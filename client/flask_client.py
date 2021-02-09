######################################################
#        > File Name: flask_client.py
#      > Author:
 #     > Mail: 2
 #     > Created Time: Mon 20 May 2019 11:52:00 AM CST
 ######################################################

from flask import Flask, send_file,render_template
import sys


app = Flask(__name__)

@app.route('/index/index')
def index():
    #首页

    management = {'name': 'jiangfeijun',
                  'dep_name': '经理办公室',
                  'position_name': '办公室主任',
                  'job_no':'100101'
                  }


    return render_template('index/index.html',management=management)

@app.route('/user/login')
def login():
    #登录
    return send_file('templates/user/login.html')

@app.route('/login_callback')
def login_callback():
    #授权登录
    return send_file('templates/oauth_callback.html')

@app.route('/user/register')
def register():
    #注册
    return send_file('templates/user/register.html')
@app.route('/user/login_forget_password')
def login_forget_password():
    #忘记密码
    return send_file('templates/user/findpwd.html')

@app.route('/user/change_password')
def change_password():
    #修改密码
    return send_file('templates/user/changepwd.html')

@app.route('/user/my_info')
def info():
    #个人信息
    return send_file('templates/index/My_info.html')

@app.route('/user/my_ip')
def my_ip():
    #绑定IP
    return send_file('templates/index/My_IP.html')

@app.route('/user/update')
def change_info():
    #修改个人信息
    return send_file('templates/user/update_info.html')

# @app.route('/department')
# def department_list():
#     #部门列表
#     return send_file('templates/department/BuMenGL_list.html')


@app.route('/report/content')
def content():
    return send_file('templates/report/content.html')


@app.route('/notice/index_first')
def index_first():
    return send_file('templates/notice/index_first.html')


@app.route('/notice/notice')
def notice():
    return send_file('templates/notice/notice.html')


@app.route('/notice/notice_add')
def notice_add():
    return send_file('templates/notice/notice_add.html')


@app.route('/notice/notice_list')
def notice_list():
    return send_file('templates/notice/notice_list.html')


@app.route('/notice/notice_update')
def notice_update():
    return send_file('templates/notice/notice_update.html')


@app.route('/report/report_add')
def report_add():
    return send_file('templates/report/report_add.html')


@app.route('/report/report_list')
def report_list():
    return send_file('templates/report/report_list.html')


@app.route('/report/report_update')
def report_update():
    return send_file('templates/report/report_update.html')

@app.route('/address')
def address():
    #查询通讯录页面
    return send_file('templates/address_book/address.html')

@app.route('/weather')
def weather():
    #报告列表
    return send_file('templates/weather/weather.html')

@app.route('/department')
def department_list():
    #部门列表
    return send_file('templates/department/BuMenGL_list.html')

@app.route('/department/add_department')
def add_department():
    return send_file('templates/department/BuMenGL_bmtj.html')


@app.route('/department/add_position')
def department_add():
    return send_file('templates/department/BuMenGL_zwtj.html')

@app.route('/management')
def management_list():
    #员工列表
    return send_file('templates/management/manager_info.html')



@app.route('/management/add')
def add_management():
    return send_file('templates/management/management_add.html')

@app.route('/management/search')
def search():
    return send_file('templates/management/management_search.html')



if __name__ == '__main__':
    app.run(debug=True)

