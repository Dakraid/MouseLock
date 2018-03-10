from win32gui import GetWindowText, GetForegroundWindow
import time

x = 1
while (x):
    fg_window_name = GetWindowText(GetForegroundWindow()).lower()
    print(fg_window_name + "                         ", end='\r')
    with open("logs.txt", "a") as text_file:
        text_file.write(fg_window_name + "\n")
    time.sleep(1)

