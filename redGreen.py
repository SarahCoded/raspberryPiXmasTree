from tree import RGBXmasTree, layerDict
from colorzero import Color, Hue
import random
from time import sleep

tree = RGBXmasTree(brightness=0.05)

def colourALayer(layerArray, colour):
    for x in layerArray:
        tree[x].color = colour
    sleep(0.2)

tree[3].color = Color('yellow') # Make top yellow
layerDict.popitem() # Remove treetop from dictionary so it won't be changed later on

colours = [Color('red'), Color('green')]

try:
    while True:
        for colour in colours:
            for k, v in layerDict.items():
                colourALayer(v, colour)
            
except KeyboardInterrupt:
    tree.close()
    