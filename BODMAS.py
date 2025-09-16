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
# Use/Fix Level Editor
# fix gameloop for testing multiple collisions, + red, yellow, purple, white
# No an animations moving +,- etc. Does not help. Just leave 2+3=5, etc
# start with 1+(2+3) = (1+2)+3  associative law. Use "law" so we don't have to call it axiom or theorem
# talk about bodmas (b) and associative law at the same time
# have fruit bonuses (max 100) to have some "7Seconds" strategy
# level 0 demonstrates collecting red + before yellow +
# levels 1 to 10 have lots of simple instructions.
# ->> Real BODMAS/ALGEBRA starts at level 11 
# look at Algebra Tutorial 1
# collecting things (numbers, fruit) is fun
# build tools for LHS (level editor, etc)
# make a level inside a giant 3
# collect A, B, etc to evaluate A, B ,etc
# enemies chase car
# computer player also collects items: have two +s, one for each player. Race to finish first
# add math animation in background for each symbol of walls
#       Same activity for 100 levels would be boring
#       -> Need new activities for Maths
# Mention this is easier to read than the equivalent 2+(3*7), and esp. expressions like 1+(1+(1+1)) 
# Show how to evaluate nested brackets : 3*(1+(2/3))  read first ) then go left to first (
# distributive law a*(b+c) = a*b + a*c to simplify
# notice that distributive law depends on BODMAS. So do examples of all axioms
# can have levels with 2 expressions: 3*(7+9) and 3*7 + 3*9 with *(red), +(red), *(yellow), *(green), +(yellow)
# -1^2 = 1 (from Copilot, since BODMAS O says do exponentials first)
# have fruit pickups to increase score
# each level solves an equation. Show animation. Drive over steps in correct order, o/w fail.
# create lots of libraries to shorten code
# Level 1: design levels that remove blocks after "+" is collected so that all collections are automatically in order
#  i.e. enclose second "+" completely in blocks
# first try succesful bonus score
# help student memorise formulas/methods
# did you know? at end of each section
# have fuel/ pick up fuel? Go slow if run out of fuel
# use bejeweled style sounds for "good", "mission complete", etc
# have full instructions on screen at all times for new users
# change theme to space, change car to Space Shuttle, sparkly stars in background?
# ducks. Loose points for running over cute animals.

# execute CPU instructions to run program?
# try to make BONUS hard to get, like pinball

