@echo off
chcp 65001

set "SRC=%~dp0src"
set "PYTHON=%~dp0venv/Scripts/python.exe"
echo SRC=%SRC%
echo PYTHON=%PYTHON%

if not exist "%~dp0.log" (
    mkdir "%~dp0.log"
)
set "LOG_FILE=%~dp0.log\app.log"
echo LOG_FILE=%LOG_FILE%

echo SRC=%SRC% > "%LOG_FILE%"
echo PYTHON=%PYTHON% >> "%LOG_FILE%"

rem 基础检查
if not exist "%PYTHON%" (
    echo "未配置 Python.exe"
    exit /b 1
)
if not exist "%SRC%" (
    echo "未设置 src 目录"
    exit /b 1
)
if not exist "%SRC%\app.py" (
    echo "无法找到 %SRC%\app.py"
    exit /b 1
)

echo "启动中..."
"%PYTHON%" "%SRC%\app.py" >> "%LOG_FILE%" 2>&1
if "%errorlevel%" neq 0 (
    echo "运行出错，请查看 %LOG_FILE%"
)
timeout /t 10
exit 0

