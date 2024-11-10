@echo off
setlocal EnableDelayedExpansion

if "%~1"=="" (
    echo 请将文件夹拖放到此批处理文件上以进行整理。
    pause
    exit /b
)

rem 获取拖放的第一个文件夹路径
set folderPath="%~1"

rem 检查路径是否确实是一个文件夹
if not exist "%folderPath%" (
    echo 错误: 指定的路径不是有效的文件夹。
    pause
    exit /b
)

cd /d "%folderPath%"

for %%i in (*) do (
    set ext=%%~xi
    set fname=%%~ni

    if not exist "!ext!" (
        md "!ext!"
    ) else (
        echo 文件夹 !ext! 已存在.
    )

    if exist "!ext!\!fname!!ext!" (
        echo 文件 !fname!!ext! 在文件夹 !ext! 中已存在，并会被覆盖.
        pause
    )

    move "%%i" "!ext!"
)

echo 整理完成！
pause