from concurrent.futures import thread
from multiprocessing.connection import wait
from random import randint
from tabnanny import check
from time import sleep
from tracemalloc import start
from turtle import st
from xml.etree.ElementTree import tostring
import sys, time, threading

# Coin Flip Script
# This script flips a coin for an X amount of times
deez = "R"
while deez == "R":

    heads = 1
    tails = 0
    i = 0
    higheststreak = 0
    attempts = int(input("How many attempts would you like to flip the coin? (A Number)\n"))
    while (i <= attempts):
        streak = 0
        counter = 1
        while (counter == 1):
            if randint(0,1) == heads:
                streak += 1
            else:
                print("test " + str(i) + " had a streak of " + str(streak))
                counter = 0
        i += 1
        if (streak > higheststreak):
            higheststreak = streak
    print("Highest Streak was " + str(higheststreak))
    streakmath = 0.5 ** higheststreak
    streakpercent = streakmath * 100
    print("Chance of highest streak is " + str(streakpercent) + "%")
    i = 0
    higheststreak = 0
    bruh = input("\nPress enter to close or R to restart\n")
    if bruh == "R":
        deez = "R"
    print("")
