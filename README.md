# 📊 Exploratory Data Analysis of a Marketing Campaign Dataset

## 📌 Overview

This project presents an exploratory data analysis (EDA) of a marketing campaign dataset originally provided in a **DataCamp exercise on data cleaning**. While the exercise focused on cleaning the data, the analysis presented here is entirely my own initiative. The aim was to uncover patterns in customer behavior and campaign outcomes through visual exploration and descriptive statistics.

**Note:** The original dataset is not included in this repository due to licensing, but the notebook used for the data cleaning process is available.

---

## 🔍 Objectives
- Clean the dataset by following provided requirements.
- Explore the distribution of numerical variables (e.g., age, contact duration, number of contact attempts).
- Detect skewness and outliers using visual and statistical methods.
- Compare success rates between current and previous campaigns.
- Segment categorical variables such as job and education level.
- Visualize proportions of success and failure across multiple categories.
- Implement custom logic for selecting representative categories based on cumulative thresholds.
- Practice coding by defining a custom class for category filtering and plotting, and a custom function for bin generation (though not used, just for practicing).

---

## 🛠️ Tools & Libraries

- Python  
- Jupyter Notebook  
- pandas, numpy, seaborn, matplotlib
- Custom Python class for category analysis

---

## 📊 Key Insights

- The majority of marketing contacts result in failure, although the **current campaign shows improved performance** (success rate increased from 3.3% to 11.3%).
- **Longer contact durations** are often associated with successful outcomes.
- Most customers are between 25 and 54 years old, but **younger (17–24) and older (65–98) customers**, though less frequent, show high success rates.
- **Job categories** like "admin", "student", and "retired" have notably different success rates, with students achieving the highest (31.42%) despite low frequency.
- A **threshold-based approach** was applied to identify the main categories in categorical variables for better interpretability and focus.

---

## 🧠 What I Learned

- Applied Python coding to make data cleaning.
- Applied a full EDA pipeline on marketing data.
- Explored categorical and numerical variables using visual storytelling.
- Implemented object-oriented programming for reusable data analysis logic.
- Created clear, interpretable visualizations using both Seaborn and Matplotlib.
- Improved my coding skills by writing custom functions and classes.
- Improved my communication of data-driven insights in English.

---

## 🚀 Future Work

- Examine atypical (outliers) observations on variables like constact time and number of contacts. This might give new insights about customer engagement.
- Extend the project to include predictive modeling (logistic regression or decision trees).
- Build a dashboard in PowerBI for interactive exploration.

