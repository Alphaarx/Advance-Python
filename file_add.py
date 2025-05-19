try:
   with open(r"C:\Users\arpan\OneDrive\Documents\py jour\python\adv-py\1.txt", "r") as f:
    # read the entire file
      print(f.read())
except FileNotFoundError:
    print("File not found")
try:    
   with open("2.txt", "r") as f:
    # read the entire file
      print(f.read())
except FileNotFoundError:
    print("File not found")
try:    
   with open("3.txt", "r") as f:
    # read the entire file
      print(f.read())
except FileNotFoundError:
    print("File not found")

print("Thanks for using this program")  