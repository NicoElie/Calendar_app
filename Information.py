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
        # must come from the Course class
        # so student_courses store object
        self.student_courses = []  # store all the course taken by the students for the current semester
        # must come from the activity class
        # so student_activities store object
        self.student_activities = []  # store students activities such as jobs, extracurricular...

    def add_course(self, course_name):  # add a course to student_courses
        self.student_courses.append(course_name)

    def remove_course(self, course_name):
        self.student_courses.remove(course_name)
        return None

    def get_student_courses(self):  # return student_courses
        return self.student_courses

    def add_activity(self, activity):  # add an activity to student_activities
        self.student_activities.append(activity)

    def remove_activity(self, activity):
        self.student_activities.remove(activity)

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

    def get_course_name(self):
        return self.course_name

    def get_course_code(self):
        return self.course_code

    def get_course_section(self):
        return self.section

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
    def homework_deadline(has_homework, deadline):
        # if the course has homework, return the deadline day
        if has_homework:
            return deadline

    @staticmethod
    def lab_deadline(has_lab, deadline):
        # if the course has lab, return the deadline day
        if has_lab:
            return deadline

    @staticmethod
    def quiz_deadline(has_quiz, deadline):
        # if the course has quiz, return the deadline day
        if has_quiz:
            return deadline

    @staticmethod
    def exam_date(has_exam):
        # if the course has exams, return the respective deadline
        deadline: List[List[int]] = []  # list of lists [[month,day, duration]]
        if has_exam:
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
# -------------------------------------------------------------------------------------------------------------------#


"""
Class Activity:
This class will represents the skeleton of an activity
we will have:
- activity name
-start time
- duration
- day 
- if it is not a repetitive activity: we also need month
"""


class Activity:

    def __init__(self, activity_name, start_time, duration, day):
        self.activity_name = activity_name
        self.start_time = start_time  # start_time is a list such as [9, 0] 9 o'clock
        self.duration = duration  # duration of the activity in minute
        self.day = day  # day when the activity happen (for repetitive activity)
        self.month = None  # None is the default value

    def get_activity_name(self):
        return self.activity_name

    def get_start_time(self):
        return self.start_time

    def get_duration(self):
        return self.duration

    def get_day(self):
        return self.day

    def get_month(self):
        return self.month

    # Now for non-repetitive activity such as meeting with a friend or whatever
    # we need to set the month to have full date
    def set_activity_month(self, month):  # we already have the the day
        self.month = month
# ------------------------------------------------------------------------------------------------------------------#


"""
class Exam:
This class will represents the skeleton of an exam
we will have:
- exam name ( exam 1, exam 2,...) # I don't know if it's necessary
-start time of the exam #will be a list such like [9, 0] to say that it starts at 9 o'clock
- duration # will be given in minutes
- date of the exam # will be a list such as [month, day] # we will assume it is the same year
"""


class Exam:
    def __init__(self, name, start_time, duration, date):
        self.name = name
        self.start_time = start_time  # list such as [9, 0] 9 o'clock
        self.duration = duration  # given in minute
        self.date = date  # list such as [month, day]

    def get_exam_name(self):
        return self.name

    def get_exam_start_time(self):
        return self.start_time

    def get_exam_duration(self):
        return self.duration

    def get_exam_date(self):
        return self.date
# ------------------------------------------------------------------------------------------------------------------#


"""
class Homework
This class will represents the skeleton of a Homework
we will have:
- homework name ( homework 1, homework 2,...) # I don't know if it's necessary
- due_date will be a list like [month,day] # we will not focus on the time at which the homework is due
because we want the students to be done before that date

"""


class Homework:
    def __init__(self, name, due_date):
        self.name = name
        self.due_date = due_date  # [month, day]

    def get_homework_name(self):
        return self.name

    def get_homework_due_date(self):
        return self.due_date
# ------------------------------------------------------------------------------------------------------------------#


"""
class Quiz
This class will represents the skeleton of a Homework
we will have:
- quiz name ( homework 1, homework 2,...) # I don't know if it's necessary
- quiz_date will be a list like [month,day] 
- start_time will be a list like [9, 0] which means it starts at 9 o'clock
- quiz_type , mainly to know if it is a CBTF quiz or a in class quiz like during discussion session
- if it is a CBTF quiz, we should ask for duration
- if it is a discussion type quiz, the discussion duartion will be used instead
because we want the students to be done before that date

"""


class Quiz:
    def __init__(self, name, quiz_date, start_time, quiz_type, duration):
        self.name = name
        self.quiz_date = quiz_date  # [month, day]
        self.start_time = start_time  # [9,0] 9 o'clock
        self.quiz_type = quiz_type  # CBTF or Discussion
        self.duration = duration  # given in minutes

    def get_quiz_name(self):
        return self.name

    def get_quiz_date(self):
        return self.quiz_date

    def get_quiz_start_time(self):
        return self.start_time

    def get_quiz_type(self):
        return self.quiz_type

    def get_quiz_duration(self):
        return self.duration



Elie = Student("Elie", "Masanka", "masanka2@illinois.edu", "23", "Statistics", "spring")
Elie.add_course("ECE110")
course_d = Elie.get_student_courses()[0]
ECE110 = Course("ECE110", course_d, "AL1")
ECE110.exam_date(has_exam=False)
print(ECE110.lab_deadline(has_lab=True, deadline=6))
job = Activity("Work", [9, 0], 50, 0)
job.set_activity_month(6)
print(job.get_month())
#print(ECE110.get_time_and_day())
