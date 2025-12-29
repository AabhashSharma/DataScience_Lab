''' Take a paragraph input from the user. Split it into words, remove duplicates, sort them
alphabetically, and count the total number of unique words.'''

para = input("Enter a paragraph: ").split(" ")
word_freq = {}
for i in para:
    word_freq[i] = word_freq.get(i, 0) + 1

uw = set(para)
w = list(uw)
w = sorted(w)
count = len(w)

print(f"Unique Words: {w}")
print(f"Count: {count}")
print(f"Word frequency : {word_freq}")
