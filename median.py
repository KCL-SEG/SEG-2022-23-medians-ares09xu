"""Median calculator."""
"""ENTER YOUR SOLUTION HERE!"""

def is_odd(int):
    if int % 2 != 0:
        return True
    else:
        return False

while True:
    try:
        print("Enter a list of numbers separated by commas: ")
        numbers = [float(value) for value in input().split(",")]
    except ValueError:
        print("Some input could not be converted to a number!")
    else:
        break
median = 0
if is_odd(len(numbers)):
    median = numbers[int((len(numbers)+1)/2-1)]
else:
    median = (numbers[int(len(numbers)/2-1)] + numbers[int(len(numbers)/2)])/2
print(median)
