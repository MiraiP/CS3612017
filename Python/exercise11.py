def iter(List):
    product = 1

    if List == []:
        return ("Empty List")
        
    for i in List:
        product *= i
        
    return(product)

listo = [2,4,6]


#print(iter(listo))


def recur(List):
    if List == []:
        return 1
    else:
       return List[0] * recur(List[1:])
    
#print(recur(listo))
