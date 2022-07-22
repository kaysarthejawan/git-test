from tracemalloc import start


def arrange (ar,number) :
    left =0
    right= len(ar)-1
    while left <right :
        while left <right and  ar[right] ==number:
            right -=1
        if ar[left]==number:
                ar[left],ar[right]= ar[right],ar[left]
        left +=1
                
    return ar
           

key=[5,6,6,5,4,5,6,7,5,5,8,5,9]
print(key)
arrange(key,5)
print (key)



