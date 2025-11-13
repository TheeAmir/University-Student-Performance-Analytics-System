# University-Student-Performance-Analytics-System
Analyze and visualize student performance data across multiple sections to identify trends in grades, attendance, and overall academic success.

### 🧩 **Dataset**

Each record represents a student with the following columns:

- `Student_ID`
- `Name`
- `Section`
- `Attendance_%`
- `Midterm`
- `Final`
- `Assignments`
- *(You’ll later calculate)* → `Final_Grade`, `Pass/Fail`

---

### 🧠 **Tasks**

1. **Data Generation / Loading**
    - Create or load student data (around 30–50 students).
    - Use **NumPy** to generate random but realistic marks and attendance values.
2. **Data Cleaning**
    - Handle missing or duplicate values.
    - Ensure numeric columns have correct data types.
3. **Feature Engineering**
    - Compute weighted **Final Grade** using Midterm, Final, and Assignments.
    - Add **Pass/Fail** column based on grade threshold (e.g., 60%).
4. **Statistical Analysis**
    - Find average, median, and standard deviation of grades.
    - Compare **section-wise performance** (A, B, C).
    - Find correlation between **attendance and grades**.
5. **Visualizations (Matplotlib)**
    - Histogram of final grades
    - Bar chart: average grade per section
    - Scatter plot: attendance vs final grade
6. **Business / Academic Insights**
    - Which section performed best?
    - Does higher attendance lead to better grades?
    - What percentage of students passed or failed?
7. **Export**
    - Save the cleaned and processed dataset to CSV.
