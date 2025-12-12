# sum of 2 number
try:
    a = float(input("enter first number:"))
    b = float(input("enter second number:"))

    if(a.is_integer() and b.is_integer()):
        a=int(a)
        b=int(b)

    print(f" the sum of {a} and {b} is:{a+b}")

except ValueError:
    print("Invalid Input.Please enter a number ")