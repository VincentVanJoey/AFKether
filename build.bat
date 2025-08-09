@echo off
REM This script will compile the extract script and create an installer.
 
set OUTPUT_DIR=dist
 
del /s /q build
del /s /q dist
 
echo Installing PyInstaller ...
py -3.13 -m pip install PyInstaller
 
echo Compiling the extract script ...
py -3.13 -m PyInstaller --distpath %OUTPUT_DIR% AFKether_Details.spec
 
REM Check if the build was successful
 
if %ERRORLEVEL% neq 0 (
 
    echo Build failed!
 
    exit /b 1
 
)
 
echo Build completed successfully! Executable is located in the %OUTPUT_DIR% folder.
 
echo Done.