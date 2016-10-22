#! /usr/bin/env python

#Minimal Roguelike by David Weaver 2016
import random
from operator import itemgetter

landscape1 = ['a small line of hills', 'a quiet brook', 'a lake', 'a sun-dappled forest','an old cobbled road']
joining = ['by a', 'next to','opposite']
landscape2 = ['a silent valley','a tidy looking village','an old crumbling fort']


def worldGen():

    worldscape = []
    
    worldscape.append(random.choice(landscape1))
    worldscape.append(random.choice(joining))
    worldscape.append(random.choice(landscape2))

    renderWorld(worldscape)

    return worldscape

def renderWorld(worldscape):
    world =(" ".join(worldscape)) 
    print("You can see " + world)
    
    

def mainLoop():
    while 1:
        worldscape = worldGen()
        choice = takeInput()
        resolveInput(choice,worldscape)

def takeInput():
    choice = input("Choose 1 or 2 ")
    return int(choice)
    
def resolveInput(choice,worldscape):

        if choice is 1:
            print("You head towards " + str(worldscape[0]))

        elif choice is 2:
            print("You head towards " + str(worldscape[2]))
            
        else:
            print("I didn't understand that input")

mainLoop()
