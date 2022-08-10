from concurrent.futures import thread
from multiprocessing.connection import wait
from random import randint
from tabnanny import check
from time import sleep
from tracemalloc import start
from turtle import st
from xml.etree.ElementTree import tostring
import sys, time, threading

# Most Seen Number Script
# This Script
check = "nay"
class Loader:
    def bruhmoment(self):
        while check == "ya":
            for char in chars:
                if check == "ya":
                    sys.stdout.write('\r'+"Loading"+char)
                    time.sleep(0.1)

    def __init__(self):
        t = threading.Thread(target=self.bruhmoment)
        t.start()

def randthing():
    return randint(100,999)
threadcheck = 0

chars = [".    ","..    ","...    "]
deez = "R"

while deez == "R":
    check = "ya"
    i = 0
    attempts = input("How many numbers would you like to make \n")
    sleep(0.1)
    Loader()

    doodoo = []
    if len(doodoo) > 0:
        doodoo.clear()
    
    while (i <= int(attempts)):
        doodoo.append(randthing())
        i += 1 
    s = 0
    x = 0
    xname = 0
    y = 0
    yname = 0
    z = 0
    zname = 0
    while (s <= 1001):

        if doodoo.count(s) > x:
            x = doodoo.count(s)
            xname = doodoo[doodoo.index(s)]
        elif doodoo.count(s) > y:
            y = doodoo.count(s)
            yname = doodoo[doodoo.index(s)]
        elif doodoo.count(s) > z:
            z = doodoo.count(s)
            zname = doodoo[doodoo.index(s)]

        s += 1
    # Optional File Writing (must change address)
   # filething = open("C:\\Games\\loler.txt", "w")
   # filething.write(str(doodoo))
   # filething.close()

    check = "nay"
    sleep(0.1)
    print("")
    print("Done!")
    print("\nMost Seen Number is " + str(xname) + " with a count of " + str(x))
    print("Second Most Seen Number is " + str(yname) + " with a count of " + str(y))
    print("Third Most Seen Number is " + str(zname) + " with a count of " + str(z))
    print("Mean is " + str((xname + yname + zname)/3))
    bruh = input("\nPress enter to close or R to restart\n")
    if bruh == "R":
        deez = "R"
    print("")
