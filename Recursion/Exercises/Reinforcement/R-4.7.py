def strToInt(strInt, last, count=0, value=0):
    """recursive function, returns the integer that String represents"""

    digits = {
        "0": 0,
        "1": 1,
        "2": 2,
        "3": 3,
        "4": 4,
        "5": 5,
        "6": 6,
        "7": 7,
        "8": 8,
        "9": 9,
    }

    if last<0:
        return value
    elif strInt[last]==".": # 
        return strToInt(strInt, last-1, 0, 0) # removing the floating points as there's a point (.)
    elif last==0 and strInt[0]=="-":
        return -value
    else:
        try:
            digit = digits[strInt[last]]
        except:
            raise ValueError(f"invalid literal for strToInt() with base 10: {strInt}")
        
        value += (10**count)*digit
        return strToInt(strInt, last-1, count+1, value)



if __name__=="__main__":
    str_integer = input("Enter your integer: ")
    print(f"You typed {strToInt(str_integer, len(str_integer)-1)}")