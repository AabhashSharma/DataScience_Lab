"""3. Create a generator function using the yield keyword that produces numbers from 1 to
5 one by one to illustrate how lazy evaluation can save memory when dealing with large
datasets."""

def generator():
    for i in range(1,6):
        yield i

number = generator()

for num in number:
    print(num)