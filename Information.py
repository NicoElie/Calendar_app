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
        self.student_courses = []  # store all the course taken by the students for the current semester
        self.student_activities = []  # store students activities such as jobs, extracurricular...

    def add_course(self, course_name):  # add a course to student_courses
        self.student_courses.append(course_name)

    def remove_course(self, course_name):
        self.student_courses.remove(course_name)

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
        self.exams = []  # will store Exam object
        self.quiz = []  # will store Quiz object, only one because quizzes are repetitive event
        self.homework = []  # will store Homework object, only one because homework is a repetitive event

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
            # [9,0,50], [0, 2, 4])
        return [hour_start, minute_start, duration], days_list

    def add_exam(self, start_time_and_duration, date):  # add exams in order please
        self.exams.append(Exam(self.course_code, start_time_and_duration, date))  # this will create a EXam Object

    def get_exam(self, which_one):  # which_one will be like 1 for exam 1, and so forth, final will be last element
        return self.exams[which_one - 1]

    def remove_exam(self, which_one):  # which_one will be like 1 for exam 1, and so forth, final will be last element
        self.exams.pop(which_one - 1)  # remove based on index

    def get_exam_name(self, which_one):  # get the exam name
        return self.get_exam(which_one).get_exam_name()

    def get_exam_start_time_and_duration(self, which_one):  # get the exam start time and duration
        return self.get_exam(which_one).get_exam_start_time_and_duration()

    def get_exam_date(self, which_one):
        return self.get_exam(which_one).get_exam_date()

    def add_quiz(self, quiz_date, start_time_and_duration, quiz_type):
        self.quiz.append(Quiz(self.course_code, quiz_date, start_time_and_duration, quiz_type))

    def remove_quiz(self):
        self.quiz.pop(0)

    def get_quiz(self):
        return self.quiz[0]

    def get_quiz_name(self):
        return self.get_quiz().get_quiz_name()

    def get_quiz_date(self):
        return self.get_quiz().get_quiz_date()

    def get_quiz_start_time_and_duration(self):
        return self.get_quiz().get_quiz_start_time_and_duration()

    def get_quiz_type(self):
        return self.get_quiz().get_quiz_type()

    def add_homework(self, due_date):
        self.homework.append(Homework(self.course_code, due_date))

    def remove_homework(self):
        self.homework.pop(0)

    def get_homework(self):
        return self.homework[0]

    def get_homework_name(self):
        return self.get_homework().get_homework_name()

    def get_homework_due_date(self):
        return self.get_homework().get_homework_due_date()


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

    def __init__(self, activity_name, start_time_and_duration, day):
        self.activity_name = activity_name
        self.start_time_and_duration = start_time_and_duration  # start_time is a list such as [9, 0, 50] 9 o'clock
        self.day = day  # day when the activity happen (for repetitive activity)
        self.month = None  # None is the default value

    def get_activity_name(self):
        return self.activity_name

    def get_start_time_and_duration(self):
        return self.get_start_time_and_duration()

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
- exam name ( exam for ECE110,...)
-start time_and_duration of the exam will be a list such like [9, 0, 50] to say that it starts at 9 o'clock with
duration 50 min
- date of the exam # will be a list such as [month, day] # we will assume it is the same year
"""


class Exam:
    def __init__(self, course_code, start_time_and_duration, date):
        self.name = f"Exam for {course_code}"
        self.start_time_and_duration = start_time_and_duration  # list such as [9, 0, 50] 9 o'clock 50 min for duration
        self.date = date  # list such as [month, day]

    def get_exam_name(self):
        return self.name

    def get_exam_start_time_and_duration(self):
        return self.start_time_and_duration

    def get_exam_date(self):
        return self.date
# ------------------------------------------------------------------------------------------------------------------#


"""
class Homework
This class will represents the skeleton of a Homework
we will have:
- homework name ( homework for ECE110,...)
- due_date will be a list of week day like monday etc . we will not focus on the time at which the homework is due
because we want the students to be done before that date

"""


class Homework:
    def __init__(self, course_code, due_date):
        self.name = f"Homework for {course_code}"
        self.due_date = due_date  # a list containing the week day when HW is due like [0,4] for Monday and Friday

    def get_homework_name(self):
        return self.name

    def get_homework_due_date(self):
        return self.due_date
# ------------------------------------------------------------------------------------------------------------------#


"""
class Quiz
This class will represents the skeleton of a Homework
we will have:
- quiz name ( homework for ECE110,...)
- quiz_date will be a list like [week day]  a list of week day 0 for monday and so forth
- start_time_and_duration will be a list like [9, 0, 50] which means it starts at 9 o'clock, duration 50 min
- quiz_type , mainly to know if it is a CBTF quiz or a in class quiz like during discussion session
"""


class Quiz:
    def __init__(self, course_code, quiz_date, start_time_and_duration, quiz_type):
        self.name = f"Quiz for {course_code}"
        self.quiz_date = quiz_date  # [week day] [0] means monday
        self.start_time_and_duration = start_time_and_duration  # [9,0, 50] 9 o'clock and 50 min for duration
        self.quiz_type = quiz_type  # CBTF or Discussion

    def get_quiz_name(self):
        return self.name

    def get_quiz_date(self):
        return self.quiz_date

    def get_quiz_start_time_and_duration(self):
        return self.start_time_and_duration

    def get_quiz_type(self):
        return self.quiz_type
# --------------------------------------------------------------------------------------------------------------------#