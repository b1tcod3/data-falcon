try:
   f = open("data.txt")
   num = int(input("Enter a number: "))
   value = 10 / num
except FileNotFoundError:
   print("The file was not found!")
except ValueError:
   print("Please enter a number.")
except ZeroDivisionError:
   print("Cannot divide by zero!")
else:
    print("Division successful")
finally:
    print("This will always be executed")