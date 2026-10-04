import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import math 

data = pd.DataFrame({
    "accuracy": [82, 88, 91, 85, 94, 89, 87, 96, 84, 90],
    "response_time": [3.8, 3.2, 2.7, 3.6, 2.4, 3.0, 3.3, 2.1, 3.7, 2.8]
})

meanAccuracy = np.mean(data["accuracy"])
medianAccuracy = np.median(data["accuracy"])

print("Mean accuracy: ", meanAccuracy)
print("Median accuracy: ", medianAccuracy)

rangeCalc = np.max(data["accuracy"]) - np.min(data["accuracy"])

print("Range: ", rangeCalc)

dataVar = np.var(data["accuracy"])
print("Varience: ",dataVar)

dataSD = np.std(data["accuracy"])
print("SD: ",dataSD)

corrAccRes = data["accuracy"].corr(data["response_time"])
print("Correlation: ",corrAccRes)

#Z-scores - assuming accuracy - 96
zScore = (96-meanAccuracy)/dataSD
print("Z-Score: ",zScore)

#Standard error - assuming 10 observation sample
standardErr = dataSD/math.sqrt(10)
print("Stanard Error: ", standardErr)

#confidence interval: for 95% mean
upperBond = meanAccuracy + 2*(standardErr)
print("UpperBond: ", upperBond)

lowerBond = meanAccuracy - 2*(standardErr)
print("LowerBound: ", lowerBond)

#6-Visualization
plt.scatter(data["response_time"],data["accuracy"])
plt.title("Response Time VS Accuracy")
plt.xlabel("Response time")
plt.ylabel("Accuracy")
plt.savefig("result.png")
plt.close()

print("Reject H0 cause, p = 0.018 < 005")


