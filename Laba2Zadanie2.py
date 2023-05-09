def multiplicate(m, p, i):
    proizv = 1.0
    for j in range(1, m+1):
        proizv *= ((2*p + i)/(j**2 + i))
    return proizv  

def func(n, m, p):
    rez = 0.0
    for i in range(1, n+1) :
        rez += ((i**2 + p) / (i+2)) * multiplicate(m, p, i)
    print(rez)
        
func(n = int(input("N = ")), m = int(input("M = ")), p = float(input("p = "))) 

""" 4/3 * 7/2 * 7/5 + 7/4 * 8/6 * 8/3 = 4*49 / 6*5  +  7*64 / 24*3 = 574/45 = 12,7(5) """