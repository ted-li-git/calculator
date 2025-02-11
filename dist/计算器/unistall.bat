@echo off
title 计算器卸载向导
echo 即将为你卸载计算器
pause
del "%USERPROFILE%\Desktop\计算器.lnk"
rd /s /q %cd%
echo 卸载完毕！
pause