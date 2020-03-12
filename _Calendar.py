"""
This part of the code is to create the calendar that will store all events
"""
import sys

import numpy as np
import calendar
import datetime

import Information

"""
class Calendar:
- based on year 
- is an array containing array
"""


class Calendar:
    def __init__(self, year):
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

    def set_month_calendar(self):
        """
        This function has for purpose to create the data structure for the calendar
        each month has multiple array that represents that represents the day
        for example, january will have 31 arrays; one for each day
        the structure for the day calendar is a numpy array of 1 columns and 145 rows

        :return: yearly calendar
        """
        for month in range(len(self.year_calendar)):
            num = calendar.monthrange(self.year, month + 1)[1]
            i = num
            while i > 0:
                self.year_calendar[month].append(np.empty((145, 1), dtype=object))
                i -= 1
        return len(self.year_calendar[1])

    def monthly_view(self, month):
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

    def fill_calendar(self):
        """
        This function is to fill the calendar with default activities for user such as the lectures
        The input for this function is the output of get_time_and_day from Utilities_information.py
        """
        course_detail = Information.Course.get_time_and_day()  # ('ECE110', [11, 0, 50], [0, 2])
        start = (course_detail[1][0] * 60 + course_detail[1][1]) / 10
        end = (course_detail[1][0] * 60 + course_detail[1][1] + course_detail[1][2]) / 10

        # let's assume that we are in the fall semester
        # so we have august, september, october, november, december

        # fill august
        for day in range(len(self.august)):
            i = int(start - 1)
            while i < int(end):
                for j in course_detail[2]:
                    if self.august[day][j] == None:
                        student_calendar[i][j] = class_detail[0]
                i += 1

test = Calendar(2020)
test.set_month_calendar()
np.set_printoptions(threshold=sys.maxsize)
print(len(test.monthly_view('february')))
