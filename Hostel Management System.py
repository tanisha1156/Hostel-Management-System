import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy import stats
from bokeh.plotting import figure, show
from bokeh.models import ColumnDataSource

print("=" * 70)
print("                  HOSTEL MANAGEMENT SYSTEM")
print("=" * 70)

# --------------------------------------------------
# 1. HOSTEL DATA USING PANDAS
# --------------------------------------------------
hostel_data = {
    "Student_ID": ["S101", "S102", "S103", "S104", "S105", "S106", "S107", "S108", "S109", "S110"],
    "Student_Name": ["Aarav", "Diya", "Rohan", "Priya", "Krish", "Ananya", "Rahul", "Meera", "Arjun", "Neha"],
    "Room_No": [101, 102, 103, 104, 105, 201, 202, 203, 204, 205],
    "Block": ["A", "A", "A", "A", "A", "B", "B", "B", "B", "B"],
    "Year": [1, 2, 3, 1, 4, 2, 3, 1, 4, 2],
    "Fees": [60000, 62000, 65000, 60000, 68000, 62000, 65000, 60000, 68000, 62000],
    "Attendance": [92, 88, 95, 85, 90, 87, 93, 89, 96, 91],
    "Status": ["Occupied", "Occupied", "Occupied", "Occupied", "Occupied", "Occupied", "Occupied", "Available", "Occupied", "Available"]
}

hostel = pd.DataFrame(hostel_data)

print("\nHOSTEL STUDENT DETAILS")
print("-" * 70)
print(hostel.to_string(index=False))

# --------------------------------------------------
# 2. NUMPY ANALYSIS
# --------------------------------------------------
fees = np.array(hostel["Fees"])
attendance = np.array(hostel["Attendance"])

print("\nNUMPY STATISTICS")
print("-" * 70)
print("Total Students:", len(hostel))
print("Average Hostel Fee: ₹", round(np.mean(fees), 2))
print("Highest Hostel Fee: ₹", np.max(fees))
print("Lowest Hostel Fee: ₹", np.min(fees))
print("Average Attendance:", round(np.mean(attendance), 2), "%")
print("Highest Attendance:", np.max(attendance), "%")
print("Lowest Attendance:", np.min(attendance), "%")

# --------------------------------------------------
# 3. PANDAS ANALYSIS
# --------------------------------------------------
print("\nPANDAS ANALYSIS")
print("-" * 70)
occupied = hostel[hostel["Status"] == "Occupied"]
available = hostel[hostel["Status"] == "Available"]

print("\nOccupied Rooms:")
print(occupied[["Student_Name", "Room_No", "Block", "Fees"]].to_string(index=False))

print("\nAvailable Rooms:")
print(available[["Room_No", "Block"]].to_string(index=False))

# --------------------------------------------------
# 4. BLOCK-WISE ANALYSIS
# --------------------------------------------------
block_summary = hostel.groupby("Block").agg(
    Students=("Student_ID", "count"),
    Average_Fees=("Fees", "mean"),
    Average_Attendance=("Attendance", "mean")
)

print("\nBLOCK-WISE ANALYSIS")
print("-" * 70)
print(block_summary.round(2).to_string())

# --------------------------------------------------
# 5. TOTAL FEE COLLECTION
# --------------------------------------------------
total_fee = np.sum(occupied["Fees"])

print("\nFEE COLLECTION")
print("-" * 70)
print("Total Fee Collected from Occupied Rooms: ₹", total_fee)

# --------------------------------------------------
# 6. SCIPY STATISTICAL ANALYSIS
# --------------------------------------------------
print("\nSCIPY STATISTICAL ANALYSIS")
print("-" * 70)
# One sample t-test: Testing whether average attendance is different from 85%
t_statistic, p_value = stats.ttest_1samp(attendance, 85)

print("T-Statistic:", round(t_statistic, 4))
print("P-Value:", round(p_value, 4))

if p_value < 0.05:
    print("Result: Average attendance is significantly different from 85%.")
else:
    print("Result: No significant difference from 85%.")

# --------------------------------------------------
# 7. SCIPY CORRELATION
# --------------------------------------------------
correlation, correlation_p = stats.pearsonr(fees, attendance)

print("\nCorrelation between Hostel Fees and Attendance:")
print("Correlation:", round(correlation, 4))
print("P-Value:", round(correlation_p, 4))

# --------------------------------------------------
# 8. MATPLOTLIB BAR GRAPH
# --------------------------------------------------
plt.figure(figsize=(10, 6))
plt.bar(hostel["Student_Name"], hostel["Fees"])
plt.title("Hostel Fees by Student")
plt.xlabel("Students")
plt.ylabel("Hostel Fee")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# --------------------------------------------------
# 9. MATPLOTLIB LINE GRAPH
# --------------------------------------------------
plt.figure(figsize=(10, 6))
plt.plot(hostel["Student_Name"], hostel["Attendance"], marker="o")
plt.title("Student Hostel Attendance")
plt.xlabel("Students")
plt.ylabel("Attendance (%)")
plt.xticks(rotation=45)
plt.grid(True)
plt.tight_layout()
plt.show()

# --------------------------------------------------
# 10. BOKEH INTERACTIVE GRAPH
# --------------------------------------------------
source = ColumnDataSource(hostel)
bokeh_plot = figure(
    x_range=hostel["Student_Name"].tolist(),
    title="Hostel Attendance - Interactive Bokeh Graph",
    x_axis_label="Students",
    y_axis_label="Attendance (%)",
    width=900,
    height=500
)
bokeh_plot.vbar(x="Student_Name", top="Attendance", width=0.6, source=source)
bokeh_plot.xaxis.major_label_orientation = 0.8
show(bokeh_plot)

# --------------------------------------------------
# 11. FINAL SUMMARY
# --------------------------------------------------
print("\n" + "=" * 70)
print("                     HOSTEL SUMMARY")
print("=" * 70)
print("Total Students:", len(hostel))
print("Occupied Rooms:", len(occupied))
print("Available Rooms:", len(available))
print("Total Fee Collected: ₹", total_fee)
print("Average Hostel Fee: ₹", round(np.mean(fees), 2))
print("Average Attendance:", round(np.mean(attendance), 2), "%")
print("Student with Highest Attendance:", hostel.loc[hostel["Attendance"].idxmax(), "Student_Name"])
print("Student with Highest Hostel Fee:", hostel.loc[hostel["Fees"].idxmax(), "Student_Name"])
print("\nHostel Management System Completed Successfully!")
print("=" * 70)