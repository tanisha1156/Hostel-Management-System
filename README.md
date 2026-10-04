# Hostel Management System

## 📌 Project Description

The Hostel Management System is a Python-based project used to manage and analyze hostel student information.

The system stores student details such as student ID, student name, room number, block, year, hostel fees, attendance, and room status.

It also performs statistical analysis and creates graphs for better understanding of hostel data.

## 🎯 Objectives

- Manage hostel student information.
- Check occupied and available rooms.
- Calculate hostel fee statistics.
- Analyze student attendance.
- Calculate total fee collection.
- Perform statistical analysis.
- Display hostel data using graphs.
- Provide a final hostel summary.

## 🛠️ Technologies Used

- Python
- NumPy
- Pandas
- SciPy
- Matplotlib
- Bokeh

## 📊 Features

### 1. Student Details

The system stores:

- Student ID
- Student Name
- Room Number
- Block
- Year
- Hostel Fees
- Attendance
- Room Status

### 2. NumPy Analysis

The program calculates:

- Total students
- Average hostel fee
- Highest hostel fee
- Lowest hostel fee
- Average attendance
- Highest attendance
- Lowest attendance

### 3. Pandas Analysis

The program displays:

- Occupied rooms
- Available rooms
- Student details of occupied rooms
- Room and block details of available rooms

### 4. Block-Wise Analysis

The system calculates:

- Number of students in each block
- Average fees for each block
- Average attendance for each block

### 5. Fee Collection

The total fee collected from occupied rooms is calculated.

**Total Fee Collection = Sum of Fees of Occupied Rooms**

### 6. SciPy Statistical Analysis

The project performs:

- One-sample t-test
- Pearson correlation

The t-test checks whether average attendance is significantly different from 85%.

### 7. Data Visualization

The project creates:

- Bar graph of hostel fees by student
- Line graph of student attendance
- Interactive Bokeh graph for hostel attendance

## 📈 Sample Results

- Total Students: **10**
- Occupied Rooms: **8**
- Available Rooms: **2**
- Average Hostel Fee: **₹63,200**
- Total Fee Collected: **₹5,10,000**
- Average Attendance: **90.6%**
- Highest Attendance: **Arjun**
- Highest Hostel Fee: **Krish**

The above results are based on the output included in the project PDF. :chatgpt-content-reference{index="1"}

## 📚 Sample Data

| Student | Room | Block | Fees | Attendance | Status |
|---|---:|---|---:|---:|---|| Aarav | 101 | A | ₹60,000 | 92% | Occupied |
| Diya | 102 | A | ₹62,000 | 88% | Occupied |
| Rohan | 103 | A | ₹65,000 | 95% | Occupied |
| Priya | 104 | A | ₹60,000 | 85% | Occupied |
| Krish | 105 | A | ₹68,000 | 90% | Occupied |
| Ananya | 201 | B | ₹62,000 | 87% | Occupied |
| Rahul | 202 | B | ₹65,000 | 93% | Occupied |
| Meera | 203 | B | ₹60,000 | 89% | Available |
| Arjun | 204 | B | ₹68,000 | 96% | Occupied |
| Neha | 205 | B | ₹62,000 | 91% | Available |

