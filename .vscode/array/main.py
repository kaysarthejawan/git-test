from cmath import inf


print("hello")
def traverse(ar):

    left= 0
    right= len(ar)-1
    while left<right:
        ar[left],ar[right]=ar[right],ar[left]
        left +=1
        right -=1
    


t=[5,6,9,8,9,4,67,78,89]
print(t)
traverse(t)
print(t)
def sumtwo (ar,target):
    sorted(ar)
    left = 0
    right= len(ar)-1
    while left<right:
        data=ar[left]+ar[right]
        if data==target:
            return [ar[left],ar[right]]
        elif data<target:
            right -=1
        elif data>target:
            left +=1


jawann=sumtwo(t,11)
print(jawann)
def threesum(ar,key):
    sorted(ar)
    triplets=[]
    
    for i in range(len(ar)-2):
        left =i+1
        right= len(ar)-1
        while left <right :
            data = ar[i]+ar[left]+ar[right]
            if data == key:
                triplets.append([ar[i],ar[left],ar[right]])
                left +=1
                right -=1
                
                
 
            elif data<key:
                left +=1
            elif data >key :
                right -=1
    return triplets
k=[78,89,99,100]
def smalldif (ar1,ar2):
    sorted(ar1)
    sorted (ar2)
    idx1=0
    idx2=0
    smaallest=float(inf)
    current= float(inf)
    pair=[]
    while idx1< len(ar1) and idx2< len(ar2):
        firstname= ar1[idx1]
        secondname= ar2[idx2]
        if firstname<secondname :
            current=secondname-firstname
            idx1+=1
        elif firstname>secondname:
            current=firstname-secondname
        else:
            return [firstname,secondname]
        


ar1=[2,6,7,8,9]
ar2=[9,4,3,22,6]
print(smalldif( ar1,ar2))










