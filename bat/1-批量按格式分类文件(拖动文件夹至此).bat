@echo off
setlocal EnableDelayedExpansion

if "%~1"=="" (
    echo �뽫�ļ����Ϸŵ����������ļ����Խ�������
    pause
    exit /b
)

rem ��ȡ�Ϸŵĵ�һ���ļ���·��
set folderPath="%~1"

rem ���·���Ƿ�ȷʵ��һ���ļ���
if not exist "%folderPath%" (
    echo ����: ָ����·��������Ч���ļ��С�
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
        echo �ļ��� !ext! �Ѵ���.
    )

    if exist "!ext!\!fname!!ext!" (
        echo �ļ� !fname!!ext! ���ļ��� !ext! ���Ѵ��ڣ����ᱻ����.
        pause
    )

    move "%%i" "!ext!"
)

echo ������ɣ�
pause