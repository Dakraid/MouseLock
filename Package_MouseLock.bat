rem Build MouseLock
call "MouseLock_Build.bat"
cd ..

IF NOT EXIST GetWindow GOTO NOWIN

rem Build GetWindow
cd GetWindow
call "GetWindow_Build.bat"
cd ..

xcopy /s /y .\GetWindow\build\exe.win-amd64-3.6 .\MouseLock_Standalone\GetWindow\

rem Remove leftovers
del .\MouseLock_Standalone\GetWindow\logs.txt

:NOWIN
xcopy /s /y .\MouseLock\build\exe.win-amd64-3.6 .\MouseLock_Standalone\
xcopy /s /y .\MouseLock\MouseLock_Extras .\MouseLock_Standalone\


rem Package the utility
7z u .\Netrve_MouseLock_Standalone.7z .\MouseLock_Standalone\*