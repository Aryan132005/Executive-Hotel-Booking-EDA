import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Load Dataset
df = pd.read_csv("Day15_Executive_Hotel_Booking_EDA_Dataset.csv")

print("===== EXECUTIVE HOTEL BOOKING EDA =====")

# 1. Dataset Overview
print("\n===== DATASET OVERVIEW =====")
print("Rows:", df.shape[0])
print("Columns:", df.shape[1])

print("\nFirst 5 Rows:")
print(df.head())

print("\nColumn Names:")
print(df.columns.tolist())

print("\nData Types:")
print(df.dtypes)

# 2. Data Quality Check
print("\n===== MISSING VALUES BEFORE CLEANING =====")
print(df.isnull().sum())

print("\nTotal Missing Values:",
      df.isnull().sum().sum())

print("\nDuplicate Rows:")
print(df.duplicated().sum())

# 3. Convert Date Columns
date_columns = [
    "Booking_Date",
    "Arrival_Date",
    "Reservation_Status_Date"
]

for column in date_columns:
    df[column] = pd.to_datetime(
        df[column],
        errors="coerce"
    )

print("\n===== DATE COLUMNS CONVERTED =====")
print(df[date_columns].dtypes)

# 4. Handle Missing Values
print("\n===== CLEANING MISSING VALUES =====")

# Children - median
df["Children"] = df["Children"].fillna(
    df["Children"].median()
)

# Agent and Company IDs - 0 means unavailable
df["Agent_ID"] = df["Agent_ID"].fillna(0)
df["Company_ID"] = df["Company_ID"].fillna(0)

# Satisfaction - median
df["Satisfaction_Score"] = df["Satisfaction_Score"].fillna(
    df["Satisfaction_Score"].median()
)

# Categorical columns
categorical_columns = df.select_dtypes(
    include="object"
).columns

for column in categorical_columns:
    if df[column].isnull().sum() > 0:
        df[column] = df[column].fillna(
            df[column].mode()[0]
        )

# Remove duplicate records
df = df.drop_duplicates()

print("Missing values after cleaning:",
      df.isnull().sum().sum())

print("Duplicate rows after cleaning:",
      df.duplicated().sum())

# 5. Check Inconsistent Values
print("\n===== UNIQUE CATEGORICAL VALUES =====")

for column in [
    "Hotel_Type",
    "Hotel_Location",
    "Market_Segment",
    "Distribution_Channel",
    "Deposit_Type",
    "Customer_Type",
    "Meal_Type",
    "Reservation_Status"
]:
    print("\n", column)
    print(df[column].unique())

# 6. Descriptive Statistics
print("\n===== DESCRIPTIVE STATISTICS =====")
print(df.describe())

# 7. Create Useful Features
df["Arrival_Year"] = df["Arrival_Date"].dt.year
df["Arrival_Month"] = df["Arrival_Date"].dt.month
df["Arrival_Month_Name"] = df["Arrival_Date"].dt.month_name()
df["Arrival_Day"] = df["Arrival_Date"].dt.day
df["Arrival_Day_Name"] = df["Arrival_Date"].dt.day_name()

df["Total_Guests"] = (
    df["Adults"] +
    df["Children"] +
    df["Babies"]
)

df["Revenue_Per_Night"] = (
    df["Estimated_Revenue"] /
    df["Total_Nights"].replace(0, np.nan)
)

print("\n===== NEW FEATURES CREATED =====")
print(df[
    [
        "Arrival_Year",
        "Arrival_Month",
        "Total_Guests",
        "Revenue_Per_Night"
    ]
].head())

# 8. Outlier Analysis
print("\n===== OUTLIER ANALYSIS =====")

numeric_columns = [
    "Lead_Time_Days",
    "Total_Nights",
    "ADR",
    "Estimated_Revenue",
    "Total_Guests",
    "Satisfaction_Score"
]

