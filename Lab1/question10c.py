from question10a import birth_year , calculate_age
from question10b import bmi

def army_check(age , bmi):

    if((age >= 18 and age <=40) and (bmi >= 18.5 and bmi <= 29.9)):
        print("you are eligible for army entrance")
    else:
        print("you are not eligible for army entrance")    

age = birth_year()
birthyear = calculate_age(age)
bmi = bmi()    

print(f"Age {age}")
print(f"Bmi:{bmi}")

army_check(age , bmi)

