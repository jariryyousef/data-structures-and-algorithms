def inserttion(arr):
  n = len(arr)
  for i in range (n-1):
    min = i
    for j in range(i+1,n):
      if (arr[j] < arr[min]):
        min = j
        
    temp = arr[min]
    arr[min] = arr[i]
    arr[i] = temp
    
  return arr