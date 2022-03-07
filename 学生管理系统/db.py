import pymysql
import json

# 数据库连接
def Get_db():
    host = 'localhost'
    user = 'root'
    password = 'root'
    db = 'student'
    try:
        db = pymysql.connect(host=host, user=user, password=password, db=db)
    except:
        print("数据库连接失败")
    return db


# 查询操作
def select(sql):
    db = Get_db()
    cursor = db.cursor()
    try:
        cursor.execute(sql)
        db.commit()
    except:
        print('查询语句执行失败')

    returns=cursor.fetchall()
    db.close()
    return returns   #返回结果集


# 插入操作
def insert(sql):
    db = Get_db()
    cursor = db.cursor()
    try:
        cursor.execute(sql)
        db.commit()
        print("插入成功")
    except:
        print('插入语句执行失败')
        db.rollback()
    db.close()


# 删除操作
def delete(sql):
    db = Get_db()
    cursor = db.cursor()
    try:
        cursor.execute(sql)
        db.commit()
        print('删除成功')
    except:
        db.rollback()
        print('删除失败')
    db.close()


# 修改操作
def update(sql):
    db = Get_db()
    cursor = db.cursor()
    try:
        cursor.execute(sql)
        db.commit()
        print('修改成功')
    except:
        db.rollback()
        print('修改失败')
    db.close()
