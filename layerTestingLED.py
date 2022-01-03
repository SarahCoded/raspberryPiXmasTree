from tree import RGBXmasTree
from colorzero import Color

tree = RGBXmasTree(brightness=0.2)

# Bottom layer
tree[0].color = Color('green')
tree[6].color = Color('green')
tree[7].color = Color('green')
tree[12].color = Color('green')
tree[15].color = Color('green')
tree[16].color = Color('green')
tree[19].color = Color('green')
tree[24].color = Color('green')

# Middle Layer
tree[1].color = Color('red')
tree[5].color = Color('red')
tree[8].color = Color('red')
tree[11].color = Color('red')
tree[14].color = Color('red')
tree[17].color = Color('red')
tree[20].color = Color('red')
tree[23].color = Color('red')

# Top Layer
tree[2].color = Color('blue')
tree[4].color = Color('blue')
tree[9].color = Color('blue')
tree[10].color = Color('blue')
tree[13].color = Color('blue')
tree[18].color = Color('blue')
tree[21].color = Color('blue')
tree[22].color = Color('blue')

# Treetop
tree[3].color = Color('yellow')
