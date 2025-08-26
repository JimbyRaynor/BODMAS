# BODAS game in style of 7Seconds
import math
import sys
import os
import time
from tkinter import * 

sys.path.insert(0, "/home/deck/Documents") # needed to load LEDlib
import LEDlib

# for loading files (.png, .txt), set current directory = location of this python script (needed for Linux)
current_script_directory = os.path.dirname(os.path.abspath(__file__))
os.chdir(current_script_directory)

# TODO
# look at Algebra Tutorial 1
# add math animation in background for each symbol of walls
#       Same activity for 100 levels would be boring
#       -> Need new activities for Maths
# leave Math comments at end of each game
# BODMAS level: Use car to choose  * or + (with e.g. 2+3*7) 
# Mention this is easier to read than the equivalent 2+(3*7), and esp. expressions like 1+(1+(1+1)) 
# have fruit pickups to increase score
# score is increased per remaining time
# each level solves an equation. Show animation. Drive over steps in correct order, o/w fail.

STEPD = 4 # speed of car. This changes dx,dy.
MAXx = 800
MAXy = 600