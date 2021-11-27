# Hashtables
A hash table is a special collection that is used to store key-value items. So instead of storing just one value like the stack, array list and queue, the hash table stores 2 values. These 2 values form an element of the hash table

## Challenge
- Implement a Hashtable Class with the following methods:

- add  
  Arguments: key, value  
  Returns: nothing  
  This method should hash the key, and add the key and value pair to the table, handling collisions as needed.  

- get  
  Arguments: key  
  Returns: Value associated with that key in the table  

- contains  
  Arguments: key  
  Returns: Boolean, indicating if the key exists in the table already.  

- hash  
    Arguments: key  
    Returns: Index in the collection for that key  

## Approach & Efficiency  
- space ==> O(n)
- time ==> O(1)

## API

- hash:  
    Arguments: key  
    Returns: Index in the collection for that key  

- add:  
  Arguments: key, value  
  Returns: nothing  

- get:  
  Arguments: key  
  Returns: Value associated with that key in the table  

- contains:  
  Arguments: key  
  Returns: Boolean


https://github.com/jariryyousef/data-structures-and-algorithms/pull/37

# Code Challenge 31 | Hashmap Repeated Word
- Find the first repeated word in a book.


## Whiteboard Process
![](CodeCh31.PNG)

## Approach & Efficiency
- time ==> O(n)
- space ==> O(n)

## Solution
```
    def repeated_word(self,string):
      hash_table = HashTable()
      string = re.sub('[^A-z ]+', '', string).split(" ")
      for i in string:
        i = i.lower()
        if i and hash_table.contains(i):return i
        hash_table.add(i,i)

```
https://github.com/jariryyousef/data-structures-and-algorithms/pull/39




# Code Challenge 32 | Hashmap Repeated Word
- Find common values in 2 binary trees.


## Whiteboard Process
![](CC32.PNG)

## Approach & Efficiency
- time ==> O(n)
- space ==> O(n)

## Solution
```
def tree_intersection(tree1,tree2):
  tree1_list = tree1.pre_order()
  tree2_list = tree2.pre_order()
  hash_table = HashTable()
  result = []
  
  for i in tree1_list:
    hash_table.add(i,i)
  
  for i in tree2_list:
    if hash_table.contains(i):
      result.append(i)
  return result

```
https://github.com/jariryyousef/data-structures-and-algorithms/pull/41




# Code Challenge 33 | LEFT JOIN 
- Implement a simplified LEFT JOIN for 2 Hashmaps.


## Whiteboard Process
![CC33.jpg](CC33.jpg)

## Approach & Efficiency
- time ==> O(n)
- space ==> O(n)

## Solution
```
    def left_join(hash1, hash2):

        arr = []
        for i in hash1.buckets:
            if i:
                if hash2.contains(i.head.value[0]):
                    right_item = hash2.get(i.head.value[0])
                    arr.append([i.head.value[0], i.head.value[1],right_item])
                else:
                    arr.append([i.head.value[0], i.head.value[1],'Null'])
        return arr

```
https://github.com/jariryyousef/data-structures-and-algorithms/pull/44