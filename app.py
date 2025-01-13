'''Python Functions - Sets'''

numbers = [1, 2, 3, 4]
first = set(numbers)
second = {1, 5}

# returns a new set of all items that are in the first or second set  {1, 2, 3, 4, 5}
print(first | second)
# returns a new set of all the items that are both in the first and second set {1}
print(first & second)
# returns a new set of the difference of the items of the first and second set {2, 3, 4}
print(first - second)
#  returns a new set of items that are in the first or second set but not both {2, 3, 4, 5}
print(first ^ second)
