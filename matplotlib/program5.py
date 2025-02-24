# HISTOGRAM
#Analyzing the frequency distribution of normally distributed data.

import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
import pandas as pd
from mpl_toolkits.mplot3d import Axes3D 

data = np.random.randn(1000)

plt.hist(data, bins=30, color='pink', edgecolor='black')
plt.xlabel("Value")
plt.ylabel("Frequency")
plt.title("Histogram")
plt.show()