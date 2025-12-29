'''1. Basic File Read & Write
● Create a text file and write multiple lines into it
● Read the contents of the file and display them on the screen
● Handle the case where the file does not exist using try-except '''


with open("file.txt", "w") as file:
    file.write("Hello\n")
    file.write("This\n")
    file.write("is\n ")

try:
    with open("file.txt","r") as file:
        f=file.read()
        print(f)
except FileNotFoundError:
    print("File doesnot exist")