
import numpy as np

x = [1,2,3,4,5]

y = [10,20,-10,-50,30000]

# logy = 20*np.log10(y)
y_abs = np.abs(y)
print(y_abs)
# y = 20 * np.log10(y)
y_abs = 20 * np.log10(y_abs)
print(y_abs)