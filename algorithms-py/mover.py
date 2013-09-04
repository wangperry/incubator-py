
import win32api, win32con
import time
import random


def click(x,y):
    win32api.SetCursorPos((x,y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,x,y,0,0)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,x,y,0,0)

#
# Simple mouse mover
#
def main():     
    while True:          
        x = random.randint(100, 700)
        y = random.randint(500, 1200)
        click(x, y)    
        time.sleep(15) # delays for 15 seconds   
    print("cursor mover finished")    


if __name__ == '__main__':
    main()