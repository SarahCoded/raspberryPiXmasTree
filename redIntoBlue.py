from tree import RGBXmasTree, layerDict
from colorzero import Color, Hue
from time import sleep

tree = RGBXmasTree()

# Initially set tree as red
r = 1
g = 255
b = 255

try:
    while True:
        tree.color = (r, g, b)
        if r == 1:
            sleep(2) # Pause on red
            for x in range(254):
                tree.color = (r, g, b)
                r += 1
                b -= 1
        else:
            for x in range(254):
                tree.color = (r, g, b)
                r -= 1
                b += 1
        sleep(2) # Pause on blue

except KeyboardInterrupt:
    tree.close()