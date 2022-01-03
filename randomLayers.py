from tree import RGBXmasTree, layerDict
from colorzero import Color
import random

tree = RGBXmasTree(brightness=0.2)

def colourALayer(layerArray, colour):
    for x in layerArray:
        tree[x].color = colour

colours = [Color('red'), Color('green'), Color('blue'), Color('yellow'), Color('magenta'), Color('orange'), Color('lime'), Color('deeppink'), Color('maroon'), Color('purple'), Color('violet')]

try:
    while True:
        randomColour = colours[random.randint(0, len(colours) - 1)]
        randomLayerArray = layerDict[random.randint(0, len(layerDict) - 1)]
        colourALayer(randomLayerArray, randomColour)
except KeyboardInterrupt:
    tree.close()
