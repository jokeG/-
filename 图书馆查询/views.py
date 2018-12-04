from jinja2 import Template
import pymysql


def error(env):
    return 'web erro'


def libary(env):
    conn = pymysql.connect(host='127.0.0.1', port=3306, user='root', db='django', password='123')
    cur = conn.cursor(pymysql.cursors.DictCursor)
    cur.execute('select * from libary')
    dic = cur.fetchall()
    print(dic)
    with open('temlates/libary.html', 'r') as f:
        data = f.read()
    tem = Template(data)
    response = tem.render(book_list=dic)
    return response
