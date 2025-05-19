try:
    a = int(input("enter a number: "))
    b = int(input("enter a number: "))
    c = a/b
    print(c)
except ZeroDivisionError:
    print("cannot divide by zero")
except ValueError:
    print("enter a valid number")
except Exception:
    print("something went wrong")
else:
    print("no exception") #if no exception occurs .. try successfully
finally:
    print("this will always execute") #even if exception occurs or not...use in functions

if(b==0):
    raise ZeroDivisionError("cannot divide by zero")     