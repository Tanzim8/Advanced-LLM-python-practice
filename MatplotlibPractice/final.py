import matplotlib.pyplot as plt
import pandas as pd

data = pd.read_csv("ai_experiments.csv")

plt.scatter(data["response_time"],data["accuracy"])
plt.title("Response VS Accuracy")
plt.xlabel("Response Time")
plt.ylabel("Accuracy")
plt.savefig("ResVsACC.png")

plt.show()

plt.close()

#Challenge 3
#Scatter plot for tokens and accuracy
plt.scatter(data["tokens"], data["accuracy"])
plt.title("Tokes VS Accuracy")
plt.xlabel("Tokens")
plt.ylabel("Accuracy")
plt.savefig("TokensVsAccuracy.png")

plt.show()
plt.close()

#Challenge 4
print(data.groupby("model")["accuracy"].mean())
plt.bar(data["model"], data["accuracy"])
plt.title("ModelAvg vs Accuracy")
plt.xlabel("Model")
plt.ylabel("Accuracy")

plt.savefig("mAvg VS acc")

plt.show()

plt.close()

#Average response time by model
#Challenge 5
plt.bar(data["model"], data["response_time"])
plt.title("model vs response time")
plt.xlabel("Model")
plt.ylabel("Response time")

plt.savefig("modelVSrespnse.png")

plt.show()
plt.close()

#Challenge 6
plt.plot(range(len(data)), data["accuracy"])
plt.title("Experiment VS Accuracy")
plt.xlabel("Experiment")
plt.ylabel("Accuracy")

plt.savefig("expVSacc.png")
plt.show()
plt.close()

#Challenge-7

plt.hist(data["response_time"])
plt.title("Response time histogram")
plt.xlabel("Response time")
plt.ylabel("Frequency")

plt.savefig("ExpVrsp.png")
plt.show()
plt.close()

#Challenge-7.1

plt.hist(data["response_time"], bins=5)
plt.title("Response time histogram")
plt.xlabel("Response time")
plt.ylabel("Frequency")

plt.savefig("ExpVrsp12.png")
plt.show()
plt.close()