charRallyX = [(0,14,"#4C3A23"), (0,15,"#4C3A23"), (0,16,"#4C3A23"), (0,17,"#4C3A23"), (0,18,"#4C3A23"), (0,19,"#4C3A23"), (0,20,"#4C3A23"), (1,13,"#4C3A23"), (1,14,"#4C3A23"), (1,15,"#4C3A23"), (1,16,"#4C3A23"), (1,17,"#4C3A23"), (1,18,"#4C3A23"), (1,19,"#4C3A23"), (1,20,"#4C3A23"), (1,21,"#4C3A23"), (2,2,"#4C3A23"), (2,3,"#4C3A23"), (2,4,"#4C3A23"), (2,5,"#4C3A23"), (2,6,"#4C3A23"), (2,13,"#4C3A23"), (2,14,"#4C3A23"), (2,15,"#4C3A23"), (2,16,"#4C3A23"), (2,17,"#4C3A23"), (2,18,"#4C3A23"), (2,19,"#4C3A23"), (2,20,"#4C3A23"), (2,21,"#4C3A23"), (3,1,"#4C3A23"), (3,2,"#4C3A23"), (3,3,"#4C3A23"), (3,4,"#4C3A23"), (3,5,"#4C3A23"), (3,6,"#4C3A23"), (3,7,"#4C3A23"), (3,13,"#4C3A23"), (3,14,"#4C3A23"), (3,15,"#4C3A23"), (3,16,"#4C3A23"), (3,17,"#4C3A23"), (3,18,"#4C3A23"), (3,19,"#4C3A23"), (3,20,"#4C3A23"), (3,21,"#4C3A23"), (4,1,"#4C3A23"), (4,2,"#4C3A23"), (4,3,"#4C3A23"), (4,4,"#4C3A23"), (4,5,"#4C3A23"), (4,6,"#4C3A23"), (4,7,"#4C3A23"), (4,13,"#4C3A23"), (4,14,"#4C3A23"), (4,15,"#4C3A23"), (4,16,"#4C3A23"), (4,17,"#4C3A23"), (4,18,"#4C3A23"), (4,19,"#4C3A23"), (4,20,"#4C3A23"), (4,21,"#4C3A23"), (5,1,"#4C3A23"), (5,2,"#4C3A23"), (5,3,"#4C3A23"), (5,4,"#4C3A23"), (5,5,"#4C3A23"), (5,6,"#4C3A23"), (5,7,"#4C3A23"), (5,13,"#4C3A23"), (5,14,"#4C3A23"), (5,15,"#4C3A23"), (5,16,"#4C3A23"), (5,17,"#4C3A23"), (5,18,"#4C3A23"), (5,19,"#4C3A23"), (5,20,"#4C3A23"), (5,21,"#4C3A23"), (6,1,"#4C3A23"), (6,2,"#4C3A23"), (6,3,"#4C3A23"), (6,4,"#4C3A23"), (6,5,"#4C3A23"), (6,6,"#4C3A23"), (6,7,"#4C3A23"), (6,14,"#4C3A23"), (6,15,"#4C3A23"), (6,16,"#4C3A23"), (6,17,"#4C3A23"), (6,18,"#4C3A23"), (6,19,"#4C3A23"), (6,20,"#4C3A23"), (7,2,"#4C3A23"), (7,3,"#4C3A23"), (7,4,"#4C3A23"), (7,5,"#4C3A23"), (7,6,"#4C3A23"), (7,17,"#FFA07A"), (8,4,"#FFA07A"), (8,10,"#FFA07A"), (8,11,"#FFA07A"), (8,12,"#FFA07A"), (8,13,"#FFA07A"), (8,14,"#FFA07A"), (8,15,"#FFA07A"), (8,16,"#FFA07A"), (8,17,"#FFA07A"), (8,18,"#FFA07A"), (8,19,"#8B4513"), (8,20,"#8B4513"), (8,21,"#FF0000"), (8,22,"#FFFF00"), (8,23,"#FF0000"), (9,4,"#FFA07A"), (9,8,"#FFA07A"), (9,9,"#FFA07A"), (9,10,"#FFA07A"), (9,11,"#FFA07A"), (9,12,"#FFA07A"), (9,13,"#FFA07A"), (9,14,"#FFA07A"), (9,15,"#FFA07A"), (9,16,"#FFA07A"), (9,17,"#FFA07A"), (9,18,"#FFA07A"), (9,19,"#FFA07A"), (9,20,"#8B4513"), (9,21,"#8B4513"), (9,22,"#FF0000"), (9,23,"#FFFF00"), (10,1,"#FFA07A"), (10,2,"#FFA07A"), (10,3,"#FFA07A"), (10,4,"#FFA07A"), (10,5,"#FFA07A"), (10,6,"#FFA07A"), (10,7,"#FFA07A"), (10,8,"#FFA07A"), (10,9,"#FFA07A"), (10,10,"#FFA07A"), (10,11,"#AAAAAA"), (10,12,"#AAAAAA"), (10,13,"#AAAAAA"), (10,14,"#AAAAAA"), (10,15,"#AAAAAA"), (10,16,"#AAAAAA"), (10,17,"#FFA07A"), (10,18,"#FFA07A"), (10,19,"#FFA07A"), (10,20,"#FFA07A"), (11,0,"#FFA07A"), (11,1,"#FFA07A"), (11,2,"#FFA07A"), (11,3,"#FFA07A"), (11,4,"#FFA07A"), (11,5,"#FFA07A"), (11,6,"#FFA07A"), (11,7,"#FFA07A"), (11,8,"#FFA07A"), (11,9,"#FFA07A"), (11,10,"#AAAAAA"), (11,11,"#B5B3F5"), (11,12,"#FFFFFF"), (11,13,"#FFFFFF"), (11,14,"#FFFFFF"), (11,15,"#FFFFFF"), (11,16,"#B5B3F5"), (11,17,"#AAAAAA"), (11,18,"#FFA07A"), (11,19,"#FFA07A"), (11,20,"#FFA07A"), (12,0,"#FFA07A"), (12,1,"#FFA07A"), (12,2,"#FFA07A"), (12,3,"#FFA07A"), (12,4,"#FFA07A"), (12,5,"#FFA07A"), (12,6,"#FFA07A"), (12,7,"#FFA07A"), (12,8,"#FFA07A"), (12,9,"#FFA07A"), (12,10,"#AAAAAA"), (12,11,"#B5B3F5"), (12,12,"#FFFFFF"), (12,13,"#FFFFFF"), (12,14,"#FFFFFF"), (12,15,"#FFFFFF"), (12,16,"#B5B3F5"), (12,17,"#AAAAAA"), (12,18,"#FFA07A"), (12,19,"#FFA07A"), (12,20,"#FFA07A"), (13,1,"#FFA07A"), (13,2,"#FFA07A"), (13,3,"#FFA07A"), (13,4,"#FFA07A"), (13,5,"#FFA07A"), (13,6,"#FFA07A"), (13,7,"#FFA07A"), (13,8,"#FFA07A"), (13,9,"#FFA07A"), (13,10,"#FFA07A"), (13,11,"#AAAAAA"), (13,12,"#AAAAAA"), (13,13,"#AAAAAA"), (13,14,"#AAAAAA"), (13,15,"#AAAAAA"), (13,16,"#AAAAAA"), (13,17,"#FFA07A"), (13,18,"#FFA07A"), (13,19,"#FFA07A"), (13,20,"#FFA07A"), (14,4,"#FFA07A"), (14,8,"#FFA07A"), (14,9,"#FFA07A"), (14,10,"#FFA07A"), (14,11,"#FFA07A"), (14,12,"#FFA07A"), (14,13,"#FFA07A"), (14,14,"#FFA07A"), (14,15,"#FFA07A"), (14,16,"#FFA07A"), (14,17,"#FFA07A"), (14,18,"#FFA07A"), (14,19,"#FFA07A"), (14,20,"#8B4513"), (14,21,"#8B4513"), (14,22,"#FF0000"), (14,23,"#FFFF00"), (15,4,"#FFA07A"), (15,10,"#FFA07A"), (15,11,"#FFA07A"), (15,12,"#FFA07A"), (15,13,"#FFA07A"), (15,14,"#FFA07A"), (15,15,"#FFA07A"), (15,16,"#FFA07A"), (15,17,"#FFA07A"), (15,18,"#FFA07A"), (15,19,"#8B4513"), (15,20,"#8B4513"), (15,21,"#FF0000"), (15,22,"#FFFF00"), (15,23,"#FF0000"), (16,2,"#4C3A23"), (16,3,"#4C3A23"), (16,4,"#4C3A23"), (16,5,"#4C3A23"), (16,6,"#4C3A23"), (16,17,"#FFA07A"), (17,1,"#4C3A23"), (17,2,"#4C3A23"), (17,3,"#4C3A23"), (17,4,"#4C3A23"), (17,5,"#4C3A23"), (17,6,"#4C3A23"), (17,7,"#4C3A23"), (17,14,"#4C3A23"), (17,15,"#4C3A23"), (17,16,"#4C3A23"), (17,17,"#4C3A23"), (17,18,"#4C3A23"), (17,19,"#4C3A23"), (17,20,"#4C3A23"), (18,1,"#4C3A23"), (18,2,"#4C3A23"), (18,3,"#4C3A23"), (18,4,"#4C3A23"), (18,5,"#4C3A23"), (18,6,"#4C3A23"), (18,7,"#4C3A23"), (18,13,"#4C3A23"), (18,14,"#4C3A23"), (18,15,"#4C3A23"), (18,16,"#4C3A23"), (18,17,"#4C3A23"), (18,18,"#4C3A23"), (18,19,"#4C3A23"), (18,20,"#4C3A23"), (18,21,"#4C3A23"), (19,1,"#4C3A23"), (19,2,"#4C3A23"), (19,3,"#4C3A23"), (19,4,"#4C3A23"), (19,5,"#4C3A23"), (19,6,"#4C3A23"), (19,7,"#4C3A23"), (19,13,"#4C3A23"), (19,14,"#4C3A23"), (19,15,"#4C3A23"), (19,16,"#4C3A23"), (19,17,"#4C3A23"), (19,18,"#4C3A23"), (19,19,"#4C3A23"), (19,20,"#4C3A23"), (19,21,"#4C3A23"), (20,1,"#4C3A23"), (20,2,"#4C3A23"), (20,3,"#4C3A23"), (20,4,"#4C3A23"), (20,5,"#4C3A23"), (20,6,"#4C3A23"), (20,7,"#4C3A23"), (20,13,"#4C3A23"), (20,14,"#4C3A23"), (20,15,"#4C3A23"), (20,16,"#4C3A23"), (20,17,"#4C3A23"), (20,18,"#4C3A23"), (20,19,"#4C3A23"), (20,20,"#4C3A23"), (20,21,"#4C3A23"), (21,2,"#4C3A23"), (21,3,"#4C3A23"), (21,4,"#4C3A23"), (21,5,"#4C3A23"), (21,6,"#4C3A23"), (21,13,"#4C3A23"), (21,14,"#4C3A23"), (21,15,"#4C3A23"), (21,16,"#4C3A23"), (21,17,"#4C3A23"), (21,18,"#4C3A23"), (21,19,"#4C3A23"), (21,20,"#4C3A23"), (21,21,"#4C3A23"), (22,13,"#4C3A23"), (22,14,"#4C3A23"), (22,15,"#4C3A23"), (22,16,"#4C3A23"), (22,17,"#4C3A23"), (22,18,"#4C3A23"), (22,19,"#4C3A23"), (22,20,"#4C3A23"), (22,21,"#4C3A23"), (23,14,"#4C3A23"), (23,15,"#4C3A23"), (23,16,"#4C3A23"), (23,17,"#4C3A23"), (23,18,"#4C3A23"), (23,19,"#4C3A23"), (23,20,"#4C3A23")]
charPopsicle = [(0,1,"#8B4513"), (0,2,"#8B4513"), (0,3,"#8B4513"), (0,4,"#8B4513"), (0,5,"#8B4513"), (0,6,"#8B4513"), (0,7,"#8B4513"), (0,8,"#8B4513"), (0,9,"#8B4513"), (0,10,"#8B4513"), (0,11,"#8B4513"), (1,0,"#8B4513"), (1,1,"#8B4513"), (1,2,"#FFFFFF"), (1,3,"#FFFFFF"), (1,4,"#FFFFFF"), (1,5,"#8B4513"), (1,6,"#8B4513"), (1,7,"#8B4513"), (1,8,"#8B4513"), (1,9,"#8B4513"), (1,10,"#8B4513"), (1,11,"#FFFFFF"), (1,12,"#FFFFFF"), (2,0,"#8B4513"), (2,1,"#8B4513"), (2,2,"#8B4513"), (2,3,"#8B4513"), (2,4,"#8B4513"), (2,5,"#8B4513"), (2,6,"#8B4513"), (2,7,"#8B4513"), (2,8,"#8B4513"), (2,9,"#8B4513"), (2,10,"#8B4513"), (2,11,"#8B4513"), (2,12,"#FFFFFF"), (3,0,"#8B4513"), (3,1,"#8B4513"), (3,2,"#8B4513"), (3,3,"#8B4513"), (3,4,"#8B4513"), (3,5,"#8B4513"), (3,6,"#8B4513"), (3,7,"#8B4513"), (3,8,"#8B4513"), (3,9,"#8B4513"), (3,10,"#8B4513"), (3,11,"#FFFFFF"), (3,12,"#FFFFFF"), (3,13,"#C19153"), (3,14,"#C19153"), (3,15,"#C19153"), (3,16,"#C19153"), (3,17,"#C19153"), (4,0,"#8B4513"), (4,1,"#8B4513"), (4,2,"#8B4513"), (4,3,"#8B4513"), (4,4,"#8B4513"), (4,5,"#8B4513"), (4,6,"#8B4513"), (4,7,"#8B4513"), (4,8,"#8B4513"), (4,9,"#8B4513"), (4,10,"#8B4513"), (4,11,"#8B4513"), (4,12,"#FFFFFF"), (4,13,"#C19153"), (4,14,"#C19153"), (4,15,"#C19153"), (4,16,"#C19153"), (4,17,"#C19153"), (5,0,"#8B4513"), (5,1,"#8B4513"), (5,2,"#8B4513"), (5,3,"#8B4513"), (5,4,"#8B4513"), (5,5,"#8B4513"), (5,6,"#8B4513"), (5,7,"#8B4513"), (5,8,"#8B4513"), (5,9,"#8B4513"), (5,10,"#8B4513"), (5,11,"#8B4513"), (5,12,"#FFFFFF"), (6,0,"#8B4513"), (6,1,"#8B4513"), (6,2,"#8B4513"), (6,3,"#8B4513"), (6,4,"#8B4513"), (6,5,"#8B4513"), (6,6,"#8B4513"), (6,7,"#8B4513"), (6,8,"#8B4513"), (6,9,"#8B4513"), (6,10,"#8B4513"), (6,11,"#FFFFFF"), (6,12,"#FFFFFF"), (7,1,"#8B4513"), (7,2,"#8B4513"), (7,3,"#8B4513"), (7,4,"#8B4513"), (7,5,"#8B4513"), (7,6,"#8B4513"), (7,7,"#8B4513"), (7,8,"#8B4513"), (7,9,"#8B4513"), (7,10,"#8B4513"), (7,11,"#8B4513")]
charPacmanStrawberry = [(0,6,"#FF0000"), (0,7,"#FF0000"), (0,8,"#FF0000"), (0,9,"#FF0000"), (1,5,"#FF0000"), (1,6,"#FF0000"), (1,7,"#FFFFFF"), (1,8,"#FF0000"), (1,9,"#FF0000"), (1,10,"#FF0000"), (1,11,"#FF0000"), (2,4,"#279627"), (2,5,"#FF0000"), (2,6,"#FF0000"), (2,7,"#FF0000"), (2,8,"#FF0000"), (2,9,"#FF0000"), (2,10,"#FFFFFF"), (2,11,"#FF0000"), (2,12,"#FF0000"), (3,4,"#279627"), (3,5,"#279627"), (3,6,"#FF0000"), (3,7,"#FF0000"), (3,8,"#FFFFFF"), (3,9,"#FF0000"), (3,10,"#FF0000"), (3,11,"#FF0000"), (3,12,"#FF0000"), (3,13,"#FF0000"), (4,4,"#279627"), (4,5,"#279627"), (4,6,"#FF0000"), (4,7,"#FF0000"), (4,8,"#FF0000"), (4,9,"#FF0000"), (4,10,"#FF0000"), (4,11,"#FF0000"), (4,12,"#FFFFFF"), (4,13,"#FF0000"), (5,3,"#FFFFFF"), (5,4,"#FFFFFF"), (5,5,"#279627"), (5,6,"#279627"), (5,7,"#FF0000"), (5,8,"#FFFFFF"), (5,9,"#FF0000"), (5,10,"#FFFFFF"), (5,11,"#FF0000"), (5,12,"#FF0000"), (5,13,"#FF0000"), (5,14,"#FF0000"), (6,4,"#279627"), (6,5,"#279627"), (6,6,"#FF0000"), (6,7,"#FF0000"), (6,8,"#FF0000"), (6,9,"#FF0000"), (6,10,"#FF0000"), (6,11,"#FF0000"), (6,12,"#FF0000"), (6,13,"#FF0000"), (7,4,"#279627"), (7,5,"#279627"), (7,6,"#FF0000"), (7,7,"#FFFFFF"), (7,8,"#FF0000"), (7,9,"#FF0000"), (7,10,"#FF0000"), (7,11,"#FF0000"), (7,12,"#FFFFFF"), (7,13,"#FF0000"), (8,4,"#279627"), (8,5,"#FF0000"), (8,6,"#FF0000"), (8,7,"#FF0000"), (8,8,"#FF0000"), (8,9,"#FFFFFF"), (8,10,"#FF0000"), (8,11,"#FF0000"), (9,5,"#FF0000"), (9,6,"#FFFFFF"), (9,7,"#FF0000"), (9,8,"#FF0000"), (9,9,"#FF0000"), (9,10,"#FF0000"), (9,11,"#FF0000"), (10,6,"#FF0000"), (10,7,"#FF0000"), (10,8,"#FF0000"), (10,9,"#FF0000")]

