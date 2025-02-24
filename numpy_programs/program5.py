# In a np array of spendings of the week, find the highest spending and the day.
import numpy as np
week_spendings = np.array([50, 120, 30, 40, 200, 90, 300])
index = 1
big_spending = week_spendings[0]
index = np.argmax(week_spendings)
days = {1:'monday', 2:'tuesday', 3:'wednesday', 4:'thursday', 5:'friday', 6:'saturday', 7:'sunnday'}
print(big_spending, days[index])
