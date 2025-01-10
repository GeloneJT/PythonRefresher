''' Write a program to display all the even numbers between 1 to 10
 and then print a statement showing the COUNT of even numbers'''

COUNT = 0

for number in range(1, 10):
    if number % 2 == 0:
        COUNT += 1
        print(number)
print(f"We have {COUNT} even numbers ")
