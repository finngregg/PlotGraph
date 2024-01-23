import math

func = input("Enter a function f(x):\n")

def newfunc(x):
        newfunc=round(eval(func))
        return newfunc
        
for y in range(-10,11):
        for x in range(-10,11):
                if y==-newfunc(x):
                        print("*", end="")
                elif y==0 and x==0:
                        print("+", end="")
                elif y==0:
                        print("-", end="")
                elif x==0:
                        print("|", end="")
                else:
                        print(" ", end="")
        print()





