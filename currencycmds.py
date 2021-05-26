#Functions for currency commands

from pynput.keyboard import Key, Controller
import time
keyboard= Controller()

def post():
    keyboard.type("pls pm")
    keyboard.press(Key.enter)
    keyboard.release(Key.enter)
    time.sleep(3)               #buffer for reponse menu to load 
    keyboard.type("k")
    keyboard.press(Key.enter)
    keyboard.release(Key.enter)

def hunt():
    keyboard.type("pls hunt")
    keyboard.press(Key.enter)
    keyboard.release(Key.enter)

def highlow():
    keyboard.type("pls hl")
    keyboard.press(Key.enter)
    keyboard.release(Key.enter)
    time.sleep(3)               #buffer for reponse menu to load 
    keyboard.type("low")
    keyboard.press(Key.enter)
    keyboard.release(Key.enter)

def fish():
    keyboard.type("pls fish")
    keyboard.press(Key.enter)
    keyboard.release(Key.enter)

def beg():
    keyboard.type("pls beg")
    keyboard.press(Key.enter)
    keyboard.release(Key.enter)

def deposit():
    keyboard.type("pls deposit max")
    keyboard.press(Key.enter)
    keyboard.release(Key.enter)

def dig():
    keyboard.type("pls dig")
    keyboard.press(Key.enter)
    keyboard.release(Key.enter)

def farm(pm,h,f,d):
    while True:
        time.sleep(40)
        deposit()
        time.sleep(1)
        if pm == 1:
            post()
            time.sleep(1)
        if h == 1:
            hunt()
            time.sleep(1)
        if f == 1:
            fish()
            time.sleep(1)
        if d == 1:
            dig()
            time.sleep(1)
            
        highlow()
        time.sleep(1)
        beg()

        
    
