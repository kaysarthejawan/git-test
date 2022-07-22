# spiral traverse
from os import uname_result
from turtle import left


def spiral(array):
    result=[]
    startraw,endraw= 0,len(array)-1
    startcol,endcol=0,len(array[0])-1
    while startraw<= endraw and startcol<=endcol:
        for col in range(startcol,endcol+1):
            result.append(array[startraw][col])
        for row in range(startraw+1 ,endraw+1):
            result.append(array[row][endcol])
        for col in reversed(range(startcol,endcol)):
            result.append(array[endraw][col])
        for row in reversed(range(startraw+1,endraw)):
            result.append(array[row][startcol])
        startraw +=1
        endraw -=1
        startcol +=1
        endcol-=1
    return result


final =[[1,2,3,4],[1,2,3,4],[1,2,3,4],[1,2,3,4]]
print(final)
hello=spiral(final)
print(hello)



#LOngest peak
def longestpeakleangth(array):
    longestpeak=0
    i =1
    while i <len(array)-1:
        ispeak =array[i-1]<array[i] and array[i]>array[i+1]
        if not ispeak:
            i +=1
            continue
        leftidx=i-2
        while leftidx >=0 and array[leftidx] < array [leftidx+1]:
            leftidx -=1
        rightidx=i+2
        while rightidx < len(array)-1 and array[rightidx]<array[rightidx -1]:
            rightidx +=1
        

        currretpeakleangth=rightidx -leftidx-1
        longestpeak=max(longestpeak,currretpeakleangth)
        i= rightidx
    return longestpeak


h=longestpeakleangth(final)
print(h)
