#this python file is used to test the student module 
#this file is tesing the real life and functionality like login/registration
from modlues.student.student import studentclass


#step 1:student registration test


email = input("enter your email:")
password = input("enter your password:")

s1=studentclass()
s1.setusernameandpassword(email, password)
