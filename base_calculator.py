

def baseCalculate(num, base):
    lst = []
    base = int(base)
    numbr = int(num)
    while numbr > base:
        lst.append(numbr % base)
        numbr = int(numbr/base)
    else:
        lst.append(numbr % base)
        lst.append(int(numbr / base))

    for i in range(len(lst)):
        lst[i] = str(lst[i])
        i =+ 1


    def removeZero(string):
        string = list(string)
        if string[0] == "0":
            string.pop(0)
    
        output = "".join(string)
        return output 

    lst.reverse()
    output = "".join(lst)

    return removeZero(output)


for i in range(100):
   print(type(baseCalculate(i, 2)))