for column in numeric_columns:
    Q1 = df[column].quantile(0.25)
    Q3 = df[column].quantile(0.75)

    IQR = Q3 - Q1

    lower = Q1 - 1.5 * IQR
    upper = Q3 + 1.5 * IQR

    outliers = (
        (df[column] < lower) |
        (df[column] > upper)
    ).sum()

    print(column, "Outliers:", outliers)

# 9. Overall Business Statistics
print("\n===== OVERALL BUSINESS STATISTICS =====")

print("Total Bookings:", len(df))
print("Total Revenue:",
      round(df["Estimated_Revenue"].sum(), 2))

print("Average Revenue:",
      round(df["Estimated_Revenue"].mean(), 2))

print("Average ADR:",
      round(df["ADR"].mean(), 2))

print("Average Lead Time:",
      round(df["Lead_Time_Days"].mean(), 2))

print("Average Satisfaction:",
      round(df["Satisfaction_Score"].mean(), 2))

print("Cancellation Rate:",
      round(df["Is_Canceled"].mean() * 100, 2), "%")

# 10. Hotel Type Analysis
print("\n===== HOTEL TYPE ANALYSIS =====")

hotel_summary = df.groupby("Hotel_Type").agg(
    Bookings=("Booking_ID", "count"),
    Revenue=("Estimated_Revenue", "sum"),
    Average_ADR=("ADR", "mean"),
    Average_Satisfaction=("Satisfaction_Score", "mean"),
    Cancellation_Rate=("Is_Canceled", "mean")
)

hotel_summary["Cancellation_Rate"] *= 100

print(hotel_summary.sort_values(
    "Revenue",
    ascending=False
))

# 11. Location Analysis
print("\n===== LOCATION ANALYSIS =====")

location_summary = df.groupby(
    "Hotel_Location"
).agg(
    Bookings=("Booking_ID", "count"),
    Revenue=("Estimated_Revenue", "sum"),
    Average_ADR=("ADR", "mean"),
    Average_Satisfaction=("Satisfaction_Score", "mean"),
    Cancellation_Rate=("Is_Canceled", "mean")
)

location_summary["Cancellation_Rate"] *= 100

print(location_summary.sort_values(
    "Revenue",
    ascending=False
))

# 12. Market Segment Analysis
print("\n===== MARKET SEGMENT ANALYSIS =====")

segment_summary = df.groupby(
    "Market_Segment"
).agg(
    Bookings=("Booking_ID", "count"),
    Revenue=("Estimated_Revenue", "sum"),
    Average_ADR=("ADR", "mean"),
    Cancellation_Rate=("Is_Canceled", "mean")
)

segment_summary["Cancellation_Rate"] *= 100

print(segment_summary.sort_values(
    "Revenue",
    ascending=False
))

# 13. Customer Type Analysis
print("\n===== CUSTOMER TYPE ANALYSIS =====")

customer_summary = df.groupby(
    "Customer_Type"
).agg(
    Bookings=("Booking_ID", "count"),
    Revenue=("Estimated_Revenue", "sum"),
    Average_Satisfaction=("Satisfaction_Score", "mean"),
    Cancellation_Rate=("Is_Canceled", "mean")
)

customer_summary["Cancellation_Rate"] *= 100

print(customer_summary.sort_values(
    "Revenue",
    ascending=False
))

# 14. Room Type Analysis
print("\n===== ROOM TYPE ANALYSIS =====")

room_summary = df.groupby(
    "Room_Type_Reserved"
).agg(
    Bookings=("Booking_ID", "count"),
    Revenue=("Estimated_Revenue", "sum"),
    Average_ADR=("ADR", "mean"),
    Average_Satisfaction=("Satisfaction_Score", "mean")
)

print(room_summary.sort_values(
    "Revenue",
    ascending=False
))

# 15. Monthly Analysis
print("\n===== MONTHLY PERFORMANCE =====")

monthly_summary = df.groupby(
    "Arrival_Month_Name"
).agg(
    Bookings=("Booking_ID", "count"),
    Revenue=("Estimated_Revenue", "sum"),
    Average_ADR=("ADR", "mean")
)

print(monthly_summary)

