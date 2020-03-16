"""
This part of the code is to create the calendar that will store all events
"""
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
            _, num = calendar.monthrange(self.year, month + 1)  # we ignore the first element in the tuple with _,
            i = num
            while i > 0:
                """
                The while loop is initializing every day of each month as an array with 144 by 1 np array. 
                each row is 10 min so 50 min will take 5 rows
                Each 10 minute in a day is represented by a row. We have 145 row, so about 1440 minutes in 1 day;
                Which is 24 hours
                """
                self.year_calendar[month].append(np.empty((144, 1), dtype=object))
                i -= 1
        """
        Let's fill holidays in the calendar
        Actually every day is represented by a (145, 1) numpy array with each element set to None.
        This function will set every holiday day array to "Holiday"
        """
        # getting all the holidays during the year, and storing it into a list
        # The holiday will be of the form ['year', 'month', 'day']
        holiday_list = [str(date[0]).split('-') for date in holidays.UnitedStates(years=self.year).items()]

        # Modifying the calendar day to account for holidays
        for date in holiday_list:
            for time_slot in range(len(self.year_calendar[int(date[1]) - 1][int(date[2]) - 1])):
                self.year_calendar[int(date[1]) - 1][int(date[2]) - 1][time_slot] = "Holiday"
        ##### If Fall semester, account for Fall break
        fall_break = (23, 1)
        for day in range(22, len(self.november), 1):
            for time_slot in range(len(self.november[day])):
                self.november[day][time_slot] = "FallBreak"

        for time_slot in range(len(self.december[0])):
            self.december[0][time_slot] = "FallBreak"

        ### If Spring, account for SpringBreak
        spring_break = (16, 25)
        for day in range(15, 26, 1):
            for time_slot in range(len(self.march[day])):
                self.march[day][time_slot] = "SpringBreak"

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

    def fill_calendar_classes(self, semester, semester_start, semester_end, class_code, date_and_time):
        """
        This function is to fill the calendar with default activities for user such as the lectures
        The input for this function is the output of get_time_and_day from Information.py
        @:param semester will be used to determine the month we need to consider

        @:param semester_start is the day the semester start

        @:param semester_end is the day regular class ends (not the last day of final!)

        @:param class_code the name code of the class like "ECE313" for example

        @:param date_and_time will be an array like [[13, 10, 40], [0, 2, 4]]
        first element in the array is the starting time and duration in this case, 13h10 and 40 min duration
        the second element in the array is the week day at which the course happen
        0 means monday and so forth
        """
        # First we get the list of all the classes that the student is taking
        week_day = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
        course_detail = date_and_time   # come from get_time_and day function in Information.Course
        print(course_detail)
        start = (course_detail[0][0] * 60 + course_detail[0][1]) / 10
        end = (course_detail[0][0] * 60 + course_detail[0][1] + course_detail[0][2]) / 10

        # if we are in the fall semester
        # so we have august, september, october, november, december
        if semester == "fall":
            # fill august
            for day in range(semester_start - 1, len(self.august)):
                # we need to check for week days, for example a course can only happen on Tuesday and Thursday
                # we check for that in the following code
                set_day = datetime.datetime.strptime(f"{day + 1} 08 {self.year}", '%d %m %Y').weekday()
                day_check = (calendar.day_name[set_day])
                for j in course_detail[1]:  # course_detail[1] store the week days as number, ex: 0 means monday
                    # we check if the actual date is the week day we need for that course
                    if day_check == week_day[j]:  # if true, then we add class at that time
                        i = int(start)
                        while i < int(end):
                            if (self.august[day][i] == None):
                                self.august[day][i] = f"{class_code}"  # come from get_course_code
                            i += 1
            # fill september
            for day in range(0, len(self.september)):
                # we need to check for week days, for example a course can only happen on Tuesday and Thursday
                # we check for that in the following code
                set_day = datetime.datetime.strptime(f"{day + 1} 09 {self.year}", '%d %m %Y').weekday()
                day_check = (calendar.day_name[set_day])
                for j in course_detail[1]:  # course_detail[1] store the week days as number, ex: 0 means monday
                    # we check if the actual date is the week day we need for that course
                    if day_check == week_day[j]:  # if true, then we add class at that time
                        i = int(start)
                        while i < int(end):
                            if (self.september[day][i] == None):
                                self.september[day][i] = f"{class_code}"  # come from get_course_code
                            i += 1
            # fill october
            for day in range(0, len(self.october)):
                # we need to check for week days, for example a course can only happen on Tuesday and Thursday
                # we check for that in the following code
                set_day = datetime.datetime.strptime(f"{day + 1} 10 {self.year}", '%d %m %Y').weekday()
                day_check = (calendar.day_name[set_day])
                for j in course_detail[1]:  # course_detail[1] store the week days as number, ex: 0 means monday
                    # we check if the actual date is the week day we need for that course
                    if day_check == week_day[j]:  # if true, then we add class at that time
                        i = int(start)
                        while i < int(end):
                            if (self.october[day][i] == None):
                                self.october[day][i] = f"{class_code}"  # come from get_course_code
                            i += 1
            # fill november
            for day in range(0, len(self.november)):
                # we need to check for week days, for example a course can only happen on Tuesday and Thursday
                # we check for that in the following code
                set_day = datetime.datetime.strptime(f"{day + 1} 11 {self.year}", '%d %m %Y').weekday()
                day_check = (calendar.day_name[set_day])
                for j in course_detail[1]:  # course_detail[1] store the week days as number, ex: 0 means monday
                    # we check if the actual date is the week day we need for that course
                    if day_check == week_day[j]:  # if true, then we add class at that time
                        i = int(start)
                        while i < int(end):
                            if (self.november[day][i] == None):
                                self.november[day][i] = f"{class_code}"  # come from get_course_code
                            i += 1
            # fill december
            for day in range(0, semester_end):
                # we need to check for week days, for example a course can only happen on Tuesday and Thursday
                # we check for that in the following code
                set_day = datetime.datetime.strptime(f"{day + 1} 12 {self.year}", '%d %m %Y').weekday()
                day_check = (calendar.day_name[set_day])
                for j in course_detail[1]:  # course_detail[1] store the week days as number, ex: 0 means monday
                    # we check if the actual date is the week day we need for that course
                    if day_check == week_day[j]:  # if true, then we add class at that time
                        i = int(start)
                        while i < int(end):
                            if (self.december[day][i] == None):
                                self.december[day][i] = f"{class_code}"  # come from get_course_code
                            i += 1
        elif semester == 'spring':
            # fill january
            for day in range(semester_start - 1, len(self.january)):
                # we need to check for week days, for example a course can only happen on Tuesday and Thursday
                # we check for that in the following code
                set_day = datetime.datetime.strptime(f"{day + 1} 01 {self.year}", '%d %m %Y').weekday()
                day_check = (calendar.day_name[set_day])
                for j in course_detail[1]:  # course_detail[1] store the week days as number, ex: 0 means monday
                    # we check if the actual date is the week day we need for that course
                    if day_check == week_day[j]:  # if true, then we add class at that time
                        i = int(start)
                        while i < int(end):
                            if (self.january[day][i] == None):
                                self.january[day][i] = f"{class_code}"  # come from get_course_code
                            i += 1
            # fill february
            for day in range(0, len(self.february)):
                # we need to check for week days, for example a course can only happen on Tuesday and Thursday
                # we check for that in the following code
                set_day = datetime.datetime.strptime(f"{day + 1} 02 {self.year}", '%d %m %Y').weekday()
                day_check = (calendar.day_name[set_day])
                for j in course_detail[1]:  # course_detail[1] store the week days as number, ex: 0 means monday
                    # we check if the actual date is the week day we need for that course
                    if day_check == week_day[j]:  # if true, then we add class at that time
                        i = int(start)
                        while i < int(end):
                            if (self.february[day][i] == None):
                                self.february[day][i] = f"{class_code}"  # come from get_course_code
                            i += 1
            # fill march
            for day in range(0, len(self.march)):
                # we need to check for week days, for example a course can only happen on Tuesday and Thursday
                # we check for that in the following code
                set_day = datetime.datetime.strptime(f"{day + 1} 03 {self.year}", '%d %m %Y').weekday()
                day_check = (calendar.day_name[set_day])
                for j in course_detail[1]:  # course_detail[1] store the week days as number, ex: 0 means monday
                    # we check if the actual date is the week day we need for that course
                    if day_check == week_day[j]:  # if true, then we add class at that time
                        i = int(start)
                        while i < int(end):
                            if (self.march[day][i] == None):
                                self.march[day][i] = f"{class_code}"  # come from get_course_code
                            i += 1
            # fill april
            for day in range(0, len(self.april)):
                # we need to check for week days, for example a course can only happen on Tuesday and Thursday
                # we check for that in the following code
                set_day = datetime.datetime.strptime(f"{day + 1} 04 {self.year}", '%d %m %Y').weekday()
                day_check = (calendar.day_name[set_day])
                for j in course_detail[1]:  # course_detail[1] store the week days as number, ex: 0 means monday
                    # we check if the actual date is the week day we need for that course
                    if day_check == week_day[j]:  # if true, then we add class at that time
                        i = int(start)
                        while i < int(end):
                            if (self.april[day][i] == None):
                                self.april[day][i] = f"{class_code}"  # come from get_course_code
                            i += 1
            # fill may
            for day in range(0, semester_end):
                # we need to check for week days, for example a course can only happen on Tuesday and Thursday
                # we check for that in the following code
                set_day = datetime.datetime.strptime(f"{day + 1} 05 {self.year}", '%d %m %Y').weekday()
                day_check = (calendar.day_name[set_day])
                for j in course_detail[1]:  # course_detail[1] store the week days as number, ex: 0 means monday
                    # we check if the actual date is the week day we need for that course
                    if day_check == week_day[j]:  # if true, then we add class at that time
                        i = int(start)
                        while i < int(end):
                            if (self.may[day][i] == None):
                                self.may[day][i] = f"{class_code}"  # come from get_course_code
                            i += 1

    def add_event_to_calendar(self, event_name, event_date, event_start_time, event_duration):
        """
        This function will be used to add different events in the calendar
        event can be quiz, homework, job or anything
        :param event_name: the name of the event # could be quiz or exam whatever
        :param event_date: [month, day] like [3,14] march the 14th
        :param event_start_time: [9,0] 9 o'clock
        :param event_duration: given in minutes
        :return: None, it just update the calendar
        """
        month = event_date[0]
        day = event_date[1]
        start = (event_start_time[0] * 60 + event_start_time[1]) / 10
        end = (event_start_time[0] * 60 + event_start_time[1] + event_duration) / 10

        """
            we will look at the position where we start, which is represented by start
            if 144 - start > duration/10 then we will go with the remaining to the next day
            available = 144 - start
            so we will add event in the day until we are left with remaining
            then we will use that for the next day starting at midnight
        """
        available = 144 - int(start)  # available number of row that we could not fill
        d = event_duration / 10  # duration in terms of row ; 10 min is 1 row
        # check if we can add all event in the same day
        if available >= d:  # if true, we can fill the all event in the day
            i = int(start)
            while i < int(end):
                if self.year_calendar[month - 1][day - 1][i] == None:
                    self.year_calendar[month - 1][day - 1][i] = event_name
                i += 1
        elif available < d:
            remaining = int((start + d) - 144)  # the remaining row to use for the next day
            row_to_use = 144 - start  # number of row that we can use for the current day

            # add the event for the actual day
            i = int(start)
            while i < int(start + row_to_use):
                if self.year_calendar[month - 1][day - 1][i] == None:
                    self.year_calendar[month - 1][day - 1][i] = event_name
                i += 1

            # add the event in the next day with the remaining number of row
            j = 0  # we start at midnight
            while j < int(remaining):
                # check if it is the last day of the month
                if (day - 1) == len(self.year_calendar[month - 1]) - 1:  # if true,move to the next month and first day
                    if self.year_calendar[month][0][j] == None:
                        self.year_calendar[month][0][j] = event_name
                else:  # stay in the same month but move to the next day
                    if self.year_calendar[month - 1][day][j] == None:
                        self.year_calendar[month - 1][day][j] = event_name
                j += 1


# Elie = Information.Student("Elie", "Masanka", "masanka2@illinois.edu", "23", "Statistics", "fall")
test = Calendar(2020)
course1 = Information.Course("Intro to Elec", "ECE110", "AL1")
course = course1.get_time_and_day()
code = course1.get_course_code()
test.fill_calendar_classes("fall", 12, 13, code, course)
print(test.view_month('august')[11])  # this check for the 12
print("-----------------------------------------------------------")
print(test.view_month('september')[10])  # check for 11
print('---------------------------------------------------------')
print(test.view_month('december')[6])  # check for 7

#print(calendar.monthrange(2020, 3))

#my_cal = Calendar(2019)
#my_cal.add_event_to_calendar("quiz for 313", [1, 31], [0, 0], 40)
#print(my_cal.view_month('january')[30])  # january 31
#print('------------------------------------------')
#print(my_cal.view_month('february')[0])  # february first


