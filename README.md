# RGB Xmas Tree

Code examples for the RGB Xmas Tree. This was run using a RaspberryPi 4B, with this [RGB Xmas tree](https://thepihut.com/products/3d-rgb-xmas-tree-for-raspberry-pi) from ThePiHut, using tree.py from [this repo](https://github.com/ThePiHut/rgbxmastree#rgbxmastree).

## Running the code on a Raspberry Pi RGB Xmas Tree

Clone this repo
```git clone https://github.com/SarahCoded/raspberryPiXmasTree.git```

In a terminal, run
```python tree.py```

All of the LEDs should light up in white. 

Next, run 
```python layerTestingLED.py```

If all of the LEDs are lit up from bottom to top in green, red, blue, yellow, then the rest of the code should work. If not, change the indexes of the lights until they are all aligned per their layer. For example, if you think that the top light happens to be at index 9, change tree[3].color = Color('yellow') to tree[9].color = Color('yellow'). Rerun the code to see if the change is expected. If it is, then also change the layerDict at the bottom of the tree.py file. Such that 3 : [3] would become 3 : [9]. In this dictionary layerDict, key is the layer number, and the values will be all the LEDs that correspond to that layer.

## redGreen.py

Cycles through red and green in layers going upward, while the yellow on top remains the same. 

### redGreenSparkles.py

This keeps the top light yellow, and allows the remaining lights to randomly switch between red and green. The choice of which light to change each time is random, but the choice of colour to change is predefined to ensure that there is always a roughly even distribution of red and green lighting. 

### huecycle.py

Cycles through red, green and blue hues forever in three layers simultaneously. 

### randomLayers.py

Changes a random tree layer with a 'random' colour. I set a predefined list of colours as an array, because I felt having completely random colours produces too many 'washed' out pale colours due to the nature of RGB possibilities.

### redIntoBlue.py

Changes colour from red to blue in a loop. Pauses for 2 seconds when red or blue is reached, as it won't stay that colour for long enough otherwise. 

### off.py

Turns off the tree lights! Useful for when there is a glitch and some lights change colour/flicker randomly.
