import sqlite3
import os

# 全局变量
base_path = r'输入文件夹路径'
custom_names = ['custom_db_1', 'custom_db_2', 'custom_db_3']
table_name = 'WQDSYQRJSYD_KZ'
table_columns = """
    列1 TEXT,
    列2 INTEGER,
    列3 DOUBLE
"""

def create_database(file_name):
    try:
        # 连接到数据库并创建表
        conn = sqlite3.connect(file_name)
        cursor = conn.cursor()
        cursor.execute(f'CREATE TABLE IF NOT EXISTS {table_name} ({table_columns})')
        conn.commit()
        conn.close()
        print(f"已成功创建数据库文件：{os.path.basename(file_name)}")
    except sqlite3.Error as e:
        print(f"创建数据库文件时发生错误：{e}")

def create_multiple_databases():
    for i, custom_name in enumerate(custom_names, start=1):
        db_file = f"{base_path}{custom_name}.db"
        create_database(db_file)

# 创建多个数据库文件
create_multiple_databases()
