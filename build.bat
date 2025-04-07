@echo off
echo Gerando executável da Calculadora...
pyinstaller --onefile --noconsole ^
--add-data "C:/Users/Samue/AppData/Local/Programs/Python/Python312/Lib/site-packages/customtkinter;customtkinter" ^
main.py
pause
