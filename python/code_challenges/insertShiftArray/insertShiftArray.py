

n=6

def fun(n):
    arr=[0,1,2,3,4,6,7,8]
    
    for i in range (len(arr)):
        index=arr.index(i)
        if (n==arr[i]):
            return index

print(fun(n))