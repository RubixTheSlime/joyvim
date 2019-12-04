python3 << en
import sys, os
import vim#pynvim as vim
import threading,time

sys.stdout = open(os.devnull, 'w')
from pygame.display import init as displayInit
from pygame.event import get as eventGet
from pygame.time import Clock
from pygame import joystick
from pygame import quit as pygamequit
from pygame import QUIT,JOYBUTTONDOWN
sys.stdout = sys.__stdout__

def press(text):
    vim.async_call(vim.input,text)

def gameloop():
    def handlepress():
        if js.get_button(0):
            press('a')
        elif js.get_button(1):
            press('')
        elif js.get_button(2):
            press('t')
        elif js.get_button(3):
            press('b')
        elif js.get_button(9):
            vim.async_call(vim.quit)
            return #True
    displayInit()
    clock = Clock()
    joystick.init()
    js = joystick.Joystick(0)
    js.init()
    done = False
    while not done:
        for event in eventGet():
            if event.type == QUIT:
                done = True
            elif event.type == JOYBUTTONDOWN:
                if handlepress():
                    done = True
        clock.tick(60)
    pygamequit()

exitFlag = 0
class myThread (threading.Thread):
    def __init__(self, threadID, name, counter):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        self.counter = counter
    def run(self):
        gameloop()

thread1 = myThread(1, 'Thread1', 1)
thread1.start()
