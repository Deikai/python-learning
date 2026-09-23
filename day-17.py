# Day 17 - Error Handling

# Example 1: ValueError
try:
    age = int(input("Enter your age: "))
    print("Your age is", age)

except ValueError:
    print("Please enter a valid age.")

finally:
    print("Program finished.")


# Example 2: ValueError + ZeroDivisionError
try:
    first = int(input("Enter the first number: "))
    second = int(input("Enter the second number: "))

    result = first / second

except ValueError:
    print("Please enter a valid number.")

except ZeroDivisionError:
    print("You cannot divide by zero.")

else:
    print("The result is", result)

finally:
    print("Program finished.")


# Example 3: Age classification
try:
    age = int(input("Enter your age: "))

except ValueError:
    print("Please enter a valid age.")

else:
    if age >= 18:
        print("Adult.")
    elif age >= 13:
        print("Teenager.")
    else:
        print("Child.")

finally:
    print("Program finished.")


# Example 4: Score validation
try:
    score = int(input("Enter your score: "))

except ValueError:
    print("Please enter a valid score.")

else:
    if score > 100 or score < 0:
        print("Invalid score.")
    elif score >= 90:
        print("Excellent")
    elif score >= 80:
        print("Good")
    elif score >= 70:
        print("Passed")
    else:
        print("Failed")

finally:
    print("Program finished.")


# Example 5: Negative, zero, positive odd/even
try:
    number = int(input("Enter your number: "))

except ValueError:
    print("Please enter a valid number.")

else:
    if number < 0:
        print("Negative number")
    elif number == 0:
        print("Zero")
    elif number % 2 != 0:
        print(number, "positive odd number")
    else:
        print(number, "positive even number")

finally:
    print("Program finished.")

#practicas personales 
try:
    number = int(input("Enter a number: "))
    number2 = int(input("Enter the second number: "))
    result = number / number2

except ValueError:
    print("Please enter a valid number.")
except ZeroDivisionError:
    print("You cannot divide by zero.")
else:
    print("The result is", result)

finally:
    print("Program finished.")


try:
    age = int(input("Enter your age: "))
    print("Your age is", age)

except ValueError:
    print("Please enter a valid age.")

finally:
    print("Program finished.")




try:
    first = int(input("Enter the first number: "))
    second = int(input("Enter the second number: "))
    result = first / second

except ValueError:
    print("Please enter a valid number.")
except ZeroDivisionError:
    print("You cannot divide by zero.")
else:
    print("The result is", result)

finally:
    print("Program finished.")



try:
    age = int(input("Enter your age: "))

except ValueError:
    print("Please enter a valid age.")
else:
    if age >= 18:
        print("Adult.")
    elif age >= 13:
        print("teenager.")
    else:
        print("child")

finally:
    print("Program finished.")


try:
    score = int(input("Enter your score: "))

except ValueError:
    print("Please enter a valid score.")
else:
    if score > 100 or score < 0:
        print("Invalid score.")
    elif score >= 90:
        print("Excellent")
    elif score >= 80:
        print("Good")
    elif score >= 70:
        print("Passed")
    else:
        print("Failed")

finally:
    print("Program finished.")


try:
    numcom = int(input("Enter your number"))

except ValueError:
    print("Please enter a valid number")
else:
    if numcom < 0:
        print("Negative number")
    elif numcom == 0:
        print("Zero")
    elif numcom >= 1 and numcom % 2 != 0:
        print(numcom, "positive odd number")
    else:
        print(numcom, "positive even number")

finally:
    print("Program finished")

