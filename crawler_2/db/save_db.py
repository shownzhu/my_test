import mysql.connector


QQ_USER = "740244173"
QQ_PASSWORD = "fly1219"


# connect default db
def connect_default_mysql():
    user_name = "root"
    password = "root123456"
    database = "crawler"
    # �����ݿ����ӣ�������Լ����û��������뼰���ݿ����ƽ����޸ģ�
    cnn = mysql.connector.connect(user=user_name, passwd=password, database=database)

    # ʹ��cursor()������ȡ�����α�
    cursor = cnn.cursor()
    return cnn, cursor