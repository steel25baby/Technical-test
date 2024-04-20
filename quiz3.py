""""Question 3: Power of Two
Write a program that takes an integer as input and returns true if the input is a power of two."""
def is_power_of_two(num):
    if num <= 0:
        return False
    return num & (num - 1) == 0

print(is_power_of_two(8)) # returns True