# Visualizing a sine wave using a line plot.
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
import pandas as pd
from mpl_toolkits.mplot3d import Axes3D  

x = np.linspace(0, 10, 100)  
y = np.sin(x) 

plt.plot(x, y, label="Sine Wave")  
plt.xlabel("X-axis") 
plt.ylabel("Y-axis") 
plt.title("Line Plot") 
plt.legend()  
plt.show() 
