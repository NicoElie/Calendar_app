"""
This part of the code is for creating all the Python classes needed for the scheduling app

"""
import pickle as pkl
import sys
import csv
from typing import List

import numpy as np
f = open('Class_Data.csv')
reader = csv.reader(f)

data = []
data_dic = {}

for row in reader:
    data.append(row)

row_number = np.shape(data)[0]
"""
Creating a dictionary containing another dictionary in the form of :
 {'Name of the Class': {'Section' : ('Time range', 'Days given')}}
 Example:
 {'ECE120' : {'AB1' : ('9:00AM - 09:50', 'MWF')}}
"""
for i in range(1, row_number):
    if data[i][0] not in data_dic:
        data_dic[data[i][0]] = {data[i][5]: (data[i][6], data[i][7])}
    else:
        data_dic[data[i][0]][data[i][5]] = (data[i][6], data[i][7])
# ---------------------------------------------------------------------------------------------------------#
"""
Class Student:
This class will store important information about students such as:
- first name
- last name
- email
- password
- Major
- University (for future updates)
we may add more methods if needed
"""


class Student:
    def __init__(self, first_name, last_name, email, password, major, semester):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.password = password
        self.major = major
        self.semester = semester
        self.student_courses = []  # store all the class taken by the students for the current semester
        self.student_activities = []  # store students activities such as jobs, extracurricular...

    def add_class(self, course_name):  # add a class to student_courses
        self.student_courses.append(course_name)

    def get_student_courses(self):  # return student_courses
        return self.student_courses

    def add_activity(self, activity_name):  # add an activity to student_activities
        self.student_activities.append(activity_name)

    def get_activity(self):  # return student_activities
        return self.student_activities

    def get_semester(self):  # return semester
        return self.semester


# -------------------------------------------------------------------------------------------------------------------#
"""
Class Course:
This class will represents the skeleton of a course structure
we will have:
- course name
- course code
- homework
- quiz
- lab
- exams
"""


class Course:
    def __init__(self, course_name, course_code, section):
        self.course_name = str(course_name)
        self.course_code = str(course_code)
        self.section = str(section)

    def get_time_and_day(self):
        dic = data_dic
        day_to_number = {'M': 0, 'T': 1, 'W': 2, 'R': 3, 'F': 4, 'Sa': 5, 'Su': 6}
        # my_info_tuple will hold the class and sections information(time and days)
        my_info_tuple = dic[self.course_code][self.section]
        time = my_info_tuple[0].split(' - ')  # Splitting the start time from the end time so we can use it
        start_time = time[0].split(':')  # Getting the start time and splitting it
        end_time = time[1].split(':')  # Getting the end time and splitting it
        # getting the start time that will be used in the calendar frame
        # and converting the time into 23:59 format
        hour_start = int(start_time[0]) if start_time[1][2:] == 'AM' else int(start_time[0]) + 12
        minute_start = int(start_time[1][0:2])
        # Calculating how long a class will take in a day per minute
        duration = 0  # It will store how long
        interval_length = 0
        if (start_time[1][2:] == 'AM' and end_time[1][2:] == 'AM' or
                start_time[1][2:] == 'PM' and end_time[1][2:] == 'PM' or
                int(end_time[0]) == 12):
            # Getting the hour interval and converting it to minutes
            duration += (int(end_time[0]) - int(start_time[0])) * 60
            # Adding the minutes
            duration += int(end_time[1][0:2]) - int(start_time[1][0:2])
        # taking the PM in consideration
        else:
            duration += ((int(end_time[0]) + 12) - int(start_time[0])) * 60
            duration += int(end_time[1][0:2]) - int(start_time[1][0:2])

        days_list = []  # This will the list of the day during which the class is given
        # Putting the days into our day list
        for char in my_info_tuple[1]:
            days_list.append(day_to_number[char])
            # return will be something like:
            # ('ECE313', [9,0,50], [0, 2, 4])
        return self.course_name, [hour_start, minute_start, duration], days_list

    @staticmethod
    def homework_deadline(is_homework, deadline):
        # if the course has homework, return the deadline day
        if is_homework:
            return deadline

    @staticmethod
    def lab_deadline(is_lab, deadline):
        # if the course has lab, return the deadline day
        if is_lab:
            return deadline

    @staticmethod
    def quiz_deadline(is_quiz, deadline):
        # if the course has quiz, return the deadline day
        if is_quiz:
            return deadline

    @staticmethod
    def exam_date(is_exam):
        # if the course has exams, return the respective deadline
        deadline: List[List[int]] = []  # list of lists [[month,day, duration]]
        if is_exam:
            number_of_exams = int(input("How many exams: "))
            i = 1
            while i <= number_of_exams:
                date = []  # [month, day, duration]
                day = int(input("what day: "))  # should be something like 23
                month = int(input("What month: "))  # month in number please
                duration = int(input("duration: "))  # duration in minute
                date.append(month)  # append to date
                date.append(day)  # append to date
                date.append(duration)
                deadline.append(date)  # append to deadline
                i += 1
        return deadline


Elie = Student("Elie", "Masanka", "masanka2@illinois.edu", "23", "Statistics", "spring")
Elie.add_class("ECE110")
course_d = Elie.get_student_courses()[0]
ECE110 = Course("ECE110", course_d, "AL1")
print(ECE110.get_time_and_day())
