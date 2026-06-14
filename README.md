# 🏠 California Real Estate Market Analysis

An end-to-end data analytics project that uses Python to transform a large raw California residential real estate dataset into an interactive Tableau dashboard. The project focuses on data cleaning, feature engineering, exploratory analysis, and dashboard design to demonstrate a complete business intelligence workflow. A Santa Clara County market analysis is included as a case study showing how the cleaned dataset can be used to generate actionable market insights.

---

## Project Overview

Real estate transaction datasets often contain inconsistent formatting, duplicate records, missing values, and fields that are not immediately useful for analysis. This project demonstrates the full analytics pipeline, from preparing raw MLS data to building professional Tableau dashboards for business decision-making.

The final deliverables include:

- Cleaned and transformed housing dataset
- Feature engineering for analytical metrics
- Interactive Tableau dashboards
- A market intelligence report
- A presentation summarizing key findings

Rather than focusing on predictive modeling, this project emphasizes the data preparation and visualization process that supports business intelligence.

---

## Dataset

The project uses California residential MLS transaction data containing property, pricing, location, and listing information.

Key variables include:

- Listing and sold prices
- Listing and purchase dates
- Property characteristics
- Square footage
- Days on market
- Sale-to-list price ratio
- City and county
- Listing brokerage
- Agent information

The original dataset required extensive cleaning before analysis.

---

## Data Cleaning & Preparation

The majority of the project consisted of transforming raw MLS data into an analysis-ready dataset.

Cleaning steps included:

- Removing duplicate listings
- Handling missing and invalid values
- Standardizing city and county names
- Converting date fields into usable formats
- Creating Year-Month time variables
- Formatting currency and numeric fields
- Engineering business metrics including:
  - Price per square foot
  - Sale-to-list price ratio
  - Closed sales counts
- Creating calculated fields for Tableau visualizations
- Preparing the dataset for dashboard interactivity

---

## Tableau Dashboard

The cleaned dataset was used to build an interactive Tableau dashboard that allows users to explore housing market performance across California.

Dashboard features include:

- Overall market summary
- Monthly pricing trends
- Sales volume trends
- Geographic comparisons by city
- Competitive brokerage analysis
- Interactive filters for county and city selection
- Dynamic KPIs and summary metrics

The dashboard enables users to drill into specific markets while maintaining a statewide perspective.

The dashboards can be found under "santaclara_analysis", "market_analysis", "competitive_analysis_1", and "competitive_analysis_2" here: https://public.tableau.com/app/profile/cynthia.gao6184/vizzes

---

## Santa Clara County Case Study

To demonstrate how the cleaned dataset can support business analysis, the project includes a market intelligence case study focused on Santa Clara County.

The analysis examines:

- Overall market conditions
- Price trends over time
- Geographic variation across cities
- Competitive landscape among listing brokerages
- Business implications for real estate professionals

This case study illustrates how the dashboard can be used to generate actionable insights for a specific local market.

---

## Key Insights

### Market Performance

- Median sold price remained around **$1.6M**
- Homes sold quickly with a median of **9 days on market**
- Properties sold for approximately **5% above asking price**
- Transaction volume declined after Spring 2024 while prices remained relatively stable

### Geographic Differences

- Significant pricing variation exists across cities
- Premium markets include Monte Sereno, Stanford, and Los Altos
- Moderately priced cities such as Sunnyvale and Cupertino experienced some of the fastest sales
- Santa Clara County functions as a collection of distinct local submarkets rather than one uniform market

### Competitive Landscape

- Listing activity is concentrated among a small number of large brokerages
- Compass, Intero Real Estate Services, and Coldwell Banker Realty account for a substantial share of transactions
- Smaller firms compete by leveraging local expertise and specialized market knowledge

---

## Technologies Used

- **Python**
  - pandas
  - NumPy
- **Tableau Public**
- **Jupyter Notebook**
- **Git & GitHub**

---

## Repository Structure

```text
.
├── IDX Files/
│   ├── functions/
│   │   ├── data_cleaning_functions.py
│   │   ├── feature_engineering_functions.py
│   │   ├── outlier_functions.py
│   │   ├── plots_functions.py
│   │   └── stats_summary_functions.py
│   │
│   ├── EDA_combined.ipynb
│   ├── SantaClara_analysis.ipynb
│   ├── append_listed.py
│   ├── append_sold.py
│   ├── santaclara_analysis.twbx
│   └── Cynthia Gao - IDX Exchange Market Analysis.pdf
│
├── README.md
└── requirements.txt
```

### Repository Contents

- **functions/** – Modular Python functions used throughout the project for data cleaning, feature engineering, outlier detection, statistical summaries, and visualization.
- **EDA_combined.ipynb** – Main notebook containing data cleaning, exploratory data analysis (EDA), and preparation of the California housing dataset.
- **SantaClara_analysis.ipynb** – Notebook containing the Santa Clara County market intelligence analysis and business insights.
- **append_listed.py** – Script used to merge and process listed property datasets.
- **append_sold.py** – Script used to merge and process sold property datasets.
- **santaclara_analysis.twbx** – Tableau workbook containing the interactive dashboard and visualizations.
- **Cynthia Gao - IDX Exchange Market Analysis.pdf** – Final market intelligence report and presentation deliverable.

---

## Skills Demonstrated

- Data cleaning
- Data transformation
- Feature engineering
- Exploratory data analysis
- Business intelligence
- Dashboard development
- Data visualization
- Market analysis
- Business communication
- Tableau dashboard design

---

## Future Improvements

Potential enhancements include:

- Automated ETL pipeline
- Predictive modeling for home prices
- Time-series forecasting
- Additional county comparisons
- Neighborhood-level analysis
- Interactive map visualizations
- Deployment through Tableau Public

---

## Author

**Cynthia Gao**

- LinkedIn: https://www.linkedin.com/in/cynthiaqgao/
