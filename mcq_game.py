
print("Welcome to the McQ Game!")


agree = input("Would you like to participate? ")

if agree != "yes":
    quit()

print("Okay! You got this")
score = 0

answer = input("What does CPU stand for? ")

if answer == "central processing unit":
    print("Okay! Correct")
    score += 1
else:
    print("Incorrect")

answer = input("What does PSU stand for? ")
if answer == "power supply":
    print("Okay! Correct")
    score += 1
else:
    print("Incorrect")

print("Your score is:", score)