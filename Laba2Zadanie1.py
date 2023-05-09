import math

x = float(input("x =  "))
def intervals(x):
    if x == 0 or  x == 6 or x<=4 and x>=2:
        y = 3*math.cos(x)
    elif x==12 or x<=37.5 and x>=30:
        y = x/4-5
    elif x<0 or x==90 or x==105.5 or x<=159 and x>=150:
        y = 2*x+1
    else:
        y = x
    print(y)

intervals(x)