charYellowPlus = [(6,6,"#90EE90"), (6,8,"#90EE90"), (6,10,"#90EE90"), (6,12,"#90EE90"), (6,14,"#90EE90"), (6,16,"#90EE90"), (8,6,"#90EE90"), (8,16,"#90EE90"), (9,11,"#FFFF00"), (10,6,"#90EE90"), (10,11,"#FFFF00"), (10,16,"#90EE90"), (11,9,"#FFFF00"), (11,10,"#FFFF00"), (11,11,"#FFFF00"), (11,12,"#FFFF00"), (11,13,"#FFFF00"), (12,6,"#90EE90"), (12,11,"#FFFF00"), (12,16,"#90EE90"), (13,11,"#FFFF00"), (14,6,"#90EE90"), (14,16,"#90EE90"), (16,6,"#90EE90"), (16,8,"#90EE90"), (16,10,"#90EE90"), (16,12,"#90EE90"), (16,14,"#90EE90"), (16,16,"#90EE90")]
charRedPlus = [(6,6,"#90EE90"), (6,8,"#90EE90"), (6,10,"#90EE90"), (6,12,"#90EE90"), (6,14,"#90EE90"), (6,16,"#90EE90"), (8,6,"#90EE90"), (8,16,"#90EE90"), (9,11,"#FF0000"), (10,6,"#90EE90"), (10,11,"#FF0000"), (10,16,"#90EE90"), (11,9,"#FF0000"), (11,10,"#FF0000"), (11,11,"#FF0000"), (11,12,"#FF0000"), (11,13,"#FF0000"), (12,6,"#90EE90"), (12,11,"#FF0000"), (12,16,"#90EE90"), (13,11,"#FF0000"), (14,6,"#90EE90"), (14,16,"#90EE90"), (16,6,"#90EE90"), (16,8,"#90EE90"), (16,10,"#90EE90"), (16,12,"#90EE90"), (16,14,"#90EE90"), (16,16,"#90EE90")]
charWhitePlus = [(6,6,"#90EE90"), (6,8,"#90EE90"), (6,10,"#90EE90"), (6,12,"#90EE90"), (6,14,"#90EE90"), (6,16,"#90EE90"), (8,6,"#90EE90"), (8,16,"#90EE90"), (9,11,"#FFFFFF"), (10,6,"#90EE90"), (10,11,"#FFFFFF"), (10,16,"#90EE90"), (11,9,"#FFFFFF"), (11,10,"#FFFFFF"), (11,11,"#FFFFFF"), (11,12,"#FFFFFF"), (11,13,"#FFFFFF"), (12,6,"#90EE90"), (12,11,"#FFFFFF"), (12,16,"#90EE90"), (13,11,"#FFFFFF"), (14,6,"#90EE90"), (14,16,"#90EE90"), (16,6,"#90EE90"), (16,8,"#90EE90"), (16,10,"#90EE90"), (16,12,"#90EE90"), (16,14,"#90EE90"), (16,16,"#90EE90")] 
charPurplePlus = [(6,6,"#90EE90"), (6,8,"#90EE90"), (6,10,"#90EE90"), (6,12,"#90EE90"), (6,14,"#90EE90"), (6,16,"#90EE90"), (8,6,"#90EE90"), (8,16,"#90EE90"), (9,11,"#BE1CBE"), (10,6,"#90EE90"), (10,11,"#BE1CBE"), (10,16,"#90EE90"), (11,9,"#BE1CBE"), (11,10,"#BE1CBE"), (11,11,"#BE1CBE"), (11,12,"#BE1CBE"), (11,13,"#BE1CBE"), (12,6,"#90EE90"), (12,11,"#BE1CBE"), (12,16,"#90EE90"), (13,11,"#BE1CBE"), (14,6,"#90EE90"), (14,16,"#90EE90"), (16,6,"#90EE90"), (16,8,"#90EE90"), (16,10,"#90EE90"), (16,12,"#90EE90"), (16,14,"#90EE90"), (16,16,"#90EE90")] 

