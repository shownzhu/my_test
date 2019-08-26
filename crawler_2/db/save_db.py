import mysql.connector


QQ_USER = "909569254"
QQ_PASSWORD = "15638396298"


# connect default db
def connect_default_mysql():
    user_name = "root"
    password = "root123456"
    database = "crawler"
    # 打开数据库连接（请根据自己的用户名、密码及数据库名称进行修改）
    cnn = mysql.connector.connect(user=user_name, passwd=password, database=database)

    # 使用cursor()方法获取操作游标
    cursor = cnn.cursor()
    return cnn, cursor