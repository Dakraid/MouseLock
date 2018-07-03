import ctypes
from ctypes import windll, Structure, c_ulong, byref
from win32gui import GetWindowText, GetForegroundWindow
import win32api
import sys, getopt, time

def main(argv):
    windll.user32.SetProcessDPIAware()
    
    x = True
    game = "Skyrim"
    screenLimit = 1920
    screenOffset = 0
    limitOffset = 1

    class POINT(Structure):
        _fields_ = [("x", c_ulong), ("y", c_ulong)]
        
    try:
        opts, args = getopt.getopt(argv,"hw:o:t:",["width=","offset=","target="])
    except getopt.GetoptError:
        print('MouseLock.py -w <width in px> -o <offset in px> -t <target>')
        sys.exit(2)
        
    for opt, arg in opts:
        if opt == '-h':
            print('MouseLock.py -w <width in px> -o <offset in px> -t <target>')
            sys.exit()
        elif opt in ("-w", "--width"):
            screenLimit = int(arg)
        elif opt in ("-o", "--offset"):
            screenOffset = int(arg)
        elif opt in ("-t", "--target"):
            game = arg
            
    totalLimit = screenLimit + screenOffset - limitOffset
    
    
    print('MouseLock Active')    
    print('Screen Width:', screenLimit, 'px, Screen Offset:', screenOffset, 'px')
    print('Locking on:', game)
    
    pt = POINT()
    while(x):
        fg_window_name = GetWindowText(GetForegroundWindow()).lower()
        if (game.lower() == fg_window_name):
            print("Lock is engaged              ", end='\r')
            windll.user32.GetCursorPos(byref(pt))
            if(pt.x > (screenLimit + screenOffset)):
                windll.user32.SetCursorPos(totalLimit,pt.y)
            elif (pt.x < (screenOffset)):
                windll.user32.SetCursorPos(screenOffset,pt.y)
        else:
            print("Lock is disengaged           ", end='\r')
        time.sleep(0.1)
          
if __name__ == "__main__":
   main(sys.argv[1:])      
