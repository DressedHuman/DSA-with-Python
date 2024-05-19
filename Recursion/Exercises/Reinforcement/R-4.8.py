# Exercises: R-4.8 - Data Structure and Algorithm with Python

def interestingSumUp(A: list[int]):
    """ A is a sequence of n integers where n is a power of 2 """
    if len(A)==2:
        return A[0]+A[1]
    else:
        B = list(map(lambda i: A[2*i]+A[2*i+1], range(len(A)//2)))
        return interestingSumUp(B)


if __name__=="__main__":
    draftA = input("Enter n space separated integers where n is a power of two : ").split()
    A = list(map(int, draftA))
    
    value = interestingSumUp(A)
    print(value)