charWall = [(0,2,"#FFFFFF"), (0,3,"#FFFFFF"), (0,4,"#FFFFFF"), (0,5,"#FFFFFF"), (0,6,"#FFFFFF"), (0,7,"#FFFFFF"), (0,8,"#FFFFFF"), (0,9,"#FFFFFF"), (0,10,"#FFFFFF"), (0,11,"#FFFFFF"), (0,12,"#FFFFFF"), (0,13,"#FFFFFF"), (0,14,"#FFFFFF"), (0,15,"#FFFFFF"), (0,16,"#FFFFFF"), (0,17,"#FFFFFF"), (0,18,"#FFFFFF"), (0,19,"#FFFFFF"), (0,20,"#FFFFFF"), (0,21,"#FFFFFF"), (1,1,"#FFFFFF"), (1,2,"#B5B3F5"), (1,3,"#B5B3F5"), (1,4,"#B5B3F5"), (1,5,"#B5B3F5"), (1,6,"#B5B3F5"), (1,7,"#B5B3F5"), (1,8,"#B5B3F5"), (1,9,"#B5B3F5"), (1,10,"#B5B3F5"), (1,11,"#B5B3F5"), (1,12,"#B5B3F5"), (1,13,"#B5B3F5"), (1,14,"#B5B3F5"), (1,15,"#B5B3F5"), (1,16,"#B5B3F5"), (1,17,"#B5B3F5"), (1,18,"#B5B3F5"), (1,19,"#B5B3F5"), (1,20,"#B5B3F5"), (1,21,"#B5B3F5"), (1,22,"#FFFFFF"), (2,0,"#FFFFFF"), (2,1,"#B5B3F5"), (2,2,"#B5B3F5"), (2,3,"#B5B3F5"), (2,4,"#B5B3F5"), (2,5,"#B5B3F5"), (2,6,"#B5B3F5"), (2,7,"#B5B3F5"), (2,8,"#B5B3F5"), (2,9,"#B5B3F5"), (2,10,"#B5B3F5"), (2,11,"#B5B3F5"), (2,12,"#B5B3F5"), (2,13,"#B5B3F5"), (2,14,"#B5B3F5"), (2,15,"#B5B3F5"), (2,16,"#B5B3F5"), (2,17,"#B5B3F5"), (2,18,"#B5B3F5"), (2,19,"#B5B3F5"), (2,20,"#B5B3F5"), (2,21,"#B5B3F5"), (2,22,"#B5B3F5"), (2,23,"#FFFFFF"), (3,0,"#FFFFFF"), (3,1,"#B5B3F5"), (3,2,"#B5B3F5"), (3,3,"#B5B3F5"), (3,4,"#B5B3F5"), (3,5,"#B5B3F5"), (3,6,"#B5B3F5"), (3,7,"#B5B3F5"), (3,8,"#B5B3F5"), (3,9,"#B5B3F5"), (3,10,"#B5B3F5"), (3,11,"#B5B3F5"), (3,12,"#B5B3F5"), (3,13,"#B5B3F5"), (3,14,"#B5B3F5"), (3,15,"#B5B3F5"), (3,16,"#B5B3F5"), (3,17,"#B5B3F5"), (3,18,"#B5B3F5"), (3,19,"#B5B3F5"), (3,20,"#B5B3F5"), (3,21,"#B5B3F5"), (3,22,"#B5B3F5"), (3,23,"#FFFFFF"), (4,0,"#FFFFFF"), (4,1,"#B5B3F5"), (4,2,"#B5B3F5"), (4,3,"#B5B3F5"), (4,4,"#B5B3F5"), (4,5,"#B5B3F5"), (4,6,"#B5B3F5"), (4,7,"#B5B3F5"), (4,8,"#B5B3F5"), (4,9,"#B5B3F5"), (4,10,"#B5B3F5"), (4,11,"#B5B3F5"), (4,12,"#B5B3F5"), (4,13,"#B5B3F5"), (4,14,"#B5B3F5"), (4,15,"#B5B3F5"), (4,16,"#B5B3F5"), (4,17,"#B5B3F5"), (4,18,"#B5B3F5"), (4,19,"#B5B3F5"), (4,20,"#B5B3F5"), (4,21,"#B5B3F5"), (4,22,"#B5B3F5"), (4,23,"#FFFFFF"), (5,0,"#FFFFFF"), (5,1,"#B5B3F5"), (5,2,"#B5B3F5"), (5,3,"#B5B3F5"), (5,4,"#B5B3F5"), (5,5,"#B5B3F5"), (5,6,"#B5B3F5"), (5,7,"#B5B3F5"), (5,8,"#B5B3F5"), (5,9,"#B5B3F5"), (5,10,"#B5B3F5"), (5,11,"#B5B3F5"), (5,12,"#B5B3F5"), (5,13,"#B5B3F5"), (5,14,"#B5B3F5"), (5,15,"#B5B3F5"), (5,16,"#B5B3F5"), (5,17,"#B5B3F5"), (5,18,"#B5B3F5"), (5,19,"#B5B3F5"), (5,20,"#B5B3F5"), (5,21,"#B5B3F5"), (5,22,"#B5B3F5"), (5,23,"#FFFFFF"), (6,0,"#FFFFFF"), (6,1,"#B5B3F5"), (6,2,"#B5B3F5"), (6,3,"#B5B3F5"), (6,4,"#B5B3F5"), (6,5,"#B5B3F5"), (6,6,"#B5B3F5"), (6,7,"#B5B3F5"), (6,8,"#B5B3F5"), (6,9,"#B5B3F5"), (6,10,"#B5B3F5"), (6,11,"#B5B3F5"), (6,12,"#B5B3F5"), (6,13,"#B5B3F5"), (6,14,"#B5B3F5"), (6,15,"#B5B3F5"), (6,16,"#B5B3F5"), (6,17,"#B5B3F5"), (6,18,"#B5B3F5"), (6,19,"#B5B3F5"), (6,20,"#B5B3F5"), (6,21,"#B5B3F5"), (6,22,"#B5B3F5"), (6,23,"#FFFFFF"), (7,0,"#FFFFFF"), (7,1,"#B5B3F5"), (7,2,"#B5B3F5"), (7,3,"#B5B3F5"), (7,4,"#B5B3F5"), (7,5,"#B5B3F5"), (7,6,"#B5B3F5"), (7,7,"#B5B3F5"), (7,8,"#B5B3F5"), (7,9,"#B5B3F5"), (7,10,"#B5B3F5"), (7,11,"#B5B3F5"), (7,12,"#B5B3F5"), (7,13,"#B5B3F5"), (7,14,"#B5B3F5"), (7,15,"#B5B3F5"), (7,16,"#B5B3F5"), (7,17,"#B5B3F5"), (7,18,"#B5B3F5"), (7,19,"#B5B3F5"), (7,20,"#B5B3F5"), (7,21,"#B5B3F5"), (7,22,"#B5B3F5"), (7,23,"#FFFFFF"), (8,0,"#FFFFFF"), (8,1,"#B5B3F5"), (8,2,"#B5B3F5"), (8,3,"#B5B3F5"), (8,4,"#B5B3F5"), (8,5,"#B5B3F5"), (8,6,"#B5B3F5"), (8,7,"#B5B3F5"), (8,8,"#B5B3F5"), (8,9,"#B5B3F5"), (8,10,"#B5B3F5"), (8,11,"#B5B3F5"), (8,12,"#B5B3F5"), (8,13,"#B5B3F5"), (8,14,"#B5B3F5"), (8,15,"#B5B3F5"), (8,16,"#B5B3F5"), (8,17,"#B5B3F5"), (8,18,"#B5B3F5"), (8,19,"#B5B3F5"), (8,20,"#B5B3F5"), (8,21,"#B5B3F5"), (8,22,"#B5B3F5"), (8,23,"#FFFFFF"), (9,0,"#FFFFFF"), (9,1,"#B5B3F5"), (9,2,"#B5B3F5"), (9,3,"#B5B3F5"), (9,4,"#B5B3F5"), (9,5,"#B5B3F5"), (9,6,"#B5B3F5"), (9,7,"#B5B3F5"), (9,8,"#B5B3F5"), (9,9,"#B5B3F5"), (9,10,"#B5B3F5"), (9,11,"#B5B3F5"), (9,12,"#B5B3F5"), (9,13,"#B5B3F5"), (9,14,"#B5B3F5"), (9,15,"#B5B3F5"), (9,16,"#B5B3F5"), (9,17,"#B5B3F5"), (9,18,"#B5B3F5"), (9,19,"#B5B3F5"), (9,20,"#B5B3F5"), (9,21,"#B5B3F5"), (9,22,"#B5B3F5"), (9,23,"#FFFFFF"), (10,0,"#FFFFFF"), (10,1,"#B5B3F5"), (10,2,"#B5B3F5"), (10,3,"#B5B3F5"), (10,4,"#B5B3F5"), (10,5,"#B5B3F5"), (10,6,"#B5B3F5"), (10,7,"#B5B3F5"), (10,8,"#B5B3F5"), (10,9,"#B5B3F5"), (10,10,"#B5B3F5"), (10,11,"#B5B3F5"), (10,12,"#B5B3F5"), (10,13,"#B5B3F5"), (10,14,"#B5B3F5"), (10,15,"#B5B3F5"), (10,16,"#B5B3F5"), (10,17,"#B5B3F5"), (10,18,"#B5B3F5"), (10,19,"#B5B3F5"), (10,20,"#B5B3F5"), (10,21,"#B5B3F5"), (10,22,"#B5B3F5"), (10,23,"#FFFFFF"), (11,0,"#FFFFFF"), (11,1,"#B5B3F5"), (11,2,"#B5B3F5"), (11,3,"#B5B3F5"), (11,4,"#B5B3F5"), (11,5,"#B5B3F5"), (11,6,"#B5B3F5"), (11,7,"#B5B3F5"), (11,8,"#B5B3F5"), (11,9,"#B5B3F5"), (11,10,"#B5B3F5"), (11,11,"#B5B3F5"), (11,12,"#B5B3F5"), (11,13,"#B5B3F5"), (11,14,"#B5B3F5"), (11,15,"#B5B3F5"), (11,16,"#B5B3F5"), (11,17,"#B5B3F5"), (11,18,"#B5B3F5"), (11,19,"#B5B3F5"), (11,20,"#B5B3F5"), (11,21,"#B5B3F5"), (11,22,"#B5B3F5"), (11,23,"#FFFFFF"), (12,0,"#FFFFFF"), (12,1,"#B5B3F5"), (12,2,"#B5B3F5"), (12,3,"#B5B3F5"), (12,4,"#B5B3F5"), (12,5,"#B5B3F5"), (12,6,"#B5B3F5"), (12,7,"#B5B3F5"), (12,8,"#B5B3F5"), (12,9,"#B5B3F5"), (12,10,"#B5B3F5"), (12,11,"#B5B3F5"), (12,12,"#B5B3F5"), (12,13,"#B5B3F5"), (12,14,"#B5B3F5"), (12,15,"#B5B3F5"), (12,16,"#B5B3F5"), (12,17,"#B5B3F5"), (12,18,"#B5B3F5"), (12,19,"#B5B3F5"), (12,20,"#B5B3F5"), (12,21,"#B5B3F5"), (12,22,"#B5B3F5"), (12,23,"#FFFFFF"), (13,0,"#FFFFFF"), (13,1,"#B5B3F5"), (13,2,"#B5B3F5"), (13,3,"#B5B3F5"), (13,4,"#B5B3F5"), (13,5,"#B5B3F5"), (13,6,"#B5B3F5"), (13,7,"#B5B3F5"), (13,8,"#B5B3F5"), (13,9,"#B5B3F5"), (13,10,"#B5B3F5"), (13,11,"#B5B3F5"), (13,12,"#B5B3F5"), (13,13,"#B5B3F5"), (13,14,"#B5B3F5"), (13,15,"#B5B3F5"), (13,16,"#B5B3F5"), (13,17,"#B5B3F5"), (13,18,"#B5B3F5"), (13,19,"#B5B3F5"), (13,20,"#B5B3F5"), (13,21,"#B5B3F5"), (13,22,"#B5B3F5"), (13,23,"#FFFFFF"), (14,0,"#FFFFFF"), (14,1,"#B5B3F5"), (14,2,"#B5B3F5"), (14,3,"#B5B3F5"), (14,4,"#B5B3F5"), (14,5,"#B5B3F5"), (14,6,"#B5B3F5"), (14,7,"#B5B3F5"), (14,8,"#B5B3F5"), (14,9,"#B5B3F5"), (14,10,"#B5B3F5"), (14,11,"#B5B3F5"), (14,12,"#B5B3F5"), (14,13,"#B5B3F5"), (14,14,"#B5B3F5"), (14,15,"#B5B3F5"), (14,16,"#B5B3F5"), (14,17,"#B5B3F5"), (14,18,"#B5B3F5"), (14,19,"#B5B3F5"), (14,20,"#B5B3F5"), (14,21,"#B5B3F5"), (14,22,"#B5B3F5"), (14,23,"#FFFFFF"), (15,0,"#FFFFFF"), (15,1,"#B5B3F5"), (15,2,"#B5B3F5"), (15,3,"#B5B3F5"), (15,4,"#B5B3F5"), (15,5,"#B5B3F5"), (15,6,"#B5B3F5"), (15,7,"#B5B3F5"), (15,8,"#B5B3F5"), (15,9,"#B5B3F5"), (15,10,"#B5B3F5"), (15,11,"#B5B3F5"), (15,12,"#B5B3F5"), (15,13,"#B5B3F5"), (15,14,"#B5B3F5"), (15,15,"#B5B3F5"), (15,16,"#B5B3F5"), (15,17,"#B5B3F5"), (15,18,"#B5B3F5"), (15,19,"#B5B3F5"), (15,20,"#B5B3F5"), (15,21,"#B5B3F5"), (15,22,"#B5B3F5"), (15,23,"#FFFFFF"), (16,0,"#FFFFFF"), (16,1,"#B5B3F5"), (16,2,"#B5B3F5"), (16,3,"#B5B3F5"), (16,4,"#B5B3F5"), (16,5,"#B5B3F5"), (16,6,"#B5B3F5"), (16,7,"#B5B3F5"), (16,8,"#B5B3F5"), (16,9,"#B5B3F5"), (16,10,"#B5B3F5"), (16,11,"#B5B3F5"), (16,12,"#B5B3F5"), (16,13,"#B5B3F5"), (16,14,"#B5B3F5"), (16,15,"#B5B3F5"), (16,16,"#B5B3F5"), (16,17,"#B5B3F5"), (16,18,"#B5B3F5"), (16,19,"#B5B3F5"), (16,20,"#B5B3F5"), (16,21,"#B5B3F5"), (16,22,"#B5B3F5"), (16,23,"#FFFFFF"), (17,0,"#FFFFFF"), (17,1,"#B5B3F5"), (17,2,"#B5B3F5"), (17,3,"#B5B3F5"), (17,4,"#B5B3F5"), (17,5,"#B5B3F5"), (17,6,"#B5B3F5"), (17,7,"#B5B3F5"), (17,8,"#B5B3F5"), (17,9,"#B5B3F5"), (17,10,"#B5B3F5"), (17,11,"#B5B3F5"), (17,12,"#B5B3F5"), (17,13,"#B5B3F5"), (17,14,"#B5B3F5"), (17,15,"#B5B3F5"), (17,16,"#B5B3F5"), (17,17,"#B5B3F5"), (17,18,"#B5B3F5"), (17,19,"#B5B3F5"), (17,20,"#B5B3F5"), (17,21,"#B5B3F5"), (17,22,"#B5B3F5"), (17,23,"#FFFFFF"), (18,0,"#FFFFFF"), (18,1,"#B5B3F5"), (18,2,"#B5B3F5"), (18,3,"#B5B3F5"), (18,4,"#B5B3F5"), (18,5,"#B5B3F5"), (18,6,"#B5B3F5"), (18,7,"#B5B3F5"), (18,8,"#B5B3F5"), (18,9,"#B5B3F5"), (18,10,"#B5B3F5"), (18,11,"#B5B3F5"), (18,12,"#B5B3F5"), (18,13,"#B5B3F5"), (18,14,"#B5B3F5"), (18,15,"#B5B3F5"), (18,16,"#B5B3F5"), (18,17,"#B5B3F5"), (18,18,"#B5B3F5"), (18,19,"#B5B3F5"), (18,20,"#B5B3F5"), (18,21,"#B5B3F5"), (18,22,"#B5B3F5"), (18,23,"#FFFFFF"), (19,0,"#FFFFFF"), (19,1,"#B5B3F5"), (19,2,"#B5B3F5"), (19,3,"#B5B3F5"), (19,4,"#B5B3F5"), (19,5,"#B5B3F5"), (19,6,"#B5B3F5"), (19,7,"#B5B3F5"), (19,8,"#B5B3F5"), (19,9,"#B5B3F5"), (19,10,"#B5B3F5"), (19,11,"#B5B3F5"), (19,12,"#B5B3F5"), (19,13,"#B5B3F5"), (19,14,"#B5B3F5"), (19,15,"#B5B3F5"), (19,16,"#B5B3F5"), (19,17,"#B5B3F5"), (19,18,"#B5B3F5"), (19,19,"#B5B3F5"), (19,20,"#B5B3F5"), (19,21,"#B5B3F5"), (19,22,"#B5B3F5"), (19,23,"#FFFFFF"), (20,0,"#FFFFFF"), (20,1,"#B5B3F5"), (20,2,"#B5B3F5"), (20,3,"#B5B3F5"), (20,4,"#B5B3F5"), (20,5,"#B5B3F5"), (20,6,"#B5B3F5"), (20,7,"#B5B3F5"), (20,8,"#B5B3F5"), (20,9,"#B5B3F5"), (20,10,"#B5B3F5"), (20,11,"#B5B3F5"), (20,12,"#B5B3F5"), (20,13,"#B5B3F5"), (20,14,"#B5B3F5"), (20,15,"#B5B3F5"), (20,16,"#B5B3F5"), (20,17,"#B5B3F5"), (20,18,"#B5B3F5"), (20,19,"#B5B3F5"), (20,20,"#B5B3F5"), (20,21,"#B5B3F5"), (20,22,"#B5B3F5"), (20,23,"#FFFFFF"), (21,0,"#FFFFFF"), (21,1,"#B5B3F5"), (21,2,"#B5B3F5"), (21,3,"#B5B3F5"), (21,4,"#B5B3F5"), (21,5,"#B5B3F5"), (21,6,"#B5B3F5"), (21,7,"#B5B3F5"), (21,8,"#B5B3F5"), (21,9,"#B5B3F5"), (21,10,"#B5B3F5"), (21,11,"#B5B3F5"), (21,12,"#B5B3F5"), (21,13,"#B5B3F5"), (21,14,"#B5B3F5"), (21,15,"#B5B3F5"), (21,16,"#B5B3F5"), (21,17,"#B5B3F5"), (21,18,"#B5B3F5"), (21,19,"#B5B3F5"), (21,20,"#B5B3F5"), (21,21,"#B5B3F5"), (21,22,"#B5B3F5"), (21,23,"#FFFFFF"), (22,1,"#FFFFFF"), (22,2,"#B5B3F5"), (22,3,"#B5B3F5"), (22,4,"#B5B3F5"), (22,5,"#B5B3F5"), (22,6,"#B5B3F5"), (22,7,"#B5B3F5"), (22,8,"#B5B3F5"), (22,9,"#B5B3F5"), (22,10,"#B5B3F5"), (22,11,"#B5B3F5"), (22,12,"#B5B3F5"), (22,13,"#B5B3F5"), (22,14,"#B5B3F5"), (22,15,"#B5B3F5"), (22,16,"#B5B3F5"), (22,17,"#B5B3F5"), (22,18,"#B5B3F5"), (22,19,"#B5B3F5"), (22,20,"#B5B3F5"), (22,21,"#B5B3F5"), (22,22,"#FFFFFF"), (23,2,"#FFFFFF"), (23,3,"#FFFFFF"), (23,4,"#FFFFFF"), (23,5,"#FFFFFF"), (23,6,"#FFFFFF"), (23,7,"#FFFFFF"), (23,8,"#FFFFFF"), (23,9,"#FFFFFF"), (23,10,"#FFFFFF"), (23,11,"#FFFFFF"), (23,12,"#FFFFFF"), (23,13,"#FFFFFF"), (23,14,"#FFFFFF"), (23,15,"#FFFFFF"), (23,16,"#FFFFFF"), (23,17,"#FFFFFF"), (23,18,"#FFFFFF"), (23,19,"#FFFFFF"), (23,20,"#FFFFFF"), (23,21,"#FFFFFF")]
charWall2 = [(4,6,"#FFFFFF"), (4,7,"#FFFFFF"), (4,8,"#FFFFFF"), (4,9,"#FFFFFF"), (4,10,"#FFFFFF"), (4,11,"#FFFFFF"), (4,12,"#FFFFFF"), (4,13,"#FFFFFF"), (4,14,"#FFFFFF"), (4,15,"#FFFFFF"), (4,16,"#FFFFFF"), (4,17,"#FFFFFF"), (5,5,"#FFFFFF"), (5,6,"#B5B3F5"), (5,7,"#B5B3F5"), (5,8,"#B5B3F5"), (5,9,"#B5B3F5"), (5,10,"#B5B3F5"), (5,11,"#B5B3F5"), (5,12,"#B5B3F5"), (5,13,"#B5B3F5"), (5,14,"#B5B3F5"), (5,15,"#B5B3F5"), (5,16,"#B5B3F5"), (5,17,"#B5B3F5"), (5,18,"#FFFFFF"), (6,4,"#FFFFFF"), (6,5,"#B5B3F5"), (6,6,"#B5B3F5"), (6,7,"#B5B3F5"), (6,8,"#B5B3F5"), (6,9,"#B5B3F5"), (6,10,"#B5B3F5"), (6,11,"#B5B3F5"), (6,12,"#B5B3F5"), (6,13,"#B5B3F5"), (6,14,"#B5B3F5"), (6,15,"#B5B3F5"), (6,16,"#B5B3F5"), (6,17,"#B5B3F5"), (6,18,"#B5B3F5"), (6,19,"#FFFFFF"), (7,4,"#FFFFFF"), (7,5,"#B5B3F5"), (7,6,"#B5B3F5"), (7,7,"#B5B3F5"), (7,8,"#B5B3F5"), (7,9,"#B5B3F5"), (7,10,"#B5B3F5"), (7,11,"#B5B3F5"), (7,12,"#B5B3F5"), (7,13,"#B5B3F5"), (7,14,"#B5B3F5"), (7,15,"#B5B3F5"), (7,16,"#B5B3F5"), (7,17,"#B5B3F5"), (7,18,"#B5B3F5"), (7,19,"#FFFFFF"), (8,4,"#FFFFFF"), (8,5,"#B5B3F5"), (8,6,"#B5B3F5"), (8,7,"#B5B3F5"), (8,8,"#B5B3F5"), (8,9,"#B5B3F5"), (8,10,"#B5B3F5"), (8,11,"#B5B3F5"), (8,12,"#B5B3F5"), (8,13,"#B5B3F5"), (8,14,"#B5B3F5"), (8,15,"#B5B3F5"), (8,16,"#B5B3F5"), (8,17,"#B5B3F5"), (8,18,"#B5B3F5"), (8,19,"#FFFFFF"), (9,4,"#FFFFFF"), (9,5,"#B5B3F5"), (9,6,"#B5B3F5"), (9,7,"#B5B3F5"), (9,8,"#B5B3F5"), (9,9,"#B5B3F5"), (9,10,"#B5B3F5"), (9,11,"#B5B3F5"), (9,12,"#B5B3F5"), (9,13,"#B5B3F5"), (9,14,"#B5B3F5"), (9,15,"#B5B3F5"), (9,16,"#B5B3F5"), (9,17,"#B5B3F5"), (9,18,"#B5B3F5"), (9,19,"#FFFFFF"), (10,4,"#FFFFFF"), (10,5,"#B5B3F5"), (10,6,"#B5B3F5"), (10,7,"#B5B3F5"), (10,8,"#B5B3F5"), (10,9,"#B5B3F5"), (10,10,"#B5B3F5"), (10,11,"#B5B3F5"), (10,12,"#B5B3F5"), (10,13,"#B5B3F5"), (10,14,"#B5B3F5"), (10,15,"#B5B3F5"), (10,16,"#B5B3F5"), (10,17,"#B5B3F5"), (10,18,"#B5B3F5"), (10,19,"#FFFFFF"), (11,4,"#FFFFFF"), (11,5,"#B5B3F5"), (11,6,"#B5B3F5"), (11,7,"#B5B3F5"), (11,8,"#B5B3F5"), (11,9,"#B5B3F5"), (11,10,"#B5B3F5"), (11,11,"#B5B3F5"), (11,12,"#B5B3F5"), (11,13,"#B5B3F5"), (11,14,"#B5B3F5"), (11,15,"#B5B3F5"), (11,16,"#B5B3F5"), (11,17,"#B5B3F5"), (11,18,"#B5B3F5"), (11,19,"#FFFFFF"), (12,4,"#FFFFFF"), (12,5,"#B5B3F5"), (12,6,"#B5B3F5"), (12,7,"#B5B3F5"), (12,8,"#B5B3F5"), (12,9,"#B5B3F5"), (12,10,"#B5B3F5"), (12,11,"#B5B3F5"), (12,12,"#B5B3F5"), (12,13,"#B5B3F5"), (12,14,"#B5B3F5"), (12,15,"#B5B3F5"), (12,16,"#B5B3F5"), (12,17,"#B5B3F5"), (12,18,"#B5B3F5"), (12,19,"#FFFFFF"), (13,4,"#FFFFFF"), (13,5,"#B5B3F5"), (13,6,"#B5B3F5"), (13,7,"#B5B3F5"), (13,8,"#B5B3F5"), (13,9,"#B5B3F5"), (13,10,"#B5B3F5"), (13,11,"#B5B3F5"), (13,12,"#B5B3F5"), (13,13,"#B5B3F5"), (13,14,"#B5B3F5"), (13,15,"#B5B3F5"), (13,16,"#B5B3F5"), (13,17,"#B5B3F5"), (13,18,"#B5B3F5"), (13,19,"#FFFFFF"), (14,4,"#FFFFFF"), (14,5,"#B5B3F5"), (14,6,"#B5B3F5"), (14,7,"#B5B3F5"), (14,8,"#B5B3F5"), (14,9,"#B5B3F5"), (14,10,"#B5B3F5"), (14,11,"#B5B3F5"), (14,12,"#B5B3F5"), (14,13,"#B5B3F5"), (14,14,"#B5B3F5"), (14,15,"#B5B3F5"), (14,16,"#B5B3F5"), (14,17,"#B5B3F5"), (14,18,"#B5B3F5"), (14,19,"#FFFFFF"), (15,4,"#FFFFFF"), (15,5,"#B5B3F5"), (15,6,"#B5B3F5"), (15,7,"#B5B3F5"), (15,8,"#B5B3F5"), (15,9,"#B5B3F5"), (15,10,"#B5B3F5"), (15,11,"#B5B3F5"), (15,12,"#B5B3F5"), (15,13,"#B5B3F5"), (15,14,"#B5B3F5"), (15,15,"#B5B3F5"), (15,16,"#B5B3F5"), (15,17,"#B5B3F5"), (15,18,"#B5B3F5"), (15,19,"#FFFFFF"), (16,4,"#FFFFFF"), (16,5,"#B5B3F5"), (16,6,"#B5B3F5"), (16,7,"#B5B3F5"), (16,8,"#B5B3F5"), (16,9,"#B5B3F5"), (16,10,"#B5B3F5"), (16,11,"#B5B3F5"), (16,12,"#B5B3F5"), (16,13,"#B5B3F5"), (16,14,"#B5B3F5"), (16,15,"#B5B3F5"), (16,16,"#B5B3F5"), (16,17,"#B5B3F5"), (16,18,"#B5B3F5"), (16,19,"#FFFFFF"), (17,4,"#FFFFFF"), (17,5,"#B5B3F5"), (17,6,"#B5B3F5"), (17,7,"#B5B3F5"), (17,8,"#B5B3F5"), (17,9,"#B5B3F5"), (17,10,"#B5B3F5"), (17,11,"#B5B3F5"), (17,12,"#B5B3F5"), (17,13,"#B5B3F5"), (17,14,"#B5B3F5"), (17,15,"#B5B3F5"), (17,16,"#B5B3F5"), (17,17,"#B5B3F5"), (17,18,"#B5B3F5"), (17,19,"#FFFFFF"), (18,5,"#FFFFFF"), (18,6,"#B5B3F5"), (18,7,"#B5B3F5"), (18,8,"#B5B3F5"), (18,9,"#B5B3F5"), (18,10,"#B5B3F5"), (18,11,"#B5B3F5"), (18,12,"#B5B3F5"), (18,13,"#B5B3F5"), (18,14,"#B5B3F5"), (18,15,"#B5B3F5"), (18,16,"#B5B3F5"), (18,17,"#B5B3F5"), (18,18,"#FFFFFF"), (19,6,"#FFFFFF"), (19,7,"#FFFFFF"), (19,8,"#FFFFFF"), (19,9,"#FFFFFF"), (19,10,"#FFFFFF"), (19,11,"#FFFFFF"), (19,12,"#FFFFFF"), (19,13,"#FFFFFF"), (19,14,"#FFFFFF"), (19,15,"#FFFFFF"), (19,16,"#FFFFFF"), (19,17,"#FFFFFF")]


