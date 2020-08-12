# basic modules
import numpy as np
import pandas as pd
from matplotlib import pyplot as plt

# style choices: 'bmh', 'classic', 'dark_background', 'fast', 
#'fivethirtyeight', 'ggplot', 'grayscale', 'seaborn-bright', 
#'seaborn-colorblind', 'seaborn-dark-palette', 'seaborn-dark', 
#'seaborn-darkgrid', 'seaborn-deep', 'seaborn-muted', 'seaborn-notebook', 
#'seaborn-paper', 'seaborn-pastel', 'seaborn-poster', 'seaborn-talk', 
#'seaborn-ticks', 'seaborn-white', 'seaborn-whitegrid', 'seaborn', 
#'Solarize_Light2', 'tableau-colorblind10', '_classic_test'
plt.style.use('seaborn')

#donaldlax_colors = 

x = [1,2,3,4,5,6,7,8,9,10]

y1 = [13,11,9,7,5,3,1,-1,-3,-5]
y2 = [1,4,9,16,25,36,49,64,81,100]

plt.plot(x,y1, label = 'y1')
plt.plot(x,y2, label = 'y2')

plt.legend()

plt.xlabel('x - axis')
plt.ylabel('y - axis')
plt.title('this is a plot')

plt.show() #show the figures