# 16. Reservation Status
print("\n===== RESERVATION STATUS =====")
print(df["Reservation_Status"].value_counts())

# 17. Deposit Type Analysis
print("\n===== DEPOSIT TYPE ANALYSIS =====")

deposit_summary = df.groupby(
    "Deposit_Type"
).agg(
    Bookings=("Booking_ID", "count"),
    Revenue=("Estimated_Revenue", "sum"),
    Cancellation_Rate=("Is_Canceled", "mean")
)

deposit_summary["Cancellation_Rate"] *= 100

print(deposit_summary)

# 18. Distribution Channel
print("\n===== DISTRIBUTION CHANNEL =====")

channel_summary = df.groupby(
    "Distribution_Channel"
).agg(
    Bookings=("Booking_ID", "count"),
    Revenue=("Estimated_Revenue", "sum"),
    Average_ADR=("ADR", "mean"),
    Cancellation_Rate=("Is_Canceled", "mean")
)

channel_summary["Cancellation_Rate"] *= 100

print(channel_summary)

# 19. Correlation Analysis
print("\n===== CORRELATION WITH REVENUE =====")

numeric_data = df.select_dtypes(
    include="number"
)

revenue_corr = (
    numeric_data.corr()["Estimated_Revenue"]
    .sort_values(ascending=False)
)

print(revenue_corr.round(2))

# 20. Correlation Matrix
plt.figure(figsize=(14, 10))

correlation = numeric_data.corr()

sns.heatmap(
    correlation,
    cmap="coolwarm",
    annot=False
)

plt.title("Hotel Booking Numerical Correlation Matrix")
plt.tight_layout()
plt.show()

print(
    "Interpretation: The heatmap shows positive and negative relationships "
    "between numerical hotel booking variables."
)

# 21. Univariate Analysis - ADR
plt.figure(figsize=(8, 5))

sns.histplot(
    df["ADR"],
    bins=30,
    kde=True
)

plt.title("Distribution of Average Daily Rate")
plt.xlabel("ADR")
plt.ylabel("Frequency")
plt.tight_layout()
plt.show()

print(
    "Interpretation: This distribution shows the variation in hotel room pricing."
)

# 22. Revenue Distribution
plt.figure(figsize=(8, 5))

sns.histplot(
    df["Estimated_Revenue"],
    bins=30,
    kde=True
)

plt.title("Distribution of Estimated Revenue")
plt.xlabel("Estimated Revenue")
plt.ylabel("Frequency")
plt.tight_layout()
plt.show()

print(
    "Interpretation: This chart shows how booking revenue is distributed."
)

# 23. Cancellation Distribution
plt.figure(figsize=(7, 5))

sns.countplot(
    data=df,
    x="Is_Canceled"
)

plt.title("Booking Cancellation Distribution")
plt.xlabel("Canceled (0 = No, 1 = Yes)")
plt.ylabel("Number of Bookings")
plt.tight_layout()
plt.show()

print(
    "Interpretation: This chart compares completed and canceled bookings."
)

# 24. Hotel Type Revenue
plt.figure(figsize=(8, 5))

sns.barplot(
    data=df,
    x="Hotel_Type",
    y="Estimated_Revenue",
    estimator="sum"
)

plt.title("Total Revenue by Hotel Type")
plt.xlabel("Hotel Type")
plt.ylabel("Total Revenue")
plt.tight_layout()
plt.show()

print(
    "Interpretation: This comparison identifies which hotel type generates more revenue."
)

# 25. Location Revenue
plt.figure(figsize=(8, 5))

sns.barplot(
    data=df,
    x="Hotel_Location",
    y="Estimated_Revenue",
    estimator="sum"
)

plt.title("Total Revenue by Hotel Location")
plt.xlabel("Location")
plt.ylabel("Total Revenue")
plt.tight_layout()
plt.show()

print(
    "Interpretation: Revenue performance varies across hotel locations."
)

# 26. Market Segment
plt.figure(figsize=(10, 5))

