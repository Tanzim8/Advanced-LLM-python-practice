import pandas as pd

data = pd.read_csv("ai_experiment.csv")

print("First 5 rows: ","\n",data.head())

print("Last 5 rows: ","\n",data.tail())

print("Shape of the CSV file: ", "\n", data.shape)

print("The columns: ", "\n", data.columns)

print("The info: ", "\n", data.info())

print("Description: ", "\n", data.describe())

#only printing the model and accuracy columns
print(data[["model", "accuracy"]])

print("4th Row: ",data.iloc[3])

print("6th ROW: ",data["response_time"].iloc[4])

#All experiments greater than 85

print(data[data["accuracy"]>85])

print(data[
    (data["accuracy"] > 85) & 
    (data["response_time"]<3.0)
    ])

print("All the halluciated response: ", data[(data["hallucinated"] == True)] )

print(data[
      (data["model"]=="GPT") &
      (data["accuracy"] > 90)
])

#Statistics
print("Average accuracy: ",data["accuracy"].mean())

print("Max accuracy: ",data["accuracy"].max())

print("Min Accuracy: ",data["accuracy"].min())

print("Average response time: ", data["response_time"].mean())

print("Total tokens: ", data["tokens"].sum())

count = (data["accuracy"]>90).sum()

print(count)

data["performence"] = data["accuracy"] / data["response_time"]

print(data)

data["Passed"] = data["accuracy"]>=85
print(data)

mistral_performence = 91/2.8
mistral_passed = 91 >=85
data.loc[len(data)] = ["Mistral", "Coding", 2.8, 91, 350, False, mistral_performence, mistral_passed]
print(data)

#GroupBy for average

print(data.groupby("model")["response_time"].mean())

# print(data.dtypes)

print(data.iloc[data["performence"].idxmax()])