"""2. File Processing with Exception Handling
● Reads numbers from a text file (one number per line)
● Ignores invalid entries using exception handling
● Calculates and displays the sum and average of valid numbers"""

try:
    total = 0
    count = 0

    with open("q2.txt", "r") as file:
        for line in file.readlines():
            try:
                num = int(line.strip())
                total += num
                count += 1
            except ValueError:
                continue

    if count > 0:
        print(f"Sum: {total}")
        print(f"Average: {total / count}")
    else:
        print("No valid numbers found in the file.")

except FileNotFoundError:
    print("File not found.")
