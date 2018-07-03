import ctypes
from ctypes import windll, Structure, c_ulong, byref
from win32gui import GetWindowText, GetForegroundWindow
import sys, getopt, time

def main(argv):
    windll.user32.SetProcessDPIAware()
    
    x = True
    game = "Skyrim"
    screenLimit = 1920
    screenOffset = 0
    limitOffset = 1
    buffer = 100

    class POINT(Structure):
        _fields_ = [("x", c_ulong), ("y", c_ulong)]
        
    try:
        opts, args = getopt.getopt(argv,"hw:o:b:t:",["width=","offset=","buffer=","target="])
    except getopt.GetoptError:
        print('MouseLock.py -w <width in px> -o <offset in px> -b <buffer in px> -t <target>')
        sys.exit(2)
        
    for opt, arg in opts:
        if opt == '-h':
            print('MouseLock.py -w <width in px> -o <offset in px> -t <target>')
            sys.exit()
        elif opt in ("-w", "--width"):
            screenLimit = int(arg)
        elif opt in ("-o", "--offset"):
            screenOffset = int(arg)
        elif opt in ("-b", "--buffer"):
            buffer = int(arg)
        elif opt in ("-t", "--target"):
            game = arg
            
    totalLimit = screenLimit + screenOffset - limitOffset
    
    
    print('MouseLock Active')    
    print('Screen Width:', screenLimit, 'px, Screen Offset:', screenOffset, 'px, Buffer: ', buffer, 'px')
    print('Locking on:', game)
    
    pt = POINT()
    while(x):
        fg_window_name = GetWindowText(GetForegroundWindow()).lower()
        if (game.lower() == fg_window_name):
            print("Lock is engaged              ", end='\r')
            windll.user32.GetCursorPos(byref(pt))
            # print("X: ", pt.x, " Y: ", pt.y, " ", end="\r")
            if(pt.x > (screenLimit + screenOffset - buffer)):
                windll.user32.SetCursorPos(totalLimit - buffer,pt.y)
            elif (pt.x < (screenOffset + buffer)):
                windll.user32.SetCursorPos(screenOffset + buffer,pt.y)
        else:
            print("Lock is disengaged           ", end='\r')
        time.sleep(0.01)
          
if __name__ == "__main__":
   main(sys.argv[1:])      
