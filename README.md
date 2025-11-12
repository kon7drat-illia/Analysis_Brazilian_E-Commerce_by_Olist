# **Analysis Brazilian E-Commerce Public Dataset by Olist**
## 1. Project Overview & Business Problem
This project will analyze the Olist E-commerce dataset, a real dataset containing over 100,000 orders from a large Brazilian marketplace. The data is distributed across 8 separate tables, including information on orders, products, payments, deliveries, and customer reviews.

The Business Goal: The primary objective is to investigate the relationship between logistics performance and customer satisfaction. We will be looking for evidence to answer one key question: "How much do delivery-related issues (like delays, shipping costs, and speed) impact negative customer review scores?"
## 2. Tech Stack
* ### Database: SQLite
* ### Data Extraction & Transformation: SQL
* ### Data Analysis & Enrichment: Python (Pandas, Matplotlib, Seaborn)
* ### Business Intelligence & Visualization: Power BI (or Tableau)
* ### Environment: Jupyter Notebook, VS Code
## 3. Analysis Steps

### 1. Data Preparation & Integration:
* Load all 8 original Olist CSV files into a local SQLite database to create a relational structure. This mimics a real-world production environment where data lives in tables, not flat files.

### 2. Data Extraction & Transformation (SQL):
* Write a single, comprehensive SQL query to JOIN the necessary tables (e.g., orders, order_items, reviews, customers).
* Engineer new, calculated features (as required by the lab) directly in SQL. This includes: 
    * time_to_deliver_days (Time from purchase to delivery)
    * delivery_status (e.g., 'On Time', 'Late')
    * freight_to_price_ratio (Shipping cost vs. product price)

### 3. Data Enrichment & Analysis (Python):
* Load the clean data from the SQL query result into a Pandas DataFrame.

* Enrich the dataset by adding the required external data (e.g., Brazilian national holidays) to create the is_holiday_purchase column.

* Perform the "+" task analysis (EDA) using Matplotlib to find initial insights and correlations between delivery metrics and review scores.

* Export the final, fully enriched DataFrame to a new, clean CSV file.

### 4. Data Visualization (Power BI):
* Import the final, clean CSV into Power BI.

* Build an interactive dashboard to visually answer our key business question. The dashboard will include:

    * KPIs (Total Sales, Avg. Review Score, % Late Deliveries)

    * A map showing logistics performance by region.

    * Charts showing the direct impact of delivery_status on review_score.
## 4. Data Source
The 8 raw .csv files for this project are not included in this repository due to their large size (>100MB).

You can download the original dataset directly from Kaggle:
https://www.kaggle.com/datasets/olistbr/brazilian-ecommerce

To run this project, please download the files and place all 8 .csv files into the data/raw/ directory. The notebook will then load them into the SQLite database from there.