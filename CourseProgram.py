'''
You have been given partial code. The objective is to reproduce the output as shown in the file - Output.png
1) Create an instance of the Course object
2) Create an instance of the Register object for EACH student in the students list using a For loop.
3) Print out the student name, course name, CRN and number of seats left for each iteration using
   ONLY get methods.
4) Take note that student 'Joanne' cannot register since there are only 4 seats in the course and
   and the output should reflect that as shown in the picture.
'''

from atexit import register
import CourseClass as cc

def main():

    name = 'MIS 4322 - Advanced Python'
    crn = '250309'
    seats = 4
    status = 'open'
    students = ['John','James','Jill','Jack','Joanne']
    

    mis4322 = cc.Course('MIS 4322 - Advanced Python','250309',4,'open')

    student1 = cc.Register('John', 250309)
    student2 = cc.Register('James', 250309)
    student3 = cc.Register('Jill', 250309)
    student4 = cc.Register('Jack', 250309)
    student5 = cc.Register('Joane', 250309)
    student_list = [student1,student2,student3,student4,student4,student5]
    seats_aval = 4
    n = 0
   
    for n in student_list:
       if seats_aval == 0:
          seats_aval -= 1
          print('Student Name: ', student_list[n].get_name())
          print('Course Name: ', cc.Course.get_name())
          print('CRN: ', cc.Course.get_name())
          print('Seats Available: ', cc.Course.get_seats)
       else:
          print('Sorry ' + cc.Register.get_name(n) + ','+ ' registration is closed for MIS 4322.')



    
main()



        
    
    
