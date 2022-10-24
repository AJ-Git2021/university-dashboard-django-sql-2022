import matplotlib.pyplot as plt
from uploads.models import *
question_no = f"select question_no from question natural join answer;"
tp = f"select * from answer group by qp_id;"

m1_marks = (f"select sum(answered) from answer where qp_id like '2022DBMS' group by sap;")
print (m1_marks)
m2_marks = f"select sum(answered) from answer where qp_id like '2022DBMS2' group by sap;"

avg_marks = f"select avg(answered) from answer where qp_id like '2022DBMS' ;"


print(Student.objects.all())

def m1m2():
 roll = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']
 m1 = [15, 13, 17, 9, 11, 19, 13]
 m2 = [12, 10, 18, 14, 16, 20, 7]
 line_chart1 = plt.plot(roll, m1, color='Blue')
 line_chart2 = plt.plot(roll, m2, color='Red')
 plt.xlabel('Roll No', color="black")
 plt.ylabel('Marks', color="black")
 plt.title('M1 M2 comparision graph')
 plt.legend(['M1 marks', 'M2 marks'], loc=3)
 plt.grid()
 plt.show()

def co():

 co = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']
 que= [15, 13, 17, 9, 11, 19, 13]
 line_chart1 = plt.plot(co, que, color='Blue')
#  line_chart2 = plt.plot(roll, m2, color='Red')
 plt.xlabel('CO', color="black")
 plt.ylabel('Number of Q attempted', color="black")
 plt.title('Number of Questions attempted')
#  plt.axhline(y=threshold,color='r',linestyle='-')
#  plt.legend(['M1 marks', 'M2 marks'], loc=3)
 plt.grid()
 plt.show()
 
def attempted():
 threshold=5
 rollno=1
 subject="ki"
 number_of_que = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']
 que= [15, 13, 17, 9, 11, 19, 13]
 line_chart1 = plt.plot(number_of_que, que, color='Blue')
#  line_chart2 = plt.plot(roll, m2, color='Red')
 plt.xlabel('Subjects', color="black")
 plt.ylabel('Number of Q attempted', color="black")
 plt.title(f'Number of Questions attempted by {rollno}')
 plt.axhline(y=threshold,color='r',linestyle='-')
#  plt.legend(['M1 marks', 'M2 marks'], loc=3)
 plt.grid()
 plt.show()
 
 
def marks():
 avg=5
 rollno=1
 
 subjects = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']
 marks= [15, 13, 17, 9, 11, 19, 13]
 line_chart1 = plt.plot(subjects, marks, color='Blue')
#  line_chart2 = plt.plot(roll, m2, color='Red')
 plt.xlabel('rollno', color="black")
 plt.ylabel('Number of Q attempted', color="black")
 plt.title(f'Marks Obtained')
 plt.axhline(y=avg,color='r',linestyle='-')
 plt.legend(['Marks', 'Average'],loc=0)
 plt.grid()
 plt.show()
 