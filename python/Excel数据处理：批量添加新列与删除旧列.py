import pandas as pd
import os
from tqdm import tqdm

# 设置工作目录，即包含Excel文件的文件夹路径
work_dir = r'C:\Users\新建文件夹'

# 新增列的名称和预设值
new_column_name = '新增列1123'
new_column_default_value = '哈哈'  # 新列的预设值

# 要删除列的名称
old_column_name = '新增列'

# 指定的sheet名，如果为None，则代表所有sheet
sheet_name = None  # 或者设定为 'Sheet1' 或其他特定的sheet名

# 用于存储操作结果的字典
processed_files = {
    'updated': [],
    'ignored': []
}

print("开始处理文件...")

# 使用tqdm列出文件夹中的所有文件，并进行迭代处理
for filename in tqdm(os.listdir(work_dir), desc="Processing files", unit="file"):
    # 检查文件扩展名是否为.xls或.xlsx，意味着它是一个Excel文件
    if filename.endswith(('.xls', '.xlsx')):
        # 构建完整的文件路径
        file_path = os.path.join(work_dir, filename)
        
        try:
            # 打印正在处理的文件名
            print(f"正在处理文件: {filename}")
            
            # 使用pandas读取Excel文件的指定sheet，如果sheet_name为None则读取所有sheet
            if sheet_name:
                df = pd.read_excel(file_path, sheet_name=sheet_name)
            else:
                df = pd.read_excel(file_path, sheet_name=None)
            
            # 处理单个或多个sheet
            if sheet_name or isinstance(df, pd.DataFrame):
                # 添加新列，并删除旧列
                df[new_column_name] = new_column_default_value
                df.drop(old_column_name, axis=1, inplace=True, errors='ignore')
                # 保存修改到同一文件
                df.to_excel(file_path, index=False, sheet_name=sheet_name)
            else:
                # 处理包含多个sheet的Excel文件
                with pd.ExcelWriter(file_path) as writer:
                    for sheet in df:
                        df_sheet = df[sheet]
                        df_sheet[new_column_name] = new_column_default_value
                        df_sheet.drop(old_column_name, axis=1, inplace=True, errors='ignore')
                        df_sheet.to_excel(writer, index=False, sheet_name=sheet)
            
            # 打印成功更新的文件名
            print(f"文件 '{filename}' 更新成功。")
            processed_files['updated'].append(filename)
        except Exception as e:
            print(f"处理文件 {filename} 时发生错误：{e}")
            processed_files['ignored'].append(filename)
    else:
        # 如果不是Excel文件，则忽略
        processed_files['ignored'].append(filename)

# 打印处理结果
print("处理完成。")
print("更新的文件:", processed_files['updated'])
print("未处理或被忽略的文件:", processed_files['ignored'])