STEPD = 4 # speed of car. This changes dx,dy.
MAXx = 800
MAXy = 600
DOWNOFFSET = 100

STARTX = 0  # start location of car
STARTY = MAXy//2-10

LEVELSTART = 1   # change with start keys 1,2,3,...,9

popiscletype  = 1
strawberrytype = 2
plusredtype = 8
plusyellowtype = 9
pluswhitetype = 10
pluspurpletype = 11

threetype = 3

walls0 = {(0,3),(1,3),(2,3),(3,3),(4,3),(5,3),(6,3),(7,3),(9,3),(8,3),(10,3),(11,3),(12,3),(13,3),(14,3),(15,3),(16,3),(17,3),(18,3),(19,3),(20,3),(21,3),(22,3),(23,3),(0,8),(1,8),(2,8),(3,8),(4,8),(5,8),(5,8),(6,8),(7,8),(8,8),(9,8),(10,8),(11,8),(12,8),(13,8),(14,8),(15,8),(16,8),(17,8),(18,8),(19,8),(20,8),(21,8),(22,8),(23,8)}
pointsset0 = {(5,5,1),(5,6,1),(7,5,1),(7,6,1),(9,5,1),(9,6,1),(11,5,1),(11,6,1),(13,5,2),(13,6,2),(15,5,2),(15,6,2)}

