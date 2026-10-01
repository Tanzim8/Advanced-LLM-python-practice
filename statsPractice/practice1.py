import numpy as np
import math
import pandas as py

accuracy = np.array([88, 92, 85, 94, 91, 87, 96])

Mean = accuracy.mean()
print("Mean: ", Mean)

Range = accuracy.max() - accuracy.min()
print("Range: ", Range)

# sqrdDff = 0
# Diff = 0
# for val in accuracy:
#     diff = val - Mean
#     # print("Varience: ", diff)
#     Diff += diff
#     orgDiff = (diff)*(diff)
#     sqrdDff+=orgDiff



# Varience = (sqrdDff)/len(accuracy)
# print("Varience: ", Varience)

# SD = math.sqrt(Varience)
# print("SD: ", SD)

varience = np.var(accuracy)
print("Varience: ", varience)

SD = np.std(accuracy)
print("SD: ", SD)

data = py.read_csv("ai_experiments.csv")

#Accuracy and response time correlation: -.77 srongly negative
Corr = data["accuracy"].corr(data["response_time"])
print(Corr)

#Accuracy and tokens correlation: 0.30 weak positive linear rel

Corr1 = data["accuracy"].corr(data["tokens"])
print(Corr1)

#Z-socre
for acc in accuracy:
    z = (acc-Mean)/SD
    print(z)


