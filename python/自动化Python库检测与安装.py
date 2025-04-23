import subprocess

# 需要检查的包列表
packages_to_check = ["requests", "pandas", "jieba", "numpy"]

# 需要安装但尚未安装的包列表
packages_to_install = []

# 检查每个包是否已经安装
for package in packages_to_check:
    try:
        __import__(package)
    except ImportError:
        packages_to_install.append(package)

# 输出未安装的包列表
if packages_to_install:
    print("以下包尚未安装，需要安装：")
    for pkg in packages_to_install:
        print(pkg)
else:
    print("所有需要的包都已安装。")

# 如果有包需要安装，使用subprocess调用pip并使用清华的源进行安装
if packages_to_install:
    for pkg in packages_to_install:
        try:
            subprocess.run(["pip", "install", "--upgrade", "--user", "--index-url=https://pypi.tuna.tsinghua.edu.cn/simple", pkg], check=True)
        except subprocess.CalledProcessError:
            print(f"安装 {pkg} 失败")

# 再次检查是否安装成功
failed_packages = []
for package in packages_to_install:
    try:
        __import__(package)
    except ImportError:
        failed_packages.append(package)

# 输出安装失败的包
if failed_packages:
    print("以下包安装失败：")
    for pkg in failed_packages:
        print(pkg)
else:
    print("所有包均安装成功。")
