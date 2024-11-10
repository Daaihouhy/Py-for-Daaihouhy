import sqlite3  # 导入sqlite3库以与SQLite数据库交互
import os  # 导入os库以使用操作系统相关的功能

# 指定包含数据库文件的文件夹路径
folder_path = r'C:\Users\daihao\Desktop\新建文件夹'

# 获取指定文件夹内所有以.db为扩展名的文件
db_files = [file for file in os.listdir(folder_path) if file.endswith('.db')]

# 设置你要操作的表名
table_name = "WQDSYQRJSYD_KZ"

# 设置你想要添加的新列的名字、数据类型、最大长度、空值是否允许以及默认值
column_name = "嗯嗯1"
data_type = "TEXT"
max_length = 25
is_nullable = True
default_value = None
unique = False
# 指定要从表中删除的列名
column_to_delete = "JJJZ"

# 根据提供的参数构造列定义语句
column_definition = f"{column_name} {data_type}" \
                    + (f"({max_length})" if data_type in ["TEXT", "CHAR", "VARCHAR"] else "") \
                    + (" DEFAULT " + ("NULL" if default_value is None else f"'{default_value}'") if default_value is not None else "") \
                    + (" UNIQUE" if unique else "") \
                    + (" NOT NULL" if not is_nullable else "")

# 遍历找到的数据库文件
for db_file in db_files:
    db_path = os.path.join(folder_path, db_file)  # 获取数据库文件的完整路径
    conn = sqlite3.connect(db_path)  # 连接到数据库
    cursor = conn.cursor()  # 创建数据库操作游标

    try:
        # 尝试添加新列到指定表
        cursor.execute(f"ALTER TABLE {table_name} ADD COLUMN {column_definition};")
        print(f"列'{column_name}'已经添加到表'{table_name}'中.")
    except sqlite3.OperationalError as e:
        print(f"{db_file}操作错误: {e.args[0]}")  # 捕获并打印SQL操作错误信息
    except Exception as e:
        print(f"{db_file}遇到错误: {e.args[0]}")  # 捕获并打印其他错误信息

    try:
        # 准备删除表中的指定列
        # 关闭外键约束，以便能够重命名表和修改结构
        cursor.execute(f"PRAGMA foreign_keys=off;")
        cursor.execute(f"BEGIN TRANSACTION;")  # 开启一个事务
        
        # 将旧表重命名
        cursor.execute(f"ALTER TABLE {table_name} RENAME TO _{table_name}_old;")
        
        # 获取旧表的列信息
        cursor.execute(f"PRAGMA table_info(_{table_name}_old);")
        columns = cursor.fetchall()
        
        # 确定要保留的列名，排除预删除的列
        columns_to_keep = [ci[1] for ci in columns if ci[1] != column_to_delete]
        
        # 创建一个新表，仅包含要保留的列
        cursor.execute(f"CREATE TABLE {table_name} ({', '.join([f'{ci[1]} {ci[2]}' for ci in columns if ci[1] in columns_to_keep])});")
        
        # 将旧表的数据插入到新表中
        cursor.execute(f"INSERT INTO {table_name}({', '.join(columns_to_keep)}) SELECT {', '.join(columns_to_keep)} FROM _{table_name}_old;")
        
        # 删除旧表
        cursor.execute(f"DROP TABLE _{table_name}_old;")
        
        cursor.execute(f"COMMIT;")  # 提交事务
        cursor.execute(f"PRAGMA foreign_keys=on;")  # 重新启用外键约束
        print(f"列 '{column_to_delete}' 已从表 '{table_name}' 中移除。")
    except sqlite3.Error as e:
        print(f"{db_file}操作错误: {e.args[0]}")  # 捕获并打印SQLite错误信息

    # 关闭游标和数据库连接
    cursor.close()
    conn.close()

print("数据库文件执行完毕。")  # 提示数据库文件更新完成