found = 0
x = 11

while found < 20:
    if (x % 5 == 0) & (x % 7 == 0) & (x % 11 == 0):
        print(x)
        found += 1
    x+=1
