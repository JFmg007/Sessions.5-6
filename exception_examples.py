name = input("What is your name? ")
print("hello", name)
age = input("How old are you? ")
try:
    age = int(age) #I am trying to convert it to number
    # new_age = age / 0
except ValueError:
    print("You are trying to trick me")
    print("Better luck next time")
except ZeroDivisionError:
    print("You can't divide by zero")
except:
    print("something unexpected happened")
else: # this happens if no error occurred
    print("You were probably born in", 2024 - age)
finally:
        print("thanks for playing")