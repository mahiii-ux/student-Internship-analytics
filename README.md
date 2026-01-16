# student-Internship-analytics
# Internship Analytics Project – Wide Softech

End‑to‑end **Intern Data Analysis** project built during my 6‑month internship at **Wide Softech**.  
Goal: Clean messy Excel data, load it into MySQL, analyze with SQL, and build a Power BI dashboard for business insights.

---

# 📌 Project Summary

- Cleaned raw **Excel** student internship data using **Python + Pandas**
- Standardised columns, fixed **missing values**, **dates**, and **data types**
- Loaded cleaned data into a **MySQL** database (`Intern_Data` table)
- Wrote **SQL queries** to answer key business questions (top colleges, domains, locations, status, etc.)
- Built an interactive **Power BI dashboard** for management

---

# 🛠 Tech Stack

- **Language:** Python  
- **Libraries:** Pandas, SQLAlchemy, PyMySQL, dateutil  
- **Database:** MySQL  
- **Query Language:** SQL  
- **Visualization:** Power BI  
- **Other:** Excel, Git, GitHub  

---

# 🔄 Workflow

1. **Data Cleaning (Python)**
   - Rename columns → lowercase + underscores  
   - Drop empty columns  
   - Fill missing values with labels like `"Not Provided"`  
   - Convert `pass_out_year`, `contect_no` to numeric  
   - Standardise `enquiry_date` to `YYYY-MM-DD`  

2. **Data Loading (MySQL)**
   - Create database (e.g. `internship_db`)  
   - Upload `cleaned_data.xlsx` to table **`Intern_Data`** via Python  
   - Create index on `contect_no` for faster search  

3. **Analysis (SQL)**
   - Top contributing colleges  
   - Students by city (e.g. Nagpur)  
   - Most popular internship domains  
   - Internship status breakdown (Completed / Ongoing / Not Provided)  
   - Duplicate students by contact number  
   - Students graduating in 2024–2025  

4. **Dashboard (Power BI)**
   - KPIs: total enquiries, total students, completion rate, peak month  
   - Visuals: students by college, branch, city, month, domain, status, gender  

![Internship Analytics Dashboard](dashboard/internship_analytics_dashboard.png)

---

# 🚀 How to Use

```bash
# Clone
git clone https://github.com/<your-username>/<your-repo-name>.git
cd <your-repo-name>

# Install Python dependencies
pip install -r requirements.txt
