# MouseLock
## Introduction:
MouseLock is a simple utility to bind your mouse cursor to one screen
    
## Usage:
Just double click the MouseLock.exe, which should open a command window telling you that MouseLock is active.

The application is by default set to the left-most screen with a width of 1920px (FullHD), but supports different resolutions.
If you run a different sized screen you can use "MouseLock -w <width of the screen in px> -o <offset from the left-most edge in px>"

Should you want the application to lock onto another application or game than Skyrim, you can use the parameter "-t <target>".
To find out what the application is check the window title or use GetWindow.exe.
It writes the last focused window once per second into log.txt

## Example:
You want limit your mouse to your 1440p (2560x1440) screen, but have two 1080p (1920x1080) screens left and right of it.
To set the parameters you simply edit the MouseLock_Custom.bat and it should look like this:
>MouseLock -w 2560 -o 1920
    
## Dependencies:
MouseLock requires pywin32.
>pip install pywin32

Building the exe requires cx_Freeze as well as idna
>pip install cx_Freeze idna
