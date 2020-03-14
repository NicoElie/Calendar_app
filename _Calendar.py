"""
This part of the code is to create the calendar that will store all events
"""
import sys

import numpy as np
import calendar
import datetime
import holidays

import Information

"""
class Calendar:
- based on year 
- is an array containing array
"""

##hdh
class Calendar:
    def __init__(self, year):
        """
        Constructor of Calendar
        :param year: an integer for the year
        """
        self.january = []
        self.february = []
        self.march = []
        self.april = []
        self.may = []
        self.june = []
        self.july = []
        self.august = []
        self.september = []
        self.october = []
        self.november = []
        self.december = []
        self.year = year
        self.year_calendar = [self.january, self.february, self.march, self.april, self.may, self.june, self.july,
                              self.august, self.september, self.october, self.november, self.december]
        self.len_year_calendar = len(self.year_calendar)

        for month in range(self.len_year_calendar):
            _, num = calendar.monthrange(self.year, month + 1)
            i = num
            while i > 0:
                """
                The while loop is initializing every day of each month as an array with 145 by 1 np array. 
                Each 10 minute in a day is represented by a row. We have 145 row, so about 1450 minutes in 1 day;
                Which is about 24 hours
                """
                self.year_calendar[month].append(np.empty((145, 1), dtype=object))
                i -= 1
        """
        Let's fill holidays in the calendar
        Actually every day is represented by a (145, 1) numpy array with each element set to None.
        This function will set every holiday day array to "H"
        """
        ## getting all the holidays during the year, and storing it into a list
        ## The holiday will be of the form ['year', 'month', 'day']
        holiday_list = [str(date[0]).split('-') for date in holidays.UnitedStates(years=self.year).items()]

        ## Modifying the calendar day to account for holidays
        for date in holiday_list:
            for time_slot in range(len(self.year_calendar[int(date[1]) - 1][int(date[2]) - 1])):
                self.year_calendar[int(date[1]) - 1][int(date[2]) - 1][time_slot] = "H"

    def view_month(self, month):
        """
        This function is to get the calendar of the month requested by user
        for the monthly view of the calendar
        :param month: the month to view
        :return: the calendar of the month we are interested in
        """
        if month == 'january':
            return self.january
        elif month == 'february':
            return self.february
        elif month == 'march':
            return self.march
        elif month == 'april':
            return self.april
        elif month == 'may':
            return self.may
        elif month == 'june':
            return self.june
        elif month == 'july':
            return self.july
        elif month == 'august':
            return self.august
        elif month == 'september':
            return self.september
        elif month == 'october':
            return self.october
        elif month == 'december':
            return self.december


    def fill_calendar_classes(self, semester, semester_start, semester_end, courses_list = []):
        """
        This function is to fill the calendar with default activities for user such as the lectures
        The input for this function is the output of get_time_and_day from Information.py
        @:param semester will be used to determine the month we need to consider

        @:param semester_start is the day the semester start

        @:param semester_end is the day regular class ends (not the last day of final!)

        @:param courses_list is a list of all the courses taken by a students during the semester.
        It is a list of 3 elements tuples of the form ('course_name', [start_hour, start_min, the duration of the class in minutes], a list of all the day during which the course is given)
        Example. If ECE 313 was given every monday, wednesday and friday from 1:10 pm to 1:50 pm --> ('ECE313', [13, 10, 40], [0, 2, 4])
        """
        ## First we get the list of all the classes that the student is taking


        # course_detail = ['ECE110', [11, 0, 50], [0, 2]]
        # start = (course_detail[1][0] * 60 + course_detail[1][1]) / 10
        # end = (course_detail[1][0] * 60 + course_detail[1][1] + course_detail[1][2]) / 10

        # if we are in the fall semester
        # so we have august, september, october, november, december
        if semester == "fall":
            # fill august
            for day in range(semester_start - 1, len(self.august)):
                i = int(start - 1)
                while i < int(end):
                    if (self.august[day][i] == None):
                        self.august[day][i] = f"Lecture for {course_detail[0]}"
                    i += 1
            # fill september
            for day in range(0, len(self.september)):
                i = int(start - 1)
                while i < int(end):
                    if (self.september[day][i] == None):
                        self.september[day][i] = f"Lecture for {course_detail[0]}"
                    i += 1
            # fill october
            for day in range(0, len(self.october)):
                i = int(start - 1)
                while i < int(end):
                    if (self.october[day][i] == None):
                        self.october[day][i] = f"Lecture for {course_detail[0]}"
                    i += 1
            # fill november
            for day in range(0, len(self.november)):
                i = int(start - 1)
                while i < int(end):
                    if (self.november[day][i] == None):
                        self.november[day][i] = f"Lecture for {course_detail[0]}"
                    i += 1
            # fill december
            for day in range(0, semester_end):
                i = int(start - 1)
                while i < int(end):
                    if (self.december[day][i] == None):
                        self.december[day][i] = f"Lecture for {course_detail[0]}"
                    i += 1
        elif semester == 'spring':
            # fill january
            for day in range(semester_start - 1, len(self.january)):
                i = int(start - 1)
                while i < int(end):
                    if (self.january[day][i] == None):
                        self.january[day][i] = f"Lecture for {course_detail[0]}"
                    i += 1
            # fill february
            for day in range(0, len(self.february)):
                i = int(start - 1)
                while i < int(end):
                    if (self.february[day][i] == None):
                        self.february[day][i] = f"Lecture for {course_detail[0]}"
                    i += 1
            # fill march
            for day in range(0, len(self.march)):
                i = int(start - 1)
                while i < int(end):
                    if (self.march[day][i] == None):
                        self.march[day][i] = f"Lecture for {course_detail[0]}"
                    i += 1
            # fill april
            for day in range(0, len(self.april)):
                i = int(start - 1)
                while i < int(end):
                    if (self.april[day][i] == None):
                        self.april[day][i] = f"Lecture for {course_detail[0]}"
                    i += 1
            # fill may
            for day in range(0, semester_end):
                i = int(start - 1)
                while i < int(end):
                    if (self.may[day][i] == None):
                        self.may[day][i] = f"Lecture for {course_detail[0]}"
                    i += 1


# Elie = Information.Student("Elie", "Masanka", "masanka2@illinois.edu", "23", "Statistics", "fall")
# # test = Calendar(2020)
# # test.fill_calendar(Elie.get_semester(), 1, 13)
# # print(test.monthly_view('december')[13])  # this check for the 14 not the 13
# # #print(test.monthly_view('september')[0])
# # print(calendar.monthrange(2020, 3))

my_cal = Calendar(2019)
print(my_cal.view_month('january'))

num = [1, 2,3]
print(num)
print(num)

