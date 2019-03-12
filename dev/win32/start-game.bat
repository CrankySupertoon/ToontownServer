@echo off

call constants.bat

set ROOT_PATH=..\..\
set PATH_TO_STARTUP_CONFIGURATION=%ROOT_PATH%%STARTUP_CONFIGURATION_FILE%
set PATH_TO_FILE=""

:: Parse through the start up configuration XML file for the location of ppython.exe.
setlocal enableextensions enabledelayedexpansion
set "xmlFile=%PATH_TO_STARTUP_CONFIGURATION%"
for /f "tokens=1,2 delims=:" %%n in ('findstr /n /i /c:"<path_to_panda_ppython>" "%xmlFile%"') do (
    for /f "tokens=*" %%l in ('type "%xmlFile%" ^| more +%%n') do set "PATH_TO_FILE=%%l" & goto end_loop
)
:end_loop

echo.

:: Don't get the location of ppython.exe if it was found or is valid.
if "%PATH_TO_FILE:~-19%"=="\python\ppython.exe" (
    if exist %PATH_TO_FILE% (
        goto valid_ppython_path
    )
)

:: Otherwise, execute all of this code below to find ppython.exe.
set /A PATH_TO_PANDA_ATTEMPTS=0
echo Indicate the path to your Panda3D folder!
echo.

:get_path_to_panda

set PATH_TO_PANDA=-1
set /P PATH_TO_PANDA=Path: 

set PATH_TO_FILE=%PATH_TO_PANDA%\python\ppython.exe

if /I "%PATH_TO_PANDA%"=="q" (
    exit
) else if exist %PATH_TO_FILE% (
    set PATH_TO_PPYTHON = %PATH_TO_FILE%
) else (
    set /A PATH_TO_PANDA_ATTEMPTS+=1
    echo.

    :: Sorry, I like to make an interactive prompt.
    if %PATH_TO_PANDA_ATTEMPTS% gtr 3 (
        echo *sigh* Please give up. I'm only joking, but please ask Abe or myself for help.
    )

    echo At any time, press Q to quit.
    echo 1. The path to your Panda3D folder was invalid!
    echo 2. If the path was not invalid, then check to see whether you have a folder named 'python' inside your Panda3D folder.
    echo 3. Then check to see whether you have a file named 'ppython.exe' inside that 'python' folder.
    echo 4. You only need to provide the path to your Panda3D folder, and this batch script will find 'ppython.exe' for you.
    echo.
    goto get_path_to_panda
)

:: Save to an XML file designated for startup configurations.
echo ^<path_to_panda_ppython^>>> %PATH_TO_STARTUP_CONFIGURATION%
echo     %PATH_TO_FILE%>> %PATH_TO_STARTUP_CONFIGURATION%
echo ^</path_to_panda_ppython^>>> %PATH_TO_STARTUP_CONFIGURATION%

:valid_ppython_path

echo Choose your connection method!
echo.
echo #1 - Localhost
echo #2 - Custom
echo.

:selection

set INPUT=-1
set /P INPUT=Selection: 

if %INPUT%==1 (
    set TTS_GAMESERVER=127.0.0.1
) else if %INPUT%==2 (
    set TTS_GAMESERVER=%GAME_SERVER_IP_ADDRESS%
) else (
	goto selection
)

echo.

set /P TTS_PLAYCOOKIE=Username: 

echo.

echo ===============================
echo Starting Toontown Stride...
echo ppython: %PATH_TO_FILE%

echo Username: %TTS_PLAYCOOKIE%

echo Gameserver: %TTS_GAMESERVER%
echo ===============================

cd ../../

:main
%PATH_TO_FILE% -m toontown.toonbase.ToontownStart
pause

goto main