sns.barplot(
    data=df,
    x="Market_Segment",
    y="Estimated_Revenue",
    estimator="sum"
)

plt.title("Revenue by Market Segment")
plt.xlabel("Market Segment")
plt.ylabel("Total Revenue")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

print(
    "Interpretation: Different market segments contribute differently to hotel revenue."
)

# 27. ADR vs Revenue
plt.figure(figsize=(8, 5))

sns.scatterplot(
    data=df,
    x="ADR",
    y="Estimated_Revenue",
    hue="Hotel_Type"
)

plt.title("ADR vs Estimated Revenue")
plt.xlabel("Average Daily Rate")
plt.ylabel("Estimated Revenue")
plt.tight_layout()
plt.show()

print(
    "Interpretation: This scatter plot helps identify the relationship "
    "between room pricing and booking revenue."
)

# 28. Lead Time vs Cancellation
plt.figure(figsize=(8, 5))

sns.boxplot(
    data=df,
    x="Is_Canceled",
    y="Lead_Time_Days"
)

plt.title("Lead Time by Cancellation Status")
plt.xlabel("Canceled (0 = No, 1 = Yes)")
plt.ylabel("Lead Time (Days)")
plt.tight_layout()
plt.show()

print(
    "Interpretation: The box plot compares booking lead times between "
    "canceled and non-canceled reservations."
)

# 29. Satisfaction by Hotel Type
plt.figure(figsize=(8, 5))

sns.boxplot(
    data=df,
    x="Hotel_Type",
    y="Satisfaction_Score"
)

plt.title("Customer Satisfaction by Hotel Type")
plt.xlabel("Hotel Type")
plt.ylabel("Satisfaction Score")
plt.tight_layout()
plt.show()

print(
    "Interpretation: Customer satisfaction differs across hotel types."
)

# 30. Top Countries
top_countries = (
    df["Country"]
    .value_counts()
    .head(10)
)

plt.figure(figsize=(10, 5))

top_countries.plot(kind="bar")

plt.title("Top 10 Customer Countries")
plt.xlabel("Country")
plt.ylabel("Number of Bookings")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

print(
    "Interpretation: The chart highlights the countries contributing "
    "the most hotel bookings."
)

# 31. Business Insights
top_hotel = hotel_summary["Revenue"].idxmax()
top_location = location_summary["Revenue"].idxmax()
top_segment = segment_summary["Revenue"].idxmax()
highest_cancel_hotel = hotel_summary["Cancellation_Rate"].idxmax()
highest_satisfaction_hotel = hotel_summary["Average_Satisfaction"].idxmax()
highest_adr_hotel = hotel_summary["Average_ADR"].idxmax()

print("\n===== 5 KEY BUSINESS INSIGHTS =====")

print(
    "1. The hotel type generating the highest revenue is:",
    top_hotel
)

print(
    "2. The highest-revenue hotel location is:",
    top_location
)

print(
    "3. The market segment generating the highest revenue is:",
    top_segment
)

print(
    "4. The hotel type with the highest cancellation rate is:",
    highest_cancel_hotel
)

print(
    "5. The hotel type with the highest customer satisfaction is:",
    highest_satisfaction_hotel
)

# 32. Management Recommendations
print("\n===== 7 MANAGEMENT RECOMMENDATIONS =====")

print(
    "1. Focus marketing and promotional efforts on the highest-revenue "
    "hotel type and location."
)

print(
    "2. Develop targeted cancellation-prevention strategies for segments "
    "with high cancellation rates."
)

print(
    "3. Use historical ADR and demand patterns to optimize room pricing."
)

print(
    "4. Strengthen high-performing market segments while improving "
    "underperforming segments."
)

print(
    "5. Monitor customer satisfaction regularly and replicate practices "
    "from high-satisfaction hotel types."
)

print(
    "6. Encourage direct booking channels where they provide better "
    "revenue and lower cancellation risk."
)

print(
    "7. Use lead-time patterns to design early-booking offers and "
    "last-minute pricing strategies."
)

print("\n===== EXECUTIVE EDA COMPLETED =====")