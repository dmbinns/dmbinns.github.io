# Testing the code I am using on the blog post

import requests
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np


url = "http://api.open-notify.org/astros.json"
response = requests.get(url, timeout=10)
data = response.json()

print(data.keys())
print(data["number"], "people are in space right now.")

astronauts = pd.DataFrame(data["people"])
print(astronauts.head())

# Count astronauts by spacecraft
craft_counts = astronauts["craft"].value_counts().reset_index()
craft_counts.columns = ["Craft", "Astronauts"]
print(craft_counts)

# Plot
ax = craft_counts.plot(kind="bar", x="Craft", y="Astronauts", legend=False, figsize=(6,4))
ax.set_title("Astronauts in Space by Spacecraft")
ax.set_ylabel("Number of Astronauts")
plt.xticks(rotation=0)
plt.tight_layout()
plt.show()