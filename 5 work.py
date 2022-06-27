def count_find_num(primesL, limit):
    base = eval( '*'.join( map(str, primesL) ) )
    
    if base > limit:
        return []
    
    results = [base]
    
    for i in primesL:
        for num in results:
            num *= i
            while num not in results and num <= limit:
                results += [num]
                num *= i
    
    return [ len(results), max(results) ]

print (count_find_num([2, 3], 200))
print (count_find_num([2, 5], 200))
print (count_find_num([2, 3, 5], 500))
print (count_find_num([2, 3, 5], 1000))
print (count_find_num([2, 3, 47], 200))
