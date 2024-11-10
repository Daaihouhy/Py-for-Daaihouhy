import sqlite3
import os

# 定义需要替换的表名、字段和旧值、新值
table_column_old_new_map = {
    'WQDSYQRJSYD_KZ': {
        'EJDLMC': {'0601': '工业用地', '旧值2': '新值2'},
        'EJDLBM': {'工业用地': '0601'}
    },
    # 实际使用时应避免重复定义相同的表名。
}

# 遍历指定目录下所有的 .db 文件
db_folder = r'输入db文件文件夹路径'
print("开始遍历文件夹中的.db文件...")

for filename in os.listdir(db_folder):
    if filename.endswith('.db'):
        db_path = os.path.join(db_folder, filename)
        print(f"正在处理数据库文件: {filename}")
        with sqlite3.connect(db_path) as conn:
            c = conn.cursor()

            for table_name, columns in table_column_old_new_map.items():
                for column_name, old_new_map in columns.items():
                    for old_value, new_value in old_new_map.items():
                        try:
                            sql = f'UPDATE {table_name} SET {column_name} = ? WHERE {column_name} = ?;'
                            c.execute(sql, (new_value, old_value))
                            print(f"在表{table_name}中，将列{column_name}的旧值'{old_value}'更新为新值'{new_value}'。")
                        except sqlite3.Error as e:
                            print(f"处理数据库文件 '{filename}' 时出错: 错误位于表 '{table_name}', 列 '{column_name}'，错误信息: {e}")
            conn.commit()
        print(f"数据库文件: {filename} 处理完成。")

print("所有数据库文件处理完毕。")
