
"""Python-assessment1-TrivikramanS-LVADSUSR_192.ipynb"""

#1.
l=int(input("Enter the Length of the property"))
b=int(input("Enter the Breadth of the property"))
area=l*b
print(f"Area of the property is {area}")
if(area <1000):
  print("Based on the area the property is categorized as small")
if(area>1000 and area <2000):
  print("Based on the area the property is categorized as medium")
if (area >2000):
  print("Based on the area the property is categorized as large")

#2.
weight=float(input("Enter your weight in Kg"))
height=float(input("Enter your height in meter"))
BMI=weight/(height)**2
print(f"BMI is {BMI}")
print("You will be connected with assistant for further support")

#3.
class Student:
    def __init__(self, name, grades):
        self.name = name
        self.grades = grades

    def add_grade(self, grade):
        self.grades.append(grade)

    def retrieve_grades(self):
        return self.grades

    def update_name(self, new_name):
        self.name = new_name

students = []

while True:
    print("1. Add student")
    print("2. Retrieve student grades")
    print("3. Update student name")
    print("4. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        name = input("Enter the student's name: ")
        grades = []
        student = Student(name, grades)
        students.append(student)
    elif choice == 2:
        name = input("Enter the student's name: ")
        for student in students:
            if student.name == name:
                grades = student.retrieve_grades()
                print(f"{name}'s grades: {grades}")
                break
    elif choice == 3:
        name = input("Enter the student's name: ")
        new_name = input("Enter the new name: ")
        for student in students:
            if student.name == name:
                student.update_name(new_name)
                break
    elif choice == 4:
        break
    else:
        print("Invalid choice")

print("Exiting program...")

#4
age=int(input("Enter Your age"))
if(age<=15):
  print("Minor")
elif(age<=25 and age<=45):
  print("Adult")
else:
  print("Senior")

#5
subscriber_ids=[1,2,3,4,5,6] #Example list
even_ids=[i for i in subscriber_ids if i %2==0]
print(even_ids)

#6.
password="Hello"
while(True):
  p=input("Enter your password")
  if(p==password):
    print("Congrats You Entered Right Password")
    break
  else:
    print("Try Again")
    continue

#7.

def calculate_average(numbers):
    if not numbers:
        return None
    c=sum(numbers)/len(numbers)
    return c

print("Enter the list of scores calculated from the survey data")
numbers = list(map(int,input("Enter Number List").split()))
average = calculate_average(numbers)
print(f"Average score is {average} .")

#8.
def count_vowel(s):
  count=0
  for i in s:
    if (i=='a' or i=='e' or i=='i'or i=='o' or i=='u'):
      count+=1
  return count
s=input("Enter your String")
print(f"Number of vowel in the string is {count_vowel(s)}")

#9.
import datetime

# Get the current date and time
now = datetime.datetime.now()

# Create a list of events with date and time
events = [
    {"name": "Meeting", "date": datetime.datetime(now.year, now.month, now.day, 10, 0)},
    {"name": "Lunch", "date": datetime.datetime(now.year, now.month, now.day, 12, 0)},
    {"name": "Appointment", "date": datetime.datetime(now.year, now.month, now.day + 1, 14, 0)},
]

for event in events:
    if event["date"] >= now and event["date"] <= now + datetime.timedelta(hours=1):
        print(f"Reminder: {event['name']} is starting in {int((event['date'] - now).total_seconds() / 60)} minutes.")

if not any(event["date"] >= now and event["date"] <= now + datetime.timedelta(hours=1) for event in events):
    print("No upcoming events within the next hour.")

#10.


def addition(a,b,c):
  try:
    z=m+e
  except TypeError:
    print("Can't add non numeric input")
  z=n+m
  print(f"Total amount is {z}")

while True:
  try:
    n=int(input("Enter the loan principal"))
    m=int(input("Enter the interest for the month"))
    e=int(input("Enter processing fee"))
    addition(n,m,e)
  except ValueError:
      print("Enter valid input")
      continue

#11
def online_poll(question):
  while True:
    mob=input("Enter mobile number:")
    if len(mob)>10:
      print("Enter valid mobile number")
    else:
      break
  while True:
    answer = input(question + " (yes/no): ")
    if answer.lower() in ("yes", "no"):
       return answer.lower()
    else:
       print("Invalid input. Please answer yes or no.")

question = "Do you like maths?"
answer = online_poll(question)

print(f"Your answer: {answer}")

#12
def addition(a,b):
   return a+b
def multiplication(a,b):
   return a*b
def division(a,b):
  try:
    return a/b
  except ZeroDivisionError:
    return "Division by zero gives infinity"


if __name__=="__main__":
  x=int(input("enter first number:"))
  y=int(input("enter second number:"))
  while True:
    choice=int(input("Data processing\n1.addition\n2.multiplication\n3.division\n4.Exit"))
    if choice==1:
       print(addition(x,y))
    elif choice==2:
       print(multiplication(x,y))
    elif choice==3:
       print(division(x,y))
    elif choice==4:
       break
    else:
      print("Invalid choice")
print("Bye...")

#13.
def writting_to_file(filename, content):
    with open(filename, 'w') as file:
        file.write(content)

filename = 'logfile.txt'
content = 'Reports from server'

writting_to_file(filename, content)
print(f'Content "{content}" has been written to the file "{filename}".')

#14.
file=open('/content/logfile.txt','r')
reading_from_file=file.readlines()
print(reading_from_file)

#15.
file=open('/content/market_news.txt','a')
writing_on_file=file.writelines("Company and Industry news")
writing_on_file=file.writelines("Stock market performance")
file.close()
file=open('/content/market_news.txt','r')
reading_from_file=file.readlines()
print(reading_from_file)