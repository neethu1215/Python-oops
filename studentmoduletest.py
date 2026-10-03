#this python file is used to test the student module 
#this file is tesing the real life and functionality like login/registration
from modlues.student.student import studentclass


#step 1:student registration test


email = input("enter your email:")
password = input("enter your password:")

s1=studentclass()
s1.setusernameandpassword(email, password)

#step 2:student basic details test

full_name=input("enter your full name:")
dob=input("enter your date of birth:")
age=input("enter your age:")
gender=input("enter your gender:")
mobile_number=input("enter your mobile number:")
preferred_language=input("enter your preferred language:")
school_college_name=input("enter your school/college name:")
class_grade=input("enter your class/grade:")
board_curriculum=input("enter your board/curriculum:")
academic_year=input("enter your academic year:")
s1.setbasicDetails(full_name, dob, age, gender, mobile_number, preferred_language, school_college_name, class_grade, board_curriculum, academic_year)
s1.savetodb()
