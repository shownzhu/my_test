# coding: utf-8
# import mysql.connector
#
#
# QQ_USER = "909569254"
# QQ_PASSWORD = "15638396298"
#
#
# # connect default db
# def connect_default_mysql():
#     user_name = "root"
#     password = "root123456"
#     database = "crawler"
#     # �����ݿ����ӣ�������Լ����û��������뼰���ݿ����ƽ����޸ģ�
#     cnn = mysql.connector.connect(user=user_name, passwd=password, database=database)
#
#     # ʹ��cursor()������ȡ�����α�
#     cursor = cnn.cursor()
#     return cnn, cursor