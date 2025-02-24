#Finding indices where spendings are greater than 100
import numpy as np
week_spendings = np.array([50, 120, 30, 40, 200, 90, 300])
high_spend = np.where(week_spendings > 100)
print(high_spend)