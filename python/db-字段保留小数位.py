import sqlite3
import os
import glob

# 文件夹路径
folder_path = r'C:\Users\daihao\Desktop\新建文件夹'

# db文件匹配模式
db_pattern = os.path.join(folder_path, '*.db')

# 列出文件夹内所有的.db文件
db_files = glob.glob(db_pattern)

# 需要四舍五入的表及字段信息
tables_fields_rounding = {
    'WQDSYQRJSYD_KZ': {'ZCJG': 1, 'JJJZ': 1},
    # 'table2': {'field3': 1, 'field4': 2},
    # 可以继续添加其他表和字段
}

# 遍历每个数据库文件
for db_path in db_files:
    file_name = os.path.basename(db_path)
    print(f"开始处理数据库文件：{file_name}")
    # 使用with语句自动管理资源，提高异常处理能力
    with sqlite3.connect(db_path) as conn:
        cursor = conn.cursor()

        # 遍历每个表及其对应字段
        for table_name, fields in tables_fields_rounding.items():
            for field_name, decimals in fields.items():
                # 构建SQL语句
                rounding_sql = f"UPDATE {table_name} SET {field_name} = ROUND({field_name}, {decimals})"
                print(f"正在执行四舍五入操作：表{table_name} 字段{field_name} 更新到{decimals}位小数")

                # 执行SQL语句，并进行错误处理
                try:
                    cursor.execute(rounding_sql)
                    print("操作成功。")
                except sqlite3.Error as e:
                    # 打印异常并继续处理其他表或者字段，避免一个错误导致整个流程停止
                    print(f"处理文件 {file_name} 时，在更新 {table_name}.{field_name} 时发生错误：{e}")
                    continue  # 继续执行下一个field的更新

        # 提交事务，保存所有更改
        conn.commit()
    # 关闭游标是自动的，由于使用了with语句，无需显式关闭
    print(f"数据库 {file_name} 已经更新完毕。")