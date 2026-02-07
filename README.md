# Real-Estate-Market-Analysis
Python real estate sales analysis: customer segmentation and property pricing trends through statistical analysis and visualization.

# 🏠 Real Estate Market Analysis

## 📌 Project Overview
This project analyzes real estate market data to identify trends in property prices, geographic distribution, customer demographics, and purchasing behavior and satisfaction. The analysis applies data cleaning, statistical methods, and visualization techniques to extract insights that can support strategic decision-making for management and marketing teams.

This repository is intended as a portfolio project demonstrating skills in Python data analysis and visualization.

---

## 🎯 Objectives
- Analyze real estate price trends
- Compare property prices across different locations
- Identify relationships between property features and price (customer age)
- Visualize market patterns and correlations
- Summarize key insights from the data

---

## 📂 Datasets
#customers
#properties


**Features include:**
- Customer ID
- Birth Date
- Status
- Property price
- Location
- Poperty Area
- Property type
- Additional variables used in the analysis

---

## 🛠 Tools & Technologies
- Python
- Pandas
- NumPy
- Matplotlib
- Seaborn
- Jupyter Notebook

---

## 🔍 Methodology
1. Data cleaning and preprocessing  
2. Statistical analysis
3. Visualization of trends and relationships  
5. Interpretation of results  

---

## 📊 Key Visualizations

### Net Revenue
![Monthly Net Revenue By Year](Real-Estate-Market-Analysis/figures/Monthly_Net_Revenue_by_Year.png)

### Sales by Building Type and Year
![C](Real-Estate-Market-Analysis/figures/Sales_by_Building_Type_and_Year.png)

### Customers Age Distribution
![Location Comparison](Real-Estate-Market-Analysis/figures/Distribution_of_Customers_Age.jpg)

---


## 💡 Key Findings

- The highest concentration of buyers falls within the 36–42 age group, indicating this demographic represents the strongest potential customer segment.
- The dataset shows a strong presence in the U.S. market, particularly in California, with emerging opportunities in neighboring states such as Nevada and Oregon.
- International purchases are more frequently made for investment purposes rather than personal use, suggesting the need for different marketing strategies compared to the U.S. market.
- Revenue peaked in 2007, just prior to the 2008 global financial crisis, highlighting the market’s sensitivity to economic conditions.
- Despite high sales volume, the majority of properties were purchased without mortgages, indicating that this data set may have limitations. 

---

## 📁 Repository Structure

Real-Estate-Market-Analysis/
│
├── data/
│ ├── raw/ # customers.csv
           # properties.csv
│ └── processed/ # dfcust_cleaned
                 # dfprop_cleaned2
                 #real-state-data
│
├── notebooks/ # Merging PROP-CUST.ipynb
               # Preprocessing CUST.ipynb
               # Preprocessing PROP.ipynb
               #Statistical Analysis.ipynb
               #Visualizations Real State.ipynb
├── figures/ # Avg_Deal_Satisfaction_Country.jpg
             # Distribution_of_Costumers_Age.jpg
             # Monthly_Net_Revenue_by_Year.png
             # Sales_by_Building_Type_and_year.png
             # Sales_by_State_and_Type.png
│
├── README.md
├── requirements.txt


---

## 🚀 How to Run the Project

1. Clone the repository:
```bash
git clone https://github.com/juleslighuenrc/Real-Estate-Market-Analysis.git


Install dependencies:

pip install -r requirements.txt


Open the notebooks:

jupyter notebook notebooks/Statistical Analysis
