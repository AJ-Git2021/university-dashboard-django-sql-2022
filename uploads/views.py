from multiprocessing import context
from django.shortcuts import render
from .models import *
# Create your views here.


def home(request):
        data = Student.objects.all()
        context = {"data":data} 
        return render(request, 'uploads/base.html', context)

def questionAnswerView(request):
        Qformat = Question.objects.all()
        Ques = QuestionPaper.objects.all()
        studentAnswer = Answer.objects.all()
        context = {"quesp":Ques,"quesform":Qformat,"quesans":studentAnswer}
        return render(request, 'uploads/quesans.html', context)





# matplot lib and functions here
from pylab import *
import PIL, PIL.Image
import io
import urllib, base64
import matplotlib.pyplot as plt

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
 buf = io.BytesIO()
 plt.savefig(buf,format='png')
 buf.seek(0)
 string = base64.b64encode(buf.read())
 uri = urllib.parse.quote(string)
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
 

# def analysis():
#  avg=5
#  rollno=1
 
#  subjects = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']
#  marks= [15, 13, 17, 9, 11, 19, 13]
#  line_chart1 = plt.plot(subjects, marks, color='Blue')
# #  line_chart2 = plt.plot(roll, m2, color='Red')
#  plt.xlabel('rollno', color="black")
#  plt.ylabel('Number of Q attempted', color="black")
#  plt.title(f'Marks Obtained')
#  plt.axhline(y=avg,color='r',linestyle='-')
#  plt.legend(['Marks', 'Average'],loc=0)
#  plt.grid()
#  plt.show()

def analysis(request):
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
        buf = io.BytesIO()
        plt.savefig(buf,format='png')
        buf.seek(0)
        string = base64.b64encode(buf.read())
        uri = urllib.parse.quote(string)
        plt.show()
        return render(request,'uploads/analysis.html',{"data":uri})


        
