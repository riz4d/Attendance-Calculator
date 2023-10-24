# Attendance Calculator

Flask app calculates your attendance percentage and provides advice on how to achieve a specific attendance percentage in a semester. It also suggests the number of lectures or days you can bunk while maintaining your current attendance.

## Introduction

Maintaining good attendance is crucial for academic success. This app helps you understand your current attendance and provides guidance on how to reach a desired attendance percentage. It also suggests the number of lectures or days you can bunk without falling below a certain percentage.

## Usage

1. Fill the required configuration variables in `config.py`:
   - `total_lectures_semester`: Total lectures in the semester.
   - `periods_per_day`: Periods per day.
     
2. Install Dependencies with pip
```
pip install -r requirements.txt
```
3. Then run the script with

```
python3 app.py
```
4. Now it's running in your localhost


## Explanation

The `attendance_calc` function performs the following steps:

1. Calculates the current attendance percentage based on the input data and rounds it to two decimal places.

2. Prints your current attendance percentage and the number of lectures or days left to reach the total lectures for the semester.

3. If the current attendance is below the minimum required percentage, it provides advice on how many lectures or days you need to attend to reach the desired percentage.

4. If your current attendance is already above the minimum required percentage, it suggests how many lectures or days you can bunk while maintaining your current attendance.

5. If you've reached the end of the semester and still haven't met the minimum attendance, it advises considering taking a leave of absence to cover condonation fees (if relevant).

Feel free to customize and adapt this script to your specific needs.

### License

This project is licensed under [MIT License](LICENSE).
