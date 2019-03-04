# Question

Merge two sorted linked lists and return it as a new list.

The new list should be made by splicing together the nodes of the first two lists.

**Example**

```
Input: 1->2->4, 1->3->4
Output: 1->1->2->3->4->4
```

# Solution

## Approach 1: Merge from Mergesort

* Create three pointers for the linked lists: `l1`, `l2` and `l3`
* Find the minimum between `l1` and `l2`
* Point `l3` to the minimum between `l1` and `l2`
* Advance the minimum pointer
* Advance `l3`
* If there are no more elements in either `l1` or `l2`, add the remaining elements to `l3`

## First Principle

* Understand the merge function from mergesort

```go
function merge(left, right)
    var result := empty list

    while left is not empty and right is not empty do
        if first(left) ≤ first(right) then
            append first(left) to result
            left := rest(left)
        else
            append first(right) to result
            right := rest(right)

    // Either left or right may have elements left; consume them.
    // (Only one of the following loops will actually be entered.)
    while left is not empty do
        append first(left) to result
        left := rest(left)
    while right is not empty do
        append first(right) to result
        right := rest(right)
    return result
```

## Code

```python
class Solution:
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        dummy = ListNode(-1)
        l3 = dummy
        
        while l1 and l2:
            if l1.val > l2.val:
                l3.next = l2
                l2 = l2.next
            else:
                l3.next = l1
                l1 = l1.next
            l3 = l3.next
            
        l3.next = l1 if l1 else l2
        
        return dummy.next
        
```

## Complexity

Time: O(n + m): We need to iterate through all the elements in both arrays, `n` and `m`

Space: O(1): We are not using any extra space and just using the arrays provided
