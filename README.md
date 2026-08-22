# 🏨 Executive Hotel Booking EDA Report – Day 15

## 📌 Description

This project presents a complete Exploratory Data Analysis (EDA) of a large Hotel Booking Dataset using Python, Pandas, Matplotlib, and Seaborn.

The main objective of this project is to understand hotel booking patterns, revenue performance, cancellations, customer behavior, room pricing, market segments, customer satisfaction, and other important business factors.

The project follows an end-to-end data science workflow including data inspection, data quality assessment, data cleaning, preprocessing, exploratory analysis, visualization, correlation analysis, business insights, and management recommendations.

## 🎯 Objectives

The main objectives of this project are:

- Understand the hotel booking dataset
- Inspect the structure and quality of the data
- Identify missing values
- Identify duplicate records
- Check incorrect data types
- Check inconsistent categorical values
- Identify potential outliers
- Clean and preprocess the dataset
- Perform descriptive statistical analysis
- Perform univariate analysis
- Perform bivariate analysis
- Perform group-wise analysis
- Analyze hotel booking trends
- Analyze revenue and room pricing
- Analyze cancellation behavior
- Analyze customer satisfaction
- Perform correlation analysis
- Create meaningful visualizations
- Identify key business insights
- Provide practical recommendations for management

## 🛠️ Technologies Used

- Python 3
- Pandas
- NumPy
- Matplotlib
- Seaborn
- Google Colab
- Jupyter Notebook
- CSV

## 📂 Dataset

The dataset used for this project is:

```text
Day15_Executive_Hotel_Booking_EDA_Dataset.csv
```

The dataset contains detailed hotel booking information including:

- Hotel Type
- Hotel Location
- Booking Date
- Arrival Date
- Lead Time
- Number of Guests
- Room Type
- Market Segment
- Distribution Channel
- Deposit Type
- Customer Type
- Meal Type
- ADR
- Estimated Revenue
- Reservation Status
- Satisfaction Score
- Cancellation Information

## 📂 Project Structure

```text
Executive-Hotel-Booking-EDA/
│
├── Day15_Executive_Hotel_Booking_EDA_Dataset.csv
├── Day15_Executive_Hotel_Booking_EDA.ipynb
└── README.md
```

## ▶️ How to Run

### Step 1: Open Google Colab

Open Google Colab and create a new notebook.

### Step 2: Upload the Dataset

Upload the following CSV file:

```text
Day15_Executive_Hotel_Booking_EDA_Dataset.csv
```

### Step 3: Import Required Libraries

```python
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
```

### Step 4: Load the Dataset

```python
df = pd.read_csv(
    "Day15_Executive_Hotel_Booking_EDA_Dataset.csv"
)

print(df.head())
```

### Step 5: Run the Notebook

Run all notebook cells to perform the complete hotel booking EDA and generate the visualizations, insights, and recommendations.

## 🔍 Data Quality Analysis

The dataset was checked for common data quality problems.

### Missing Values

Missing values were identified using:

```python
df.isnull().sum()
```

Appropriate methods were used to handle missing values, including:

- Median imputation for numerical values
- Mode imputation for categorical values
- Appropriate default values for unavailable IDs

### Duplicate Records

Duplicate records were identified using:

```python
df.duplicated().sum()
```

Duplicate records were removed using:

```python
df.drop_duplicates()
```

### Data Types

Data types were inspected and date columns were converted to DateTime format.

```python
df["Booking_Date"] = pd.to_datetime(
    df["Booking_Date"],
    errors="coerce"
)
```

### Inconsistent Values

Categorical columns were inspected using unique values to identify inconsistent or unexpected entries.

## 🧹 Data Cleaning and Preprocessing

The following cleaning steps were performed:

- Checked missing values
- Handled missing numerical values
- Handled missing categorical values
- Removed duplicate records
- Converted date columns to DateTime
- Checked categorical values
- Identified potential outliers
- Created useful analytical features

## 📅 Feature Engineering

Additional features were created from the booking and arrival dates.

Examples include:

```python
df["Arrival_Year"] = df["Arrival_Date"].dt.year

df["Arrival_Month"] = df["Arrival_Date"].dt.month

df["Arrival_Day"] = df["Arrival_Date"].dt.day

df["Arrival_Day_Name"] = (
    df["Arrival_Date"].dt.day_name()
)
```

A total guest feature was also created:

```python
df["Total_Guests"] = (
    df["Adults"] +
    df["Children"] +
    df["Babies"]
)
```

Revenue per night was calculated as:

```python
df["Revenue_Per_Night"] = (
    df["Estimated_Revenue"] /
    df["Total_Nights"]
)
```

## 📊 Descriptive Analysis

Descriptive statistics were generated using:

```python
df.describe()
```

Important metrics analyzed include:

- Total bookings
- Total revenue
- Average revenue
- Average ADR
- Average lead time
- Average customer satisfaction
- Cancellation rate
- Total guests

## 🏨 Group-wise Analysis

The dataset was analyzed across different business categories.

### Hotel Type Analysis

Hotel performance was compared based on:

- Number of bookings
- Total revenue
- Average ADR
- Customer satisfaction
- Cancellation rate

### Hotel Location Analysis

