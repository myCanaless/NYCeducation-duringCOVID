# NYC Students during COVID
Every year, OpenNYC and related NYC-based organizations release reports on education outcomes for students in the NYC public school system. These rich datasets usually include various demographic data, as well as geographic location which can then be subsequently used to determine socio-economic status.

Oftentimes it is hard to pinpoint one singular key-event which has had an impact on student performance. In fact, when it comes to evaluating the pedagogical-practices of teachers and the structure of the classroom, we note that not much changes on a year-by-year basis. 

However the pandemic and subsequent closure of schools is one of those rare ‘once-in-a-lifetime’ moments that truly divided student performance. In fact, this drop in academic performance has been reported as being the “single largest drop in math in 50 years” (Washington Post, 2023). 

As such, the availability of these rich data sets represents a valuable data-monitoring opportunity in order to assess if we are “back on track”, or continuing the plunge in the NYC public school system. 

# Datasets
Datasets were provided by
[NYC OpenData](https://opendata.cityofnewyork.us/data/)

 - 2017 - 2022 Demographic Snapshot 
 - 2018 - 2021 Daily Attendance by School
 - 2021 Students In Temporary Housing
 - Math and English Language Arts Test Results 2013-2023 **

** Important notes from dataset 

 "Due to COVID-19 pandemic, the exams were not administered in 2020" and were optional for students to take in 2021. In 2018, NYSED rescaled the Math and ELA exams to account for a change in test administration from 3 days to 2 days. Results from 2018 - 2022 can be compared to each other but cannot be compared to prior years (or to 2023). Exams were cancelled in 2020 and voluntary in 2021. 21% of eligible students took the exam in 2021, no data for those years is included. 

# What to know
What is a DBN (District Borough Number)?

The DBN or District Borough Number is the combination of the District Number, the letter code for the borough, and the number of the school. Every school in NYC Public Schools (NYCPS) has a District Borough Number.

![DBN](docs/NYC_DBN.jpg)

What is Economic Need Index?

The Economic Need Index (ENI) estimates the percentage of students facing economic hardship.
The student Economic Need Index (ENI) is a metric calculated used by the Department of Education to investigate and incorporate economic diversity in NYC's schools.

### Learning Standards 

- Level 1  = Not Meeting Learning Standards
- 'Pct Level 1' - Percentage of students who scored in Level 1 range  
- Level 2 = Partially Meeting Learning Standards
- 'Pct Level 2' - Percentage of students who scored in Level 2 range
- Level 3 = Meeting Learning Standards
- 'Pct Level 3' - Percentage of students who scored in Level 3 range 
- Level 4 = Meeting Learning Standards with Distinction  
- 'Pct Level 4' - Percentage of students who scored in Level 4 range

# Issues / Notes
Results from 2018 to 2022 can be compared to each other but cannot be compared to prior years  (or to 2023) due to a change in test administration. 

# Tableau Dashboard 

Attendance Rate 

https://github.com/user-attachments/assets/c5756811-0d03-4643-96c9-fbf7c4af905f

Poverty Rate 

https://github.com/user-attachments/assets/7bf889e2-8e40-4f16-8042-59740df6dc23

Test Results 

https://github.com/user-attachments/assets/845e75b6-3145-4d52-992a-437d7efeec23

# Analysis

English Language Arts Achievement Levels (Citywide)

![ELA Citywide](<docs/Percentage of Students by Achievement Levels Over Years (Citywide).png>)

Math Achievement Levels (Citywide)

![Math Citywide](<docs/CityWide Math Levels.png>)

Citywide Attendance Rate:

![Citywide Attendance Rate](<docs/Heatmap of Attendance Rate by District and Month (2018 - 2021).png>) 

Monthly Attendance Rate by Borough:

![Monthly Attendance Rate by Borough](<docs/Monthly Attendance Rate by Borough (2018 - 2021).png>)

## Geographic Subdivision Analysis

ELA Performance Levels Across Borough:

![ELA Performance Levels Across Borough](<docs/ELA Performance Levels Across Boroughs.png>)

Math Performance Levels Across Borough:

![Math Performance Levels Across Borough](<docs/Math Performance Levels Across Boroughs.png>)

## Demographics Analysis

ELA Performance Levels:

![ELA Performance Levels](<docs/ELA Performance Levels.png>)

Math Performance Levels:

![Math Performance Levels](<docs/Math Performance Levels.png>)

Economic Need Index of Students with Performance Levels 1 and 4: 

![Economic Need Index](<docs/From Tableau/Economic Need Index.jpg>)




# Goal
Analyze an NYC dataset of student data to analyze student performance. Some analytical questions/goals you may want to consider include:
- How has test performance changed after Covid? Does this vary across demographics?
- How has student attendance changed after Covid?
- How can we design a comprehensive data dashboard which provides up-to-date information on NYC student performance. 
