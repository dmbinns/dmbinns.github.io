---
title: "Visualizing API Data in Python: A Beginner's Guide"
---

# Visualizing API Data in Python: A Beginner's Guide

Have you ever wanted to analyze live data? The way many organizations share their data is through Application Programming Interfacse, more commonly known as APIs.

In this tutorial, we will walk into the world of APIs by fetching real data from a public API, turning it into a tidy table with Pandas, and creating a simple chart with Matplotlib. 

More specifically, we are going to use the [Open Notify API](http://api.open-notify.org/astros.json) to:
    - Fetch live JSON data about astronauts currently in space.
    - Convert it into a Pandas DataFrame.
    - Create a simple visualization of astronauts by spacecraft.
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

Now we will access the actual API to fetch astronaut data. This API returns JSON with three keys: "people","number", and "message".

```
url = "http://api.open-notify.org/astros.json"
response = requests.get(url, timeout=10)
data = response.json()

print(data.keys())
print(data["number"], "people are in space right now.")
```


## Loading in The Data

## Visualizing The Data

This portfolio shows my work learning data science. Each project includes:

- My code with documentation
- Visualizations I created
- What I learned and discovered

I built this site using [Quarto](https://quarto.org/) and host it on [GitHub Pages](https://pages.github.com/).

## 🛠️ Skills I'm Learning

- **Programming**: Python, Pandas for data analysis
- **Visualization**: Creating charts with Matplotlib and Seaborn
- **Data Collection**: Getting data from files, websites, and APIs
- **Analysis**: Finding patterns and answering questions with data

## 📈 My Projects

::: {.grid}

::: {.g-col-6}
### [Data Exploration Project](projects/eda.qmd)
Learn how I explore datasets to find interesting patterns and answer questions.
:::

::: {.g-col-6}
### [Data Collection Project](projects/data-acquisition.qmd)
See how I gather data from different sources and prepare it for analysis.
:::

::: {.g-col-6}
### [Final Project](projects/final-project.qmd)
See how I tackle a data science project beginning to end.
:::

:::

---

*Thanks for visiting! Feel free to explore my projects and see what I'm learning.*