# Challenge Summary - Merge-Sort

It divides the input array into two halves, calls itself for the two halves, and then merges the two sorted halves.

## Approach & Efficiency
time ==> O(n^2)
space ==> O(1)

## Solution

```

def mergeSort(arr):
  n = len(arr)
 
  if n>1:
    mid = int(n/2)
    left = arr[0:mid]
    right = arr[mid:n]

    mergeSort(left)
    mergeSort(right)
    merge(left,right,arr)
  return arr

def merge(left,right,arr):
  i = 0
  j = 0
  k = 0  
  while i < len(left) and j < len(right):
   
    if left[i] <= right[j]:
      arr[k] = left[i]
      i = i+1

    else:
      arr[k] =right[j]
      j= j+1
    k = k+1
  while i < len(left):
        arr[k] = left[i]
        i += 1
        k += 1

  while j < len(right):
        arr[k] = right[j]
        j += 1
        k += 1
```



https://github.com/jariryyousef/data-structures-and-algorithms/pull/34




# Challenge Summary - Quick-Sort
A sorting technique that sequences a list by continuously dividing the list into two parts and moving the lower items to one side and the higher items to the other. It starts by picking one item in the entire list to serve as a pivot point. The pivot could be the first item or a randomly chosen one.


## Approach & Efficiency

time ==> O(n^2)  
space ==> O(n)  

## Solution 
```
def QuickSort(arr, left, right):

  if left < right:
    position = Partition(arr, left, right)
    QuickSort(arr, left, position - 1)
    QuickSort(arr, position + 1, right)
  return arr

def Partition(arr, left, right):
  
  pivot = arr[right]
  low = left -1
  for i in range(left,right):
    if arr[i] <= pivot:
      low= low+1
      Swap(arr, i, low)
  Swap(arr, right, low + 1)
  return low + 1


def Swap(arr, i, low):
  
  temp = arr[i]
  arr[i] = arr[low]
  arr[low] = temp


```

https://github.com/jariryyousef/data-structures-and-algorithms/pull/35