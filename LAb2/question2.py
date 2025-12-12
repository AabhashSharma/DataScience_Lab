''' Take a paragraph input from the user. Split it into words, remove duplicates, sort them
alphabetically, and count the total number of unique words.'''

a=input("Enter a paragraph:").split()

w=set(a)
sort=sorted(w)