pointsset1 = {(13,7,10),(7,8,11),(23,7,9),(8,6,8),(10,8,5),(19,6,5)}

walls1 = {(3,8),(3,9),(3,10),(3,11),(5,11),(6,11),(4,11),(7,11),(9,11),(8,11),(10,11),(11,11),(12,11),(13,11),(14,11),(16,11),(15,11),(17,11),(18,11),(20,11),(19,11),(21,11),(22,11),(23,11)}


wallslist = [walls0, walls1]
pointslist = [pointsset0, pointsset1]
maxlist = [2100,5000,5000,5000,5000,5000,5000,5000,5000,5000] # max score for levels 0, ...


mathstring = "1+(2A+3B+4I)*4XY"

# 1+(2+3)
mathstring = "1+(2+3)"
FirstColourOrder = ["red","yellow"]
SecondColourOrder = ["red"]
FirstEval = "yellow+"
SecondEval = "red+"


# (1+2)+3
mathstringB = "(1+2)+3"
FirstColourOrderB = ["white","purple"]
SecondColourOrderB = ["purple"]
FirstEvalB = "white+"
SecondEvalB = "purple+"


walls = wallslist[LEVELSTART]
pointsset = pointslist[LEVELSTART]

score = 0
bonus = 1000  # decrease 100 per second

