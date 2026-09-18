@echo off
setlocal
rem CommunicationMod starts from the game directory.  Keep the repository
rem path in one place so this wrapper works even when the checkout path has
rem spaces.
set "REPO=C:\Users\shenj\Documents\ChatGPT\spire-scholar 2"
cd /d "%REPO%"
set "PYTHONIOENCODING=utf-8"
"C:\Users\shenj\AppData\Local\Programs\Python\Python312\python.exe" -m bridge.collect_states --interval 1
endlocal
