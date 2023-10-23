import pandas as pd
import matplotlib.pyplot as plt

# Load the data from the titanic competition
titanic_data = pd.read_csv("./train.csv")

# Number of passengers who survived
survived = (titanic_data.Survived == 1).sum()

# Number of passengers under 18
minors = (titanic_data.Age < 18).sum()

# Create a bar chart
categories = ["Total Passengers", "Survived", "Minors"]
counts = [len(titanic_data), survived, minors]

plt.bar(categories, counts)
plt.ylabel('Count')
plt.title('Passenger Statistics')

# Display percentages as text on the bars
for i in range(len(categories)):
    plt.text(i, counts[i] + 10, f'{(counts[i] / len(titanic_data) * 100):.2f}%', ha='center')

plt.show()
