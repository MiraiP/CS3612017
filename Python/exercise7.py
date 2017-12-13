#a)

list_a = [1,3,5,7]

def print_ele(List):
    for i in List:
        print(i)
    
#print_ele(list_a)


#b)

def reverse(List):
    print("The elements of this list in reverse is: ")
    for i in reversed(List):
        print(i)


#reverse(list_a)

#c)

def leng(List):
    counter = 0

    for i in List:
        counter += 1
        
    print("The length of this list is: " , counter)

#leng(list_a)
