import math
import statistics
import csv
print("Welcome to the student grading system ")
print('Get the grade and total marks of the student of their 5 subjects ')
print('')
name = input('NAME OF THE STUDENT:')
roll_no= input('ROLL NO.:')
print('')
print('Enter the marks of the student')
# Taking input from the user of the marks of all the subjects
a=int(input("social science="))
b=int(input("computer= "))
c=int(input("Physics= "))
d=int(input("Maths= "))
e=int(input("Chemistry= "))
x=[a,b,c,d,e]
total=a+b+c+d+e
print(' ')
print('TOTAL MARKS =',total,'/500')
percentage=(total/500)*100
percentage = math.floor(percentage *100)/100
average = statistics.mean(x)
print('PERCENTAGE=',percentage,'%')
print('Average=',average)
if percentage>100:
    print('Wrongs marks entered')
elif percentage>=95:
    grade = 'A+'
elif percentage>=85:
    grade ='A'
elif percentage>=75:
    grade ='B'
elif percentage>=65:
    grade ='C'
elif percentage>=55:
    grade ='D'
elif percentage>=45:
    grade ='E'
else:
    grade ='F'
print('  ')
if percentage>=45:
    result='PASS'
else:
    result='FAIL'
print('GRADE:',grade)
print('RESULT:',result)

#Save result in csv slides
with open ('students_results.csv', 'w', newline= "") as file:
    writer = csv.writer(file)
    writer.writerow([name,roll_no,total,percentage,average,grade,result])
print('')
import os
print('CSV location:',os.path.abspath('students_results.csv'))
print('RESULT SAVED SUCCESSFULLY')



