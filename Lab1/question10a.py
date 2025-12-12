#A program that takes the age of an user, and gives their birth year, and if birth
# year was a leap year.

import datetime

def calculate_age(age):
  year = datetime.datetime.now().year

  birth = year - age
  if((birth  % 4 == 0 and birth % 100 != 0) or birth % 400 == 0):
    print(f"your birth year {birth} is a leap year")
  else:
    print(f"your birth year {birth} is not a leap year")
  return birth

def birth_year():
    try:
       age = int(input("enter your age:"))
    except:
       print("Invalid age") 
    return age         
