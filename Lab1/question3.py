# prime number

num = int(input("enter a number:"))

for i in range (2,num+1):
    prime_number=0
    for j in range (2,i+1):
        if i%j == 0:
            prime_number +=1
    
    if prime_number == 1:
        print(i)
            
