print("Welcome to the tip calculator!")
a=int(input("What was the total bill?$"))
b=int(input("How much tip would you like to give? 10, 12, or 15?"))
c=int(input("How many people to split the bill?"))
d=((a*(b/100))+a)/c
f=round(d,2)
e=str(f)
print("Each person should pay:$"+(e))
