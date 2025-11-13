# Sameer Dattatraya Jadhav

# Exercise 1:   Prime Numbers
# Write a Python program that checks whether a given number is prime or not.
# A prime number is a natural number greater than 1 that has no positive divisors other than 1 and itself.

def is_prime(num):
    # Prime number is greater than 1
    if num <= 1:
        return False
    
    # Check divisibility from 2 to sqrt
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

number = int(input("Enter a number: "))

if is_prime(number):
    print(f"{number} is a Prime Number")
else:
    print(f"{number} is Not a Prime Number")

########################################

# Exercise 2:   Product of Random Numbers
# Develop a Python program that generates two random numbers and asks the user to enter the product of these numbers.
# The program should then check if the user's answer is correct and display an appropriate message.

import random

# Generate two random numbers
num1 = random.randint(1, 10)
num2 = random.randint(1, 10)

# Ask the user to calculate the product
print(f"What is {num1} x {num2}?")
answer = int(input("Enter your answer: "))

# Check the correct answer
correct_answer = num1 * num2

if answer == correct_answer:
    print(f" Answer is Correct!")
else:
    print(f"Incorrect answer. The correct answer is {correct_answer}.")

#########################################

# Exercise 3:   Squares of Even/Odd Numbers
# Create a Python script that prints the squares of all even or odd numbers within the range of 100 to 200. 
# Choose either even or odd numbers and document your choice in the code.

for num in range(100, 201):  
    if num % 2 == 0:  # checks number is even
        print(f"{num}^2 = {num ** 2}")

#########################################

# Exercise 4:
# Problem Statement (Question): Hospital Billing System

# Charges
room_charge_per_day = 2000
Doctor_consultation_fee = 1500
lab_test_cost = 300

# Patient details
days_stayed = 4
num_tests = 3
medicine_charges = 2400

# Bill calculation
room_charges = room_charge_per_day * days_stayed
lab_charges = lab_test_cost * num_tests

total_before_discount = room_charges + Doctor_consultation_fee + lab_charges + medicine_charges

# Discount 
if total_before_discount > 10000:
    discount = total_before_discount * 0.10
else:
    discount = 0

final_bill = total_before_discount - discount

# Output
print("----- Hospital Bill -----")
print(f"Room Charges: ₹{room_charges}")
print(f"Doctor Consultation Fee: ₹{Doctor_consultation_fee}")
print(f"Lab Test Charges: ₹{lab_charges}")
print(f"Medicine Charges: ₹{medicine_charges}")
print(f"Total (before discount): ₹{total_before_discount}")
print(f"Discount: ₹{discount}")
print(f"Final Bill Amount: ₹{final_bill}")
