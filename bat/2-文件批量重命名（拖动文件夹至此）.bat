@echo off
chcp 65001
setlocal enabledelayedexpansion

REM 检查是否有一个参数传递给批处理文件
if "%~1"=="" (
    echo 请将文件夹拖放到此批处理文件上以进行重命名操作。
    exit /b
)

REM 设置需要重命名的文件所在的目录
set "source_dir=%~1"

REM 设置要添加的内容
set "prefix=prefix_"

REM 初始化计数器
set /a counter=1

REM 进入指定的目录
cd /d "%source_dir%"

REM 遍历当前目录下的所有文件
for %%f in (*) do (
	REM 获取当前文件名（不包括扩展名）
    set "filename=%%~nf"
    REM 替换内容，添加set "filename=!filename:old=new!"
    REM 获取当前文件的扩展名
    set "ext=%%~xf"
    
    REM 生成新的文件名，调整!prefix!位置为添加内容位置
	REM 计数器为!counter!
    set "new_name=!prefix!!filename!!ext!"
    
    REM 重命名文件
    ren "%%f" "!new_name!"
    
    REM 增加计数器
    set /a counter+=1
)

echo Done.
endlocal