def log(num, base=10): # calculating the base based log of num using the binary search algorithm
    if num<0:
        return float('NaN')
    
    low = 0.0
    high = float(num)
    tolerance = 1e-10

    while high-low > tolerance:
        mid = (low+high)/2

        if base**mid<num:
            low = mid
        elif base**mid>num:
            high = mid
        else:
            return mid
    return low



if __name__=='__main__':
    # print(log(16))
    num = float(input('Enter number: '))
    print(f'log of {num} is {log(num=num)}')