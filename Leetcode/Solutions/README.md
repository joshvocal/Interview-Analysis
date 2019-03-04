# Question

Given a collection of distinct integers, return all possible permutations.

Example:

Input: [1,2,3]

Output:
[
  [1,2,3],

  [1,3,2],

  [2,1,3],

  [2,3,1],

  [3,1,2],

  [3,2,1]
]

# Solution

## Approach 1: Breadth First Search

Create all the permutations by level. First add all the single elements to the queue. Once all the single elements are done, make all permutations of 2 elements and than 3.

```python
def permute2(self, nums):
    """
    :type nums: List[int]
    :rtype: List[List[int]]
    """
    res = [[]] # A Queue

    while len(res[len(res) - 1]) < len(nums):
        temp = res.pop()
        for num in nums:
            if num not in temp:
                inner = list(temp)
                inner.insert(0, num)
                res.insert(0, inner)

    return res
```

### Walk Through


```python
# Initial Queue In --> Out 

[[]]

# First Layer

[[3], [2], [1]] # Pop off [1]

[[3, 1], [2, 1], [3], [2]] # Pop off [2]

[[3, 2], [1, 2], [3, 1], [2, 1], [3]] # Pop off [3]

# Second Layer

[[2, 3], [1, 3], [3, 2], [1, 2], [3, 1], [2, 1]] # Pop off [1, 2]

[[3, 2, 1], [2, 3], [1, 3], [3, 2], [1, 2], [3, 1]] # Pop off [3, 1]

[[2, 3, 1], [3, 2, 1], [2, 3], [1, 3], [3, 2], [1, 2]] # Pop off [1, 2]

[[3, 1, 2], [2, 3, 1], [3, 2, 1], [2, 3], [1, 3], [3, 2]] # Pop off [3, 2]

[[1, 3, 2], [3, 1, 2], [2, 3, 1], [3, 2, 1], [2, 3], [1, 3]] # Pop off [1, 3]

[[2, 1, 3], [1, 3, 2], [3, 1, 2], [2, 3, 1], [3, 2, 1], [2, 3]] # Pop off [2, 3]

# Third Layer

[[1, 2, 3], [2, 1, 3], [1, 3, 2], [3, 1, 2], [2, 3, 1], [3, 2, 1]]

# All the items in the queue of the same length as the initial array 

```

## Approach 2: Depth First Search

Create all combinations for a single number first, then build the rest of the numbers up.

```python
def permute(self, nums):
    """
    :type nums: List[int]
    :rtype: List[List[int]]
    """
    res = []
    self.backtrack(res, [], nums)
    return res

def backtrack(self, res, tmpList, nums):
    if len(tmpList) == len(nums):
        res.append(list(tmpList))
    else:
        for num in nums:
            if num not in tmpList:
                tmpList.append(num)
                self.backtrack(res, tmpList, nums)
                tmpList.remove(tmpList[-1]) # Remove the last element in the list
```

## Walk Through

```python
for num in nums:
    if num not in tmpList:
        tmpList.append(num)
        self.backtrack(res, tmpList, nums)
        tmpList.remove(tmpList[-1])

# Recursively go down to the deepest combination of 3 numbers for one.
```

```
                            []
                    / 
                [1] 
```

```
                            []
                    /   
                [1] 
              /  
        [1,2] 
```

```
                            []
                    /  
                [1] 
              /  
        [1,2] 
          / 
    [1,2,3] 
```

We've reached a combination of 3, add it to our result lists. Remove the last element in the list so we add another combination of 3

```
                            []
                    /    
                [1] 
              /  |  
        [1,2]  [1,3] 
          / 
    [1,2,3] 
```

```
                            []
                    / 
                [1]  
              /  | 
        [1,2]  [1,3] 
          /      | 
    [1,2,3]   [1,3,2]
```

Add [1,3,2] to the result list

```
                            []
                    /       |  
                [1]        [2]
              /  |    
        [1,2]  [1,3] 
          /      |  
    [1,2,3]   [1,3,2] 
```

```
                            []
                    /       | 
                [1]        [2] 
              /  |        / 
        [1,2]  [1,3]    [2,1]
          /      |  
    [1,2,3]   [1,3,2]
```

```
                            []
                    /       | 
                [1]        [2] 
              /  |        / 
        [1,2]  [1,3]    [2,1]
          /      |        |  
    [1,2,3]   [1,3,2] [2,1,3]
```

Add [2, 1, 3]

```
                            []
                    /       | 
                [1]        [2] 
              /  |        /   \  
        [1,2]  [1,3]    [2,1] [2,3] 
          /      |        | 
    [1,2,3]   [1,3,2] [2,1,3]
```

```
                            []
                    /       |  
                [1]        [2] 
              /  |        /   \ 
        [1,2]  [1,3]    [2,1] [2,3] 
          /      |        |      | 
    [1,2,3]   [1,3,2] [2,1,3]  [2,3,1] 
```

Add [2, 3, 1]

```
                            []
                    /       |       \
                [1]        [2]       [3]
              /  |        /   \    
        [1,2]  [1,3]    [2,1] [2,3]
          /      |        |      | 
    [1,2,3]   [1,3,2] [2,1,3]  [2,3,1] 
```

```
                            []
                    /       |       \
                [1]        [2]       [3]
              /  |        /   \         |
        [1,2]  [1,3]    [2,1] [2,3]    [3,1]
          /      |        |      |  
    [1,2,3]   [1,3,2] [2,1,3]  [2,3,1] 
```

```
                            []
                    /       |       \
                [1]        [2]       [3]
              /  |        /   \         |  
        [1,2]  [1,3]    [2,1] [2,3]    [3,1] 
          /      |        |      |       |  
    [1,2,3]   [1,3,2] [2,1,3]  [2,3,1]  [3,1,2]
```

Add [3, 1, 2]

```
                            []
                    /       |       \
                [1]        [2]       [3]
              /  |        /   \         |    \
        [1,2]  [1,3]    [2,1] [2,3]    [3,1]    [3,2]
          /      |        |      |       |  
    [1,2,3]   [1,3,2] [2,1,3]  [2,3,1]  [3,1,2]
```


```
                            []
                    /       |       \
                [1]        [2]       [3]
              /  |        /   \         |    \
        [1,2]  [1,3]    [2,1] [2,3]    [3,1]    [3,2]
          /      |        |      |       |         |
    [1,2,3]   [1,3,2] [2,1,3]  [2,3,1]  [3,1,2]   [3,2,1]
```

Add [3, 2, 1]
