# Write a program to display all the even numbers between 1 to 10 and then print a statement showing the count of even numbers

count = 0
for number in range(1, 10):
    if number % 2 == 0:
        count += 1
        print(number)
else:
    print(f"We have {count} even numbers ")