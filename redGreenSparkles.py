from tree import RGBXmasTree
from colorzero import Color
import random

tree = RGBXmasTree(brightness=0.4)
tree[3].color = Color('yellow') # Make top yellow
allowedValues = list(range(0, 24))
allowedValues.remove(3) # Ensure yellow won't be changed

try:
    while True:
        tree[random.choice(allowedValues)].color = Color('red')
        tree[random.choice(allowedValues)].color = Color('green')

except KeyboardInterrupt:
    tree.close()
    