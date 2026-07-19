@echo off
setlocal

cd /d "%~dp0"

if not exist ".venv\Scripts\python.exe" (
    echo The project virtual environment was not found.
    echo.
    echo Open PowerShell in this folder and run:
    echo py -m venv .venv
    echo .\.venv\Scripts\python.exe -m pip install -r requirements.txt
    echo.
    pause
    exit /b 1
)

start "AAR Generator Server" powershell -NoExit -ExecutionPolicy Bypass -File "%~dp0run_windows.ps1"

timeout /t 4 /nobreak >nul
start "" "http://localhost:7860"

endlocal
