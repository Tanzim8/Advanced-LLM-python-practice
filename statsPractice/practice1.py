import numpy as np
import math

accuracy = np.array([88, 92, 85, 94, 91, 87, 96])

Mean = accuracy.mean()
print("Mean: ", Mean)

Range = accuracy.max() - accuracy.min()
print("Range: ", Range)

sqrdDff = 0
Diff = 0
for val in accuracy:
    diff = val - Mean
    # print("Varience: ", diff)
    Diff += diff
    orgDiff = (diff)*(diff)
    sqrdDff+=orgDiff

Varience = (sqrdDff)/len(accuracy)
print("Varience: ", Varience)

SD = math.sqrt(Varience)
print("SD: ", SD)


