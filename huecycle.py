from tree import RGBXmasTree, layerDict
from colorzero import Color, Hue

tree = RGBXmasTree(brightness=0.4)

def colourALayer(layerArray, colour):
    for x in layerArray:
        tree[x].color = colour

colours = [Color('red'), Color('green'), Color('blue'), Color('white')]

# Set tree colours
for k, v in layerDict.items():
    colourALayer(v, colours[k])

try:
    while True:
        for x in range(0, 24):
            tree[x].color += Hue(deg=3)

except KeyboardInterrupt:
    tree.close()
