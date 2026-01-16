"""4. Write a Python script that takes a list of six student names and uses the
random.sample() function to randomly select exactly three "Volunteers" for a
presentation, ensuring that no student is picked more than once in the selection."""

import random

#random.seed(10)
name=["Aabhash","Shreyan","Ram","Hari","Shyam","Sita"]

select = random.sample(name,3)

print(select)