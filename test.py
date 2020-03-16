import Information
import _Calendar

# Create a student
Elie = Information.Student("Elie", "Masanka", "masanka2@illinois.edu", "23", "Statistics", "spring")
# create course
MATH347 = Information.Course("Fundamental of Mathematics", "MATH347", "B1")
MATH415 = Information.Course("Applied Linear Algebra", "MATH415", "AL3")
MATH415_d = Information.Course("Applied Linear Algebra", "MATH415", "AD4")
ECE313 = Information.Course("Probability with Engineering Application", "ECE313", "D")
CS125 = Information.Course("Intro to Computer Science", "CS125", "AL2")
CS125_l = Information.Course("Intro to Computer Science", "CS125", "AYJ")
FR156 = Information.Course("Exploring Paris", "FR156", "D")
# add those course into the student list
Elie.add_course(MATH347.get_course_code())
Elie.add_course(MATH415.get_course_code())
Elie.add_course(MATH415_d.get_course_code())
Elie.add_course(ECE313.get_course_code())
Elie.add_course(CS125.get_course_code())
Elie.add_course(CS125_l.get_course_code())
Elie.add_course(FR156.get_course_code())
# add event like homework, exams for each course
MATH347.add_homework([4])
ECE313.add_homework([4])
CS125.add_homework([0, 1, 2, 3, 4])
CS125.add_quiz([2], [15, 0, 50], "CBTF")
ECE313.add_quiz([0], [17, 0, 50], "CBTF")
# let's add that to the calendar
Elie_Calendar = _Calendar.Calendar(2020, 'spring', 21, 13)
Elie_Calendar.fill_calendar_classes(MATH347.get_course_code(), MATH347.get_time_and_day())
Elie_Calendar.fill_calendar_classes(MATH415.get_course_code(), MATH415.get_time_and_day())
Elie_Calendar.fill_calendar_classes(MATH415_d.get_course_code(), MATH415_d.get_time_and_day())
Elie_Calendar.fill_calendar_classes(ECE313.get_course_code(), ECE313.get_time_and_day())
Elie_Calendar.fill_calendar_classes(CS125.get_course_code(), CS125.get_time_and_day())
Elie_Calendar.fill_calendar_classes(CS125_l.get_course_code(), CS125_l.get_time_and_day())
Elie_Calendar.fill_calendar_quiz(CS125.get_quiz_name(), CS125.get_quiz_date(), CS125.get_quiz_start_time_and_duration())
print("#----------------------------calendar start---------------------------------------------------#")

print(Elie_Calendar.view_month('february')[11])
print(Elie.get_student_courses())
print(Elie.get_semester())
print(CS125.get_quiz_start_time_and_duration())

