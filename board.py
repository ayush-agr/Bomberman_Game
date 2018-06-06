from glob import *
from bomberman import Bomberman
from bomb import bomb
from getch import getch
from bricks import bricks
from enemy import enemy
import os
import time
import glob
import random
from walls import walls
from termcolor import colored

#from __future__ import print_function
import signal,copy,sys,time

wall1=walls(42,84)
bman=Bomberman(2,4)
lives=10
level=0
bmb=0
no_of_bricks=0
no_of_enemy=0

# These three functions to handle the cases when user doesn't input anything
class AlarmException(Exception):
    pass

def alarmHandler(signum, frame):
    raise AlarmException

def input_to(timeout=1):
    signal.signal(signal.SIGALRM, alarmHandler)
    signal.alarm(timeout)
    try:
        text = getch()
        signal.alarm(0)
        return text
    except AlarmException:
        pass#print("\n Prompt timeout. Continuing...")
    signal.signal(signal.SIGALRM, signal.SIG_IGN)
    return ''


def printboard():
    for x in range(wall1.rows):
        for y in range(wall1.columns):
            print(arr[x][y],end='')
        print('\n',end='')
    print('\n',end='')
    print("No of lives: "+str(lives)+"   level: "+str(level)+"        Score: ",glob.score)


def put_bricks():
    i=0
    while i<no_of_bricks:
        if i%2==0:
            a=random.randint(4,19)
            b=random.randint(1,19)
            y=4+4*(a-1)
            x=2+2*(b-1)
        else:
            a=random.randint(1,19)
            b=random.randint(4,19)
            y=4+4*(a-1)
            x=2+2*(b-1)
        if arr[x][y]==' ' and arr[x+1][y+3]==' ':
            brick_objs.append(bricks(x,y))
            i+=1
    for obj in brick_objs:
        obj.place_brick()

def put_enemy():
    i=0
    while i<no_of_enemy:
        if i%2==0:
            a=random.randint(4,19)
            b=random.randint(1,19)
            y=4+4*(a-1)
            x=2+2*(b-1)
        else:
            a=random.randint(1,19)
            b=random.randint(4,19)
            y=4+4*(a-1)
            x=2+2*(b-1)
        if arr[x][y]==' ' and arr[x+1][y+3]==' ':
            enemy_objs.append(enemy(x,y,i%4+1,0))
            i+=1
    for obj in enemy_objs:
        obj.place_enemy()    



while True:
    if bman.is_enemy_nearby():
             lives-=1 
    if len(enemy_objs)==0:
        bman.remove_it()
        bman=Bomberman(2,4)
        no_of_bricks+=10
        no_of_enemy+=7
        level+=1
        put_enemy()
        put_bricks()
    if level==6:
        print("Yayyyy!!, You Crosses all the levels You are WINNER")
        break
    t1=int(time.time())
    printboard()    
    inp=input_to()
    if inp=='q':
        break
    elif inp=='a':
        bman.move_left(glob.man)
    elif inp=='d':
        bman.move_right(glob.man)
    elif inp=='w':
        bman.move_up(glob.man)
    elif inp=='s':
        bman.move_down(glob.man)
    elif not(bmb) and inp=='b':
        bomb1=bomb(bman.x,bman.y)
        bmb=1
        start=int(time.time())
    if bmb:
        now=int(time.time())
        if now<=start+2:
            bomb1.plant_bomb(2-(now-start))
        elif now<=start+3:
            bomb1.remove_bomb()
            bomb1.show_effect(bman)
            bomb1.show_blast()
        elif now==start+4:
            bomb1.clear_blast()
            bmb=0
    if not(lives) or glob.dead:
        print("You Are Dead")
        break
    t2=int(time.time())
    if t2==t1+1:
        for obj in enemy_objs:
            obj.move_enemy(level)
    os.system('clear')
