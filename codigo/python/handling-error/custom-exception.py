class InvalidInputError(Exception):
   pass

try:
   num = int(input("Please enter a number: "))
   if num < 0:
      raise InvalidInputError("Negative number not allowed!")
except InvalidInputError as e:
    print(e)