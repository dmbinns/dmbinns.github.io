---
title: "Visualizing API Data in Python: A Beginner's Guide"
---

# Visualizing API Data in Python: A Beginner's Guide

Have you ever wanted to analyze live data? The way many organizations share their data is through Application Programming Interfacse, more commonly known as APIs.

In this tutorial, we will walk into the world of APIs by fetching real data from a public API, turning it into a tidy table with Pandas, and creating a simple chart with Matplotlib. 

More specifically, we are going to use the [Open Notify API](http://api.open-notify.org/astros.json) to:
* Fetch live JSON data about astronauts currently in space.
* Convert it into a Pandas DataFrame.
* Create a simple visualization of astronauts by spacecraft.
This is a short, hands-on exercise you can adapt to almost any API.

## Pre-reqs

We will be doing all thee work for this tutorial in Python. To set up, you will need to install and import a few libraries. 

First, open your terminal and makesure you have these installed:

```pip install requests pandas matplotlib```

In Python, import the libraries needed for the tutorial. We’ll use ```requests``` to call the API, ```pandas``` for data wrangling, and ```matplotlib``` for plotting.

```
import requests
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
```

## Fetching The Data

Now we will access the actual API to fetch astronaut data. This API returns JSON with three keys: ```"people"```,```"number"```, and ```"message"```.

```
url = "http://api.open-notify.org/astros.json"
response = requests.get(url, timeout=10)
data = response.json()

print(data.keys())
print(data["number"], "people are in space right now.")
```

An example of how your output should look is the following:
```
dict_keys(['people', 'number', 'message'])
10 people are in space right now.
```

## Loading in The Data

Now that we have the data from the API, we will be converting it to a ```Pandas``` DataFrame. 
In our example, the ```"people"``` key contains a list of dictionaries. This works perfectly for a Pandas DataFrame.

```
astronauts = pd.DataFrame(data["people"])
print(astronauts.head())
```

Your output should look something like this:
```
           craft              name
0             ISS   Sergey Prokopyev
1             ISS     Dmitry Petelin
2             ISS     Frank Rubio
```

## Visualizing The Data

Now that we have the data saved as a DataFrame, we will be using it to make a basic chart. 

For our example, let's group by the ```"craft"``` column and plot the counts.
```
# Count astronauts by spacecraft
craft_counts = astronauts["craft"].value_counts().reset_index()
craft_counts.columns = ["Craft", "Astronauts"]

# Plot
ax = craft_counts.plot(kind="bar", x="Craft", y="Astronauts", legend=False, figsize=(6,4))
ax.set_title("Astronauts in Space by Spacecraft")
ax.set_ylabel("Number of Astronauts")
plt.xticks(rotation=0)
plt.tight_layout()
plt.show()
```

