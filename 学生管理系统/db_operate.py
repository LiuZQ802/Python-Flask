import db


def login_is_success(uname, passwd):
        #去空格
    uname = uname.strip()
    passwd = passwd.strip()
    sql = ' SELECT `passwd` FROM `users` WHERE `username`="%s" limit 0,1' % (uname)
    result = db.select(sql)
        #元组为空直接返回false
    if(len(result)==0):
        return False
    if result[0][0] == passwd:
        return True
    else:
        return False
