from ctypes import CDLL, c_char_p
import sys

lib = CDLL('./cursor_windows.dll')

xStart = lib.getCursorX()
yStart = lib.getCursorY()
x = 0
y = 0

def reset():
    global x
    global y
    x = 0
    y = 0

def move_up(count=1):
    global y
    y-=count
    lib.setCursorPos(x + xStart, y + yStart)

def move_down(count=1):
    global y
    y+=count
    lib.setCursorPos(x + xStart, y + yStart)

def move_right(count=1):
    global x
    x+=count
    lib.setCursorPos(x + xStart, y + yStart)

def move_left(count=1):
    global x
    x-=count
    lib.setCursorPos(x + xStart, y + yStart)

def writeToCursorPos(value):
    lib.writeConsole(str(value), 1)
    lib.setCursorPos(x + xStart, y + yStart)

def writeStringToCursorPos(string):
    lib.writeConsole(string, len(string))
    lib.setCursorPos(x + xStart, y + yStart)

def goto(xPos, yPos):
    global x
    global y
    x = xPos
    y = yPos
    lib.setCursorPos(x + xStart, y + yStart)


