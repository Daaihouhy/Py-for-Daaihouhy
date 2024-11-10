import os
import sqlite3
import pandas as pd

# 指定数据库文件夹路径
db_folder_path = 'your_database_folder_path'
# 指定导出文件夹路径
export_folder_path = 'your_export_folder_path'

# 获取文件夹中所有的 .db 文件
db_files = [f for f in os.listdir(db_folder_path) if f.endswith('.db')]
# 遍历每个数据库文件
for db_file in db_files:
    db_file_path = os.path.join(db_folder_path, db_file)
    # 连接到 SQLite 数据库
    conn = sqlite3.connect(db_file_path)
    # 查询数据库中的表名
    cursor = conn.cursor()
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
    tables = cursor.fetchall()
    # 遍历每个表，导出为 Excel 文件
    for table in tables:
        table_name = table[0]
        df = pd.read_sql_query(f"SELECT * FROM {table_name};", conn)
        # 构建导出文件路径
        export_file_path = os.path.join(export_folder_path, f'{db_file}_{table_name}.xlsx')
        # 将表导出为 Excel 文件
        df.to_excel(export_file_path, index=False, engine='openpyxl')
    # 关闭数据库连接
    conn.close()