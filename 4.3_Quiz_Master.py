'''
QUIZ MASTER PROJECT
-------------------
The criteria for the project are on the website. Make sure you test this quiz with 
two of your student colleagues before you run it by your instructor.
'''
print("welcome to my quiz about random things")
ans = input("are you ready to begin?""        a. yes"
            "       b. no")
if ans.lower() == "a":
    print("have fun all your data will be stolen and sold to the highest bidder")
else:
    print("Then stop wasting my time")
    exit()

z = int(input("how moons does pluto have?"))
if z == 5:
    print("corret")
else:
    print("incorrect pluto has 5 moons")
a = input("Which Graphics card is better?"
          "       a. GeForce RTX 2060"
          "       b. Radeon R9 380")
if a.lower() == "a":
    print("correct")
else:
    print("incorrect")
b = input("How many holes are in a straw?"
          "    a. 2"
          "    b. 1")
if b.lower() == "b":
    print("correct")
else:
    print("that is incorrect there is only one hole in a straw.")
c = input("Who won super bowl 21?"
          "      a.New England Patriots"
          "      b.New York Jets"
          "      c.New York Giants"
          "      d.Minnesota Vikings")
if c.lower() == "c":
    print("correct! They beat the Denver Broncos 39-20")
else:
    print("NOPE")
d = input("What is your name?")
print("Imagine carrying around in your stomach for 9 months just to name it",d)
e = (input("how long is one day"
              "      a. 12 hours"
              "      b. 24 hours"
              "      c. 23 hours 56 minutes and 4 seconds"))
if e.lower() == "c":
    print("correct a full rotation of the earth isn't exactly 24 hours")
else:
    print("incorrect")






