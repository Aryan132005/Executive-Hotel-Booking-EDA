# 🏨 Executive Hotel Booking EDA – Day 15

## 📌 Description

This project performs a complete Exploratory Data Analysis (EDA) on a large hotel booking dataset using Python, Pandas, Matplotlib, and Seaborn.

The analysis focuses on hotel bookings, revenue, room pricing, cancellations, customer satisfaction, market segments, hotel types, and locations.

## ✨ Analysis Performed

- Loaded and inspected the hotel booking dataset
- Checked dataset shape, columns, and data types
- Checked missing values
- Checked duplicate records
- Converted date columns to DateTime format
- Handled missing values
- Checked inconsistent categorical values
- Identified potential outliers using the IQR method
- Created useful features such as:
  - Arrival Year
  - Arrival Month
  - Arrival Day
  - Day of Week
  - Total Guests
  - Revenue Per Night
- Generated descriptive statistics
- Performed univariate analysis
- Performed bivariate analysis
- Performed hotel type analysis
- Performed location analysis
- Performed market segment analysis
- Performed customer type analysis
- Performed room type analysis
- Performed monthly analysis
- Analyzed cancellation patterns
- Performed correlation analysis
- Created different visualizations
- Generated business insights
- Provided management recommendations

## 🛠️ Technologies Used

- Python 3
- Pandas
- NumPy
- Matplotlib
- Seaborn
- Google Colab
- CSV

## 📂 Project Structure

```text
Executive-Hotel-Booking-EDA/
│
├── Day15_Executive_Hotel_Booking_EDA_Dataset.csv
├── Day15_Executive_Hotel_Booking_EDA.ipynb
└── README.md  

▶️ How to Run
1. Upload the Dataset

Upload the following CSV file to Google Colab:

Day15_Executive_Hotel_Booking_EDA_Dataset.csv
2. Install Required Libraries
pip install pandas numpy matplotlib seaborn
3. Load the Dataset
import pandas as pd

df = pd.read_csv("Day15_Executive_Hotel_Booking_EDA_Dataset.csv")
4. Run the Notebook

Run all the cells in Google Colab to perform the complete hotel booking analysis.

📊 Key Analysis Areas
Hotel Type
Hotel Location
Market Segment
Customer Type
Room Type
Booking Status
Cancellation Rate
Revenue
Average Daily Rate (ADR)
Lead Time
Customer Satisfaction
Number of Guests
Monthly Booking Trends
📈 Visualizations

The notebook includes:

Revenue distribution
ADR distribution
Cancellation count plot
Revenue by hotel type
Revenue by hotel location
Revenue by market segment
ADR vs Revenue scatter plot
Lead time vs cancellation box plot
Customer satisfaction by hotel type
Top customer countries
Correlation heatmap
🔍 Key Business Insights

The analysis identifies:

The hotel type generating the highest revenue.
The highest-revenue hotel location.
The most profitable market segment.
The hotel type with the highest cancellation rate.
The hotel type with the highest customer satisfaction.
💡 Management Recommendations
Focus marketing efforts on high-performing hotel types and locations.
Develop strategies to reduce booking cancellations.
Optimize room prices based on demand and historical ADR.
Improve performance of underperforming market segments.
Monitor customer satisfaction regularly.
Encourage booking channels that provide better revenue.
Use booking lead-time patterns for early-booking and last-minute offers.
🎯 Learning Outcome

This project demonstrates a complete EDA workflow using Python and Pandas. It provides practical experience in data cleaning, descriptive analysis, group-wise analysis, correlation analysis, data visualization, business insights, and management recommendations.
