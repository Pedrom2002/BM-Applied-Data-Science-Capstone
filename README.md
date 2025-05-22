# Applied Data Science Capstone – SpaceX First Stage Landing Prediction

This Capstone project is the final course of the **IBM Data Science Professional Certificate** specialization. It consolidates all the skills acquired throughout the program into a real-world data science project.

---

## 📘 Project Overview

**Objective:**  
The goal is to predict the successful landing of the SpaceX Falcon 9 first stage using publicly available data and machine learning models. Since reusability of the first stage significantly reduces launch costs (from approximately $165M to $62M), predicting its success is economically valuable.

---

## ❓ Key Questions

- How do variables such as **payload mass**, **launch site**, **number of previous flights**, and **orbit type** influence first stage landing success?  
- Has the success rate of landings improved over the years?  
- What is the best classification algorithm for predicting landing outcomes?

---

## 🔍 Methodology

### Data Collection  
- SpaceX REST API for structured launch data  
- Web scraping from Wikipedia for historical and supplementary data  

### Data Wrangling  
- Data cleaning and filtering  
- Handling missing values  
- One-Hot Encoding of categorical variables for model compatibility  

### Exploratory Data Analysis (EDA)  
- Visualization using Matplotlib, Seaborn, and Plotly  
- SQL queries to gain additional insights  

### Interactive Visual Analytics  
- Folium maps to visualize launch site locations and success rates  
- Plotly Dash dashboard to interactively explore the dataset  

### Predictive Modeling  
- Training and evaluating classification models including:  
  - Logistic Regression  
  - Decision Trees  
  - Support Vector Machines (SVM)  
  - K-Nearest Neighbors (KNN)  
- Hyperparameter tuning to improve accuracy  
- Model comparison to identify the most effective algorithm  

---

## ✅ Conclusions

- The **Decision Tree model** outperforms other algorithms and proves to be the most suitable for predicting Falcon 9 first stage landing success on this dataset.  
- Launches with **lower payload masses** tend to achieve higher success rates compared to those carrying heavier payloads, highlighting the impact of payload weight on landing outcomes.  
- Most **launch sites are located near the Equator and close to coastal regions**, likely chosen to optimize launch logistics and enhance safety measures.  
- The **success rate of launches has improved steadily over the years**, reflecting continuous advancements in SpaceX’s technology and operational processes.  
- The **Kennedy Space Center Launch Complex 39A (KSC LC-39A)** exhibits the highest success rate among all analyzed launch sites.  
- Missions targeting **ES-L1, GEO, HEO, and SSO orbits** have achieved a **100% success rate**, demonstrating exceptional reliability for these orbital destinations.

