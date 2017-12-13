#a)
def is_prime(n):
    if n<2:
        return False
    elif n == 2:
        return True
    elif n % 2 == 0:
        return False
    elif n>2:
        for y in range(2,n):
            if n % y == 0:
                return False
        else:
            return True

#print("A)" , is_prime(1))
#print(is_prime(2))
#print(is_prime(3))
#print(is_prime(17) , ":17")

#b)

def is_prime2(n):
    if n == 2 or n == 3:
        return True
    elif (n + 1) % 6 != 0 and (n - 1) % 6 != 0: #Checking in reverse, huh. If it's not of form, then False.
        return False #Needs to be "and", not "or" it seems. Otherwise 13 -> 14 fails one condition and gets a False.
    elif n>3:
        for y in range(2,n):
            if n % y == 0:
                return False
        else:
            return True


#print("B)" , is_prime2(2))
#print(is_prime2(3))
#print(is_prime2(4))
#print(is_prime2(5))

#c)
def upto_prime(n):
    for y in range (2,n+1): #It doesn't seem to include n, so here's n+1. Unless I don't understand the meaning of "up to"
        if is_prime2(y):
            print(y)
    
    
#print(upto_prime(31)) #not quite sure where the none comes from. 

def first_primes(n):
    counter = 0
    i = 2 #an increasing number that we check is prime.
    while counter < n:
        if is_prime2(i):
            print(i)
            counter += 1 #printed a prime
            i += 1
        else:
            i += 1

    
#first_primes(10)

