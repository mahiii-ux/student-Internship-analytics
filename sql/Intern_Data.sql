create database mydb;
grant all privileges on mydb.* to 'root'@'localhost';
Flush privileges;
use mydb;
select * from Intern_Data; 

select college_name ,count(*)  as total_student
from Intern_Data
group by college_name 
order by total_student desc;

SELECT DISTINCT contect_no
FROM Intern_Data;

-- ---Nagpur Students Only
select * 
from Intern_Data
where address='Nagpur';

-- Count of Nagpur students
select COUNT(*) as total_nagpur_students
FROM Intern_Data
WHERE address = 'Nagpur';

-- Unique college_name
select distinct  college_name
from Intern_Data;

-- Not provided student 
select internship_status,count(*)
from Intern_Data
where internship_status= 'Not Provided';

-- Full Stack Developer student


select internship_domian,count(*) as total_student
from Intern_data
where internship_domian ='Full Stack Developer';
-- 
select *
from Intern_Data
where pass_out_year='2025';

select enquiry_date,count(*)
from Intern_Data
where enquiry_date =2025;

select  count(enquiry_date)
FROM Intern_Data
WHERE YEAR(STR_TO_DATE(enquiry_date, '%Y-%m-%d')) = 2025;

select qualification,count(*) total_student
FROM Intern_Data
group by qualification
order by total_student desc;

SELECT college_name, branch
FROM Intern_Data
WHERE branch IN ('Information Technology', 'Marketing', 'Computer Science And Engineering', 'Mechanical Engineering');


select contect_no,
count(*) as duplicate_count
FROM Intern_Data
GROUP BY contect_no
HAVING COUNT(*) > 1
ORDER BY duplicate_count DESC;

SELECT
    internship_status,
    COUNT(*) AS total_status
FROM Intern_Data
WHERE internship_status IN ('Not Provided', 'Completed', 'Ongoing')
GROUP BY internship_status
ORDER BY internship_status;   -- optional, just to sort the output nicely

-- find second & third largest in college_name 
SELECT
    college_name,
    total_student
FROM (
        SELECT
            college_name,
            cnt AS total_student,
            DENSE_RANK() OVER (ORDER BY cnt DESC) AS rnk
        FROM (
                SELECT
                    college_name,
                    COUNT(*) AS cnt
                FROM Intern_Data
                GROUP BY college_name
             ) AS second_rnk
     ) AS third_rnk 
WHERE rnk IN (2,3)
ORDER BY total_student DESC;


CREATE INDEX idx_name ON Intern_Data (contect_no);
show index  from Intern_Data ;

SELECT pass_out_year, COUNT(*) AS total_passout
FROM Intern_Data 
WHERE pass_out_year BETWEEN 2024 AND 2025
GROUP BY pass_out_year;


-- in process 
SELECT  enquiry_date ,COUNT(*) AS total_enquiry_date
FROM Intern_Data 
WHERE enquiry_date BETWEEN 2024 AND 2025
GROUP BY enquiry_date;