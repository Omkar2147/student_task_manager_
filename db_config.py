import mysql.connector

def get_database_connection():
    connection = mysql.connector.connect(
        host = 'gateway01.ap-southeast-1.prod.aws.tidbcloud.com',
        user = '3dnUAApHURPhx26.root',
        password = 'ZLvvBcbdd0MtGJlJ',
        database = 'student_task_manager',
        port = 4000
    )

    return connection

# def get_database_connection():
#     connection = mysql.connector.connect(
#         host = 'localhost',
#         user = 'root',
#         password = 'omkarK@2147',
#         database = 'student_task_manager1'
#     )

#     return connection