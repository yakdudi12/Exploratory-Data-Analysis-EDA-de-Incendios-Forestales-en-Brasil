---

# Exploratory Data Analysis (EDA) of Forest Fires in Brazil  
This project aims to analyze forest fires recorded in Brazil over a given period. A Python class called `EDA` was developed to perform a detailed exploratory analysis of the dataset, generating relevant visualizations and statistics.  

---  
The data was obtained from the official website of the Brazilian government.  

Kaggle dataset: amazon.csv  

---  

## Table of Contents  
1. [Project Description](#project-description)  
2. [Dataset Description](#dataset-description)  
3. [Main Functions](#main-functions)  
4. [Generated Visualizations](#generated-visualizations)  
5. [How to Run the Code](#how-to-run-the-code)  
6. [System Requirements](#system-requirements)  
7. [Author](#author)  

---  

## Project Description  

The analysis addresses key questions about forest fires in Brazil, such as:  
- Total fires recorded during the analyzed period.  
- Year and state with the highest number of fires.  
- Temporal and monthly fire trends.  
- Comparison between the states with the most and least fires.  

Methods were developed in the `EDA` class to automate the analysis and generate visualizations that facilitate data interpretation.  

---  

## Dataset Description  

The dataset contains information on forest fires recorded in Brazil. Below are some important details:  
- **Observations**: Each row represents a record of fires in a Brazilian state during a specific month and year.  
- **Main Variables**:  
  - `state`: Brazilian state where the fire occurred.  
  - `month`: Month when the fires were recorded.  
  - `year`: Year of the record.  
  - `number`: Number of fires recorded.  
- **Value Ranges**:  
  - `state`: Names of Brazilian states.  
  - `month`: Months of the year (January to December).  
  - `year`: Years within the dataset's range.  
  - `number`: Number of fires (positive numerical value).  

---  

## Main Functions  

The `EDA` class contains the following methods for exploratory analysis:  

1. **show_columns_types**  
   Displays information about columns, their data types, and missing values.  

2. **missing_values**  
   Identifies missing values in the dataset and visualizes them with a heatmap.  

3. **detect_duplicates**  
   Detects and removes duplicate rows in the dataset.  

4. **forest_fires_year**  
   Calculates the total number of fires recorded and the years covered by the data.  

5. **wildfire_season**  
   Identifies the year with the most fires and generates a line plot with the monthly distribution.  

6. **wildfire_months**  
   Displays a histogram of the total number of fires for each month, aggregating all years.  

7. **fire_state**  
   Identifies the state with the most fires and visualizes the total fires accumulated by state.  

8. **year_register**  
   Generates a box plot to analyze the distribution of fires by year.  

9. **most_fire_state**  
   Shows the monthly evolution of fires for the state with the highest number of records.  

10. **diference_fire_state**  
    Compares the states with the most and least fires, plotting their temporal trends and the absolute difference between them.  

---  

## Generated Visualizations  

The analysis generates the following charts:  

1. **Heatmap of missing values**  
   Visual representation of columns with missing data.  

2. **Line plot**  
   Monthly distribution of fires for the year with the most records.  

3. **Cumulative histogram**  
   Total number of fires by month for all years.  

4. **Bar plot by state**  
   States ranked by the total number of fires recorded.  

5. **Annual box plot**  
   Analysis of the distribution of fires for each year.  

6. **State comparison**  
   Plot showing the temporal evolution of fires in the states with the most and least records, including the absolute difference between them.  

---  

## How to Run the Code  

1. Ensure you have Python 3.8 or higher installed on your system.  
2. Install the required dependencies using `pip`:  
   ```bash  
   pip install pandas matplotlib seaborn  
   ```  
3. Download the dataset file (`amazon.csv`) and place it in the same directory as the code.  
4. Run the main script:  
   ```bash  
   python main.py  
   ```  

---  

## System Requirements  

- **Python**: 3.8 or higher.  
- **Libraries**:  
  - `pandas`  
  - `matplotlib`  
  - `seaborn`  
  - `sqlite3` (for optional SQL queries)  

---  

## Author  

**Britez, C. Santiago Luis**  
Data Analyst and Data Scientist  
LinkedIn: [www.linkedin.com/in/santiago-luis-britez-101a8a217](https://www.linkedin.com/in/santiago-luis-britez-101a8a217)  

---  
