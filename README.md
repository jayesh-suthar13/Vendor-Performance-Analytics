# Vendor Performance Analysis | End-to-End Data Analytics Project

## Overview

This project builds a complete end-to-end data analytics pipeline to evaluate vendor performance using Python, SQL, SQLite, and Power BI. The objective was to transform raw transactional data into actionable business insights by creating a structured database, engineering key performance indicators (KPIs), and developing an interactive business intelligence dashboard.

The project simulates a real-world business scenario where organizations need to monitor vendor efficiency, profitability, and inventory performance to support data-driven decision making.

---

## Business Problem

Organizations working with multiple vendors need to answer critical questions:

- Which vendors contribute most to revenue?
- Which vendors are most profitable?
- Which vendors have inefficient inventory turnover?
- Are there high-potential vendors with strong margins but low sales?

This project provides a scalable data pipeline and dashboard to answer these questions.

---

## Data Pipeline Architecture

Raw CSV Files → Python Ingestion Pipeline → SQLite Database → SQL Aggregation → KPI Engineering → Statistical Analysis → Power BI Dashboard

---

## Key Responsibilities and Implementation

### 1. Data Ingestion and Database Creation

Developed a scalable ingestion pipeline using Python and SQLAlchemy to:

- Load multiple large CSV datasets efficiently
- Transform and ingest raw data into a centralized SQLite database
- Automate ingestion using reusable functions
- Implement logging for monitoring and debugging

This simulates real-world ETL workflows used in production environments.

---

### 2. Data Aggregation using SQL

Designed SQL queries with joins and aggregations to create vendor-level summary tables.

Aggregations included:

- Total Sales
- Total Purchase Value
- Total Quantity Sold and Purchased
- Freight Costs

This ensured analysis was performed at the correct business grain.

---

### 3. KPI Engineering using Python

Created business-critical performance metrics, including:

- Gross Profit  
- Profit Margin (%)  
- Stock Turnover Ratio  
- Sales-to-Purchase Ratio  

These KPIs enabled accurate vendor performance evaluation.

---

### 4. Statistical Analysis

Performed statistical analysis to validate vendor performance differences:

- Confidence Interval Analysis
- Hypothesis Testing (T-test)
- Vendor performance segmentation

This demonstrates ability to apply statistical thinking to business problems.

---

### 5. Exploratory Data Analysis (EDA)

Identified patterns and performance drivers, including:

- High-performing vendors
- Low-performing vendors
- Vendors with high margins but low sales (growth opportunity)
- Vendor contribution distribution

---

### 6. Business Intelligence Dashboard (Power BI)

Built an interactive Power BI dashboard to visualize vendor performance.

Dashboard features:

- Vendor revenue contribution analysis
- Profitability comparison
- Brand-level performance analysis
- Target vendor identification
- Inventory efficiency analysis

The dashboard enables stakeholders to make informed business decisions.

---

## Tools and Technologies

Python  
Pandas, NumPy  
SQL  
SQLite  
SQLAlchemy  
Power BI  
Jupyter Notebook  
Git and GitHub  

---

## Key Business Insights Generated

- Identified top vendors driving majority of revenue
- Detected vendors with high profitability but low sales, representing growth opportunities
- Identified vendors with inefficient inventory turnover
- Enabled vendor performance comparison across multiple business dimensions

---

## Skills Demonstrated

Data Ingestion and ETL Pipeline Development  
SQL Data Aggregation and Database Design  
Feature Engineering and KPI Development  
Statistical Analysis and Hypothesis Testing  
Business Intelligence Dashboard Development  
End-to-End Data Analytics Workflow  

---

## Project Structure
Vendor-Performance-Analytics/

├── README.md  
├── ingestion_db.py  
├── notebooks/  
│   ├── 01_ingestion.ipynb  
│   ├── 02_EDA.ipynb  
│   ├── 03_get_vendor_summary.ipynb  
│   └── 04_Vendor performance analysis.ipynb  
└── vendorperformancedashboard.pbix
---

## Outcome

Successfully developed a production-style analytics pipeline and dashboard to evaluate vendor performance, demonstrating the complete data analytics lifecycle from raw data ingestion to business insight generation.

---
BY- jayesh Suthar
