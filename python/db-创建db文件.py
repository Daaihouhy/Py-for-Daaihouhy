# 导入 sqlite3 模块
import sqlite3

# 数据库文件名，路径使用了原始字符串表示法以支持反斜杠
db_file = r'输入db表路径'

try:
    # 连接到 SQLite 数据库
    # 如果数据库不存在，会自动创建
    conn = sqlite3.connect(db_file)
    
    # 创建一个 Cursor 对象
    c = conn.cursor()
    
    # 创建一个名为 '表1' 的表，包含字段1、字段2 两列，字段长度为254
    # 注意：SQLite 对表名和字段名的字符支持广泛，包括中文
    c.execute('''CREATE TABLE IF NOT EXISTS 表1 (
                 字段1 TEXT(254),
                 字段2 TEXT(254)
                 )''')
    
    print('表已创建成功')
finally:
    # 确保数据库连接被关闭
    if conn:
        conn.close()
