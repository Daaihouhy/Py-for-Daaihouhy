import sqlite3
import pandas as pd
import os
from tqdm import tqdm

# 文件夹路径，假设你的数据库文件都存放在这个文件夹中
folder_path = r'输入文件夹路径'

# 假设所有数据库中的表名都是相同的
table_name = 'WQDSYQRJSYD_KZ'  # 您要合并的表名

# 用于保存从所有数据库加载的DataFrame的列表
df_list = []

# 列出文件夹下的所有.db文件
db_files = [file for file in os.listdir(folder_path) if file.endswith('.db')]

# 使用tqdm在数据库文件上进行迭代，以展示进度条
for db_filename in tqdm(db_files, desc='Merging databases', unit='db'):
    # 数据库文件的完整路径
    db_path = os.path.join(folder_path, db_filename)
    
    # 连接到SQLite数据库
    conn = sqlite3.connect(db_path)
    
    # 从数据库加载表到DataFrame
    df = pd.read_sql_query(f"SELECT * FROM {table_name}", conn)
    
    # 添加DataFrame到列表中
    df_list.append(df)
    
    # 关闭数据库连接
    conn.close()

# 合并所有DataFrame
merged_df = pd.concat(df_list, ignore_index=True)

# 将合并后的数据导出到Excel
excel_output = r'导出Excel路径'
merged_df.to_excel(excel_output, index=False)

print(f'Merged data has been exported to {excel_output}')