ShowAllCollisions = False

HitWall = False
PlayerAlive = False
GameRunning = False
GameComplete = False
Stopping = False

highscore = 0

fruitlist = []
solidlist = []

wallsize = 30  # put blocks in grid from (0,0) to (22,12)

def checkcollisionrect(object1,object2):
     x1,y1,x2,y2 = object1.collisionrect 
     a1,b1,a2,b2 = object2.collisionrect
     x1 = x1 + object1.x
     y1 = y1 + object1.y
     x2 = x2 + object1.x
     y2 = y2 + object1.y 
     a1 = a1 + object2.x
     b1 = b1 + object2.y
     a2 = a2 + object2.x
     b2 = b2 + object2.y 
     if x2 < a1 or x1 > a2 or y2 < b1 or y1 > b2:
          return False
     else:
          return True

def makewalls():
    for x,y in walls:
        wall = LEDlib.LEDobj(canvas1,x*wallsize-8,y*wallsize-8+DOWNOFFSET,dx = 0,dy = 0,CharPoints=charWall2, pixelsize = 2,typestring = "solid")
        wall.collisionrect = (8,8,40,40)
        solidlist.append(wall) 

def createfruit(x,y,char, typestring):
    return LEDlib.LEDobj(canvas1,x*wallsize+8,y*wallsize+DOWNOFFSET,dx = 0,dy = 0,CharPoints=char, pixelsize = 4,typestring = typestring)

