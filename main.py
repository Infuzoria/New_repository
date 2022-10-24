def symmator (lis):
    a = 1
    for i in range (0, len(lis)):
        a *= lis[i]
    return a
print(symmator([1,2,3,4,5]))