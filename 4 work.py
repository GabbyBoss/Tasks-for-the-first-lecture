import itertools

def bananas(s):
    result = set()
    
    for test in itertools.combinations(range(len(s)), len(s) - 6):
        arr = list(s)
        
        for i in test:
            arr[i] = '-'
        
        candidate = ''.join(arr)
        
        if candidate.replace('-', '') == 'banana':
            result.add(candidate)
    
    return result

print (bananas('banann'))
print (bananas('banana'))
print (bananas('bbananana'))
print (bananas('bananaaa'))
print (bananas('bananana'))