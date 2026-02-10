# 🧙‍♂️ Harry Potter Characters – Data Analysis Project

## 📌 Project Overview
This project explores and analyzes a dataset of characters from the Harry Potter universe.  
The goal is to perform an end-to-end data analysis workflow, including data collection, data cleaning, exploratory data analysis (EDA), and data visualization, in order to extract meaningful insights from the data.

This project was developed as part of my personal learning journey in Data Analysis using Python.

---

## 🎯 Objectives
- Understand the structure and quality of the dataset  
- Clean and prepare the data for analysis  
- Explore the distribution of characters by house, gender, species, and survival status  
- Create visualizations to communicate insights  

---

## 📂 Dataset
The dataset was obtained from a public Harry Potter API and contains information about 437 characters, including:

- Name  
- House  
- Gender  
- Species  
- Survival status (alive/deceased)  

Some attributes (e.g., patronus, date of birth, eye color, ancestry) contain a high percentage of missing values and were excluded from deeper analysis.

---

## 🔎 Methodology

### 1. Exploratory Data Analysis (EDA)
- Inspected dataset structure and data types  
- Analyzed missing values  
- Explored unique values in key categorical columns  

### 2. Data Cleaning & Preparation
- Handled missing values in categorical variables by assigning an "Unknown" category  
- Standardized text values  
- Selected relevant columns for analysis  

### 3. Data Analysis & Visualization
The following analyses were performed:

- Distribution of characters by house  
- Distribution of characters by gender  
- Top 10 most common species  
- Alive vs deceased characters  
- House vs survival status  

---

## 📊 Key Insights
- Gryffindor and Slytherin are the most represented houses in the dataset (among characters with a defined house).  
- The majority of characters in the dataset are human.  
- Most characters are alive, but there are notable differences in survival counts across houses.  
- A significant portion of the dataset has missing values for certain attributes, highlighting the importance of data quality assessment before analysis.

---

## 🛠️ Technologies Used
- Python  
- pandas  
- matplotlib  

---

## ▶️ How to Run the Project
 ```bash
1. Install dependencies:
pip install -r requirements.txt

2. Run EDA:
python eda_hp.py

3. Clean the data:
python clean_hp_data.py

4. Run analysis and generate plots:
python analysis_hp.py
The generated plots will be saved in the images/ directory.
 ```

# 👩‍💻 Author
### Ana Julia Urbanek
Information Systems Student