def createplayfield():
   makewalls()
   for x,y,stype in pointsset:
       if stype == popiscletype:
           fruit = createfruit(x,y,charPopsicle, typestring = "fruit")
           fruit.collisionrect = (0,0,16,36)
           fruit.PointsType = 100
           fruitlist.append(fruit)
       if stype == strawberrytype:
           fruit = createfruit(x,y,charPacmanStrawberry,typestring = "fruit")
           fruit.collisionrect = (0,6,22,30)
           fruit.PointsType = 200
           fruitlist.append(fruit)
       if stype == plusyellowtype:
           fruit = createfruit(x,y,charYellowPlus, "yellow+")
           fruit.collisionrect =  (24,24,68,68)
           fruit.PointsType = 200
           fruitlist.append(fruit)
       if stype == plusredtype:
           fruit = createfruit(x,y,charRedPlus,typestring = "red+")
           fruit.collisionrect = (24,24,68,68)
           fruit.PointsType = 200
           fruitlist.append(fruit)
       if stype == pluswhitetype:
           fruit = createfruit(x,y,charWhitePlus, typestring = "white+")
           fruit.collisionrect = (24,24,68,68)
           fruit.PointsType = 200
           fruitlist.append(fruit) 
       if stype == pluspurpletype:
           fruit = createfruit(x,y,charPurplePlus,typestring = "purple+")
           fruit.collisionrect = (24,24,68,68)
           fruit.PointsType = 200
           fruitlist.append(fruit) 

def mykey(event):
    global HitWall, PlayerAlive, starttime,score, highscore,walls,pointsset, LEVELSTART, counttime, GameRunning, GameComplete, Stopping
    if not GameRunning and not GameComplete: # start game when user presses a key
           GameRunning  = True
           updatebonus()
    if Stopping: return        
    key = event.keysym
    if HitWall:
         HitWall = False
    elif (key == "w" or key == "Up") and LEVELSTART > 0:
         myship.rotate(0)
         myship.dy = -STEPD
         myship.dx = 0
    elif (key == "d" or key == "Right") and LEVELSTART > 0:
         myship.rotate(90)
         myship.dy = 0
         myship.dx = STEPD
    elif (key == "a" or key == "Left") and LEVELSTART > 0:
         myship.rotate(270)
         myship.dy = 0
         myship.dx = -STEPD
    elif (key == "s" or key == "Down") and LEVELSTART > 0:
         myship.rotate(180)
         myship.dy = STEPD
         myship.dx = 0


def updatebonus():
    global bonus, GameRunning
    if GameRunning:
      bonus = bonus - 10
      if bonus < 0: bonus = 0
      displaybonus.update(bonus)
      mainwin.after(200,updatebonus)
     

def slowstop():
    global Stopping
    Stopping = False
    myship.dx = 0
    myship.dy = 0

def bump():
    global HitWall, Stopping
    myship.dx = -myship.dx
    myship.dy = -myship.dy
    HitWall = True  
    print("Incorrect") 
    Stopping = True
    mainwin.after(100,slowstop) 


def gameloop():
    global HitWall, score, highscore, mathstring, FirstEval, GameRunning, GameComplete, Stopping
    if LEVELSTART == 0: myship.dx = 2
    if PlayerAlive or LEVELSTART == 0: myship.move()
    for fruit in fruitlist:
       if checkcollisionrect(myship,fruit):   
            if fruit.typestring == FirstEval:  
               displaystring = "2+3=5"
               displaymath2.update("= 1+5")
               LEDlib.LEDtextobj(canvas1,x=fruit.x,y=fruit.y,text=displaystring,colour="light green",pixelsize = 2, charwidth=16, multicolour=True, plusorder = ["yellow"], solid = True)
               FirstEval = ""
               fruit.undraw()
               fruitlist.remove(fruit)
               score = score + fruit.PointsType
            elif fruit.typestring == SecondEval: 
               if FirstEval == "":
                  displaystring = "1+5=6"
                  displaymath3.update("= 6")
                  LEDlib.LEDtextobj(canvas1,x=fruit.x,y=fruit.y,text=displaystring,colour="light green",pixelsize = 2, charwidth=16, multicolour=True, plusorder = ["red"], solid = True)
                  fruit.undraw()
                  fruitlist.remove(fruit)
                  score = score + fruit.PointsType
                  score = score + bonus
                  GameRunning = False
                  GameComplete = True
               else:
                   bump()
            else:
               bump()
            if score > highscore: 
                highscore = score
            displayscore.update(score)
    for solid in solidlist:
         if checkcollisionrect(myship,solid): 
            if not HitWall:
              myship.x = myship.x - myship.dx
              myship.y = myship.y - myship.dy
            myship.dx = 0
            myship.dy = 0
            HitWall = True
            break # exit the for loop
    mainwin.after(10,gameloop)


mainwin = Tk(className=" BODMAS")
mainwin.geometry(str(MAXx)+"x"+str(MAXy)) 
canvas1 = Canvas(mainwin,width=MAXx,height= MAXy,bg="black")
canvas1.place(x=0,y=0)

myship = LEDlib.LEDobj(canvas1,STARTX,STARTY,dx = 0,dy = 0,CharPoints=charRallyX, pixelsize = 2,typestring = "car")
myship.collisionrect = (4,3,44,45)
myship.rotate(90)


displayscore = LEDlib.LEDscoreobj(canvas1,x=210,y=10,score=0,colour="white",pixelsize=3, charwidth = 24,numzeros=5)
displaytextscore = LEDlib.LEDtextobj(canvas1,x=235,y=35,text="SCORE",colour="yellow",pixelsize = 2, charwidth=14, solid = True)

displaybonus = LEDlib.LEDscoreobj(canvas1,x=410,y=10,score=bonus,colour="white",pixelsize=3, charwidth = 24,numzeros=5)
displaytextscore = LEDlib.LEDtextobj(canvas1,x=435,y=35,text="BONUS",colour="yellow",pixelsize = 2, charwidth=14, solid = True)


displaymath = LEDlib.LEDtextobj(canvas1,x=240,y=60,text=mathstring,colour="light green",pixelsize = 3, charwidth=24, multicolour=True, plusorder = FirstColourOrder, solid = True)
displaymath2 = LEDlib.LEDtextobj(canvas1,x=193,y=98,text="= ?",colour="light green",pixelsize = 3, charwidth=24, multicolour=True, plusorder = SecondColourOrder, solid = True)
displaymath3 = LEDlib.LEDtextobj(canvas1,x=193,y=135,text="= ?",colour="light green",pixelsize = 3, charwidth=24, multicolour=True, plusorder = SecondColourOrder, solid = True)


displaymathB = LEDlib.LEDtextobj(canvas1,x=440,y=60,text=mathstringB,colour="light green",pixelsize = 3, charwidth=24, multicolour=True, plusorder = FirstColourOrderB, solid = True)
displaymathB2 = LEDlib.LEDtextobj(canvas1,x=393,y=98,text="= ?",colour="light green",pixelsize = 3, charwidth=24, multicolour=True, plusorder = SecondColourOrderB, solid = True)
displaymathB3 = LEDlib.LEDtextobj(canvas1,x=393,y=135,text="= ?",colour="light green",pixelsize = 3, charwidth=24, multicolour=True, plusorder = SecondColourOrderB, solid = True)



createplayfield()
gameloop()
# updatebonus() gets called in mkey

PlayerAlive = True

mainwin.bind("<KeyPress>", mykey)
mainwin.mainloop()