Different hotel locations were compared based on:

- Bookings
- Revenue
- ADR
- Satisfaction
- Cancellation rate

### Market Segment Analysis

Market segments were analyzed based on:

- Number of bookings
- Revenue
- ADR
- Cancellation rate

### Customer Type Analysis

Different customer types were compared based on:

- Bookings
- Revenue
- Satisfaction
- Cancellation rate

### Room Type Analysis

Room types were analyzed based on:

- Bookings
- Revenue
- ADR
- Customer satisfaction

## 📈 Data Visualizations

The project includes several visualizations to communicate important findings.

### Revenue Distribution

A histogram is used to understand the distribution of estimated revenue.

### ADR Distribution

A histogram is used to understand room pricing patterns.

### Cancellation Distribution

A count plot compares canceled and non-canceled bookings.

### Revenue by Hotel Type

A bar chart compares total revenue across different hotel types.

### Revenue by Location

A bar chart compares revenue across hotel locations.

### Revenue by Market Segment

A bar chart shows the contribution of different market segments.

### ADR vs Revenue

A scatter plot is used to analyze the relationship between Average Daily Rate and Estimated Revenue.

### Lead Time vs Cancellation

A box plot compares booking lead times between canceled and non-canceled bookings.

### Customer Satisfaction by Hotel Type

A box plot compares customer satisfaction across hotel types.

### Top Customer Countries

A bar chart identifies the countries contributing the highest number of bookings.

### Correlation Heatmap

A correlation heatmap is used to identify relationships between numerical variables.

## 🔥 Correlation Analysis

Correlation analysis was performed on numerical variables to understand relationships between important hotel business metrics.

Important variables include:

- Lead Time
- Total Nights
- ADR
- Estimated Revenue
- Total Guests
- Satisfaction Score
- Cancellation Status

The correlation matrix helps identify positive and negative relationships between variables.

Example:

```python
correlation = df.select_dtypes(
    include="number"
).corr()

sns.heatmap(
    correlation,
    cmap="coolwarm"
)
```

## 💡 Key Business Insights

The analysis identifies the following important business insights:

1. The hotel type generating the highest total revenue can be identified from the hotel-wise performance analysis.

2. The location generating the highest revenue can be identified through location-wise analysis.

3. The highest-performing market segment contributes significantly to overall hotel revenue.

4. Hotel types with higher cancellation rates require better cancellation-prevention strategies.

5. Customer satisfaction varies between hotel types and can be used to identify areas for service improvement.

## 📌 Management Recommendations

Based on the EDA, the following recommendations can be considered:

### 1. Focus on High-Performing Locations

Management should focus marketing and operational resources on locations that consistently generate higher revenue.

### 2. Reduce Booking Cancellations

Hotels should analyze high-cancellation segments and introduce suitable cancellation policies, reminders, and flexible booking options.

### 3. Optimize Room Pricing

Historical ADR and booking patterns can be used to create better pricing strategies during high- and low-demand periods.

### 4. Improve Underperforming Market Segments

Low-performing market segments should be analyzed further and targeted with customized offers and promotional campaigns.

### 5. Improve Customer Satisfaction

Management should monitor customer satisfaction regularly and identify the practices followed by high-performing hotel types.

### 6. Optimize Booking Channels

Booking channels should be evaluated based on revenue, cancellation rate, and customer behavior to identify the most effective channels.

### 7. Use Lead-Time Patterns

Lead-time information can be used to create early-booking discounts, advance reservation campaigns, and last-minute pricing strategies.

## 📋 Pandas Operations Used

The following Pandas operations were used throughout the project:

```python
df.head()
df.shape
df.columns
df.dtypes
df.info()
df.describe()
df.isnull().sum()
df.duplicated()
df.drop_duplicates()
df.groupby()
df.agg()
df.sort_values()
df.value_counts()
pd.to_datetime()
```

## 📊 Key Metrics

The analysis focuses on the following business metrics:

| Metric | Purpose |
|---|---|
| Total Bookings | Measures overall booking volume |
| Total Revenue | Measures overall revenue generation |
| Average Revenue | Measures average booking revenue |
| ADR | Measures average daily room rate |
| Lead Time | Measures how early customers book |
| Cancellation Rate | Measures booking cancellations |
| Total Guests | Measures customer volume |
| Satisfaction Score | Measures customer satisfaction |

## 🎯 Learning Outcomes

This project demonstrates a complete **end-to-end Exploratory Data Analysis workflow** using Python.

The project provides practical experience in:

- Data loading
- Data inspection
- Data quality assessment
- Missing value handling
- Duplicate handling
- Data type conversion
- Outlier analysis
- Feature engineering
- Descriptive statistics
- Univariate analysis
- Bivariate analysis
- Group-wise analysis
- Correlation analysis
- Data visualization
- Business insight generation
- Management recommendations

## 📌 Conclusion

This project demonstrates how Exploratory Data Analysis can be used to convert a large hotel booking dataset into meaningful business information.

The analysis helps management understand booking behavior, revenue performance, pricing patterns, cancellation trends, customer satisfaction, and market segment performance.

The identified insights and recommendations can support better decisions related to pricing, marketing, customer experience, booking channels, and revenue management.
