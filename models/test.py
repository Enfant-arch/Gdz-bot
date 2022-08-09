def count_bits(n):
    notgood = bin(n)
    good = notgood[2:]
    lst = []
    for i in good:
        lst.append(int(i))
    return sum(lst)
   
count_bits(1234)