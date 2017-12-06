print("a)", float(123))
print("Converts the int 123 into a float, which adds the decimal.\n")

print("b)",float('123'))
print("Converts the string 123 into a float. \n")

print("c)",float('123.23'))
print("Converts the string 123.23 into a float. \n")

print("d)",int(123.23))
print("Converts the float 123.23 into an int, removing everything past the decimal. \n")

print("e) int('123.23')")
print("Attempts to converts the string 123.23 into an int, but fails.")
print("Likely due to the decimal point - valueerror mentions base 10. \n")


print("f)",int(float('123.23')))
print("Now returns 123 because the system is able to convert a float into an int, which is the first step. \n")

print("g)", str(12))
print("Converts the int 12 into a string. \n")

print("h)", str(12.2))
print("Converts the float 12.2 into a string. \n")

print("i)", bool('a'))
print("Converts the string 'a' into a boolean, which apparently is True.")
print("It seems that only the values 0 and False will return False. \n")

print("j)", bool(0))
print("Returns false, based off of a binary system of 0s and 1s. \n")

print("k)", bool(0.1))
print("Returns true, since 0.1 has no significance in terms of bools.")
print("Interestingly enough if you cast it into an int it's false again.")
