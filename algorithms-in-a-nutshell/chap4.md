# Sorting Algorithms

- a lot of computations become simple by properly sorting info in advance 
- collections may already be in RAM, but it might be on a file, or even worse archived on tape 
  - soooo information may beed to be copied before it can be processed 
- information in RAM typically takes one of two forms 
  - pointer-based - elements in the array are pointers to the information
  - value-based  - elements are stored in record blocks of fixed size 
- lexicographical ordering - ordering is imposed on ech individual element of the composite like strings 
  - each letter is compared until a word runs ot of characters or an individual character in one word is different from its partner 
    - "ant" is less than "anthem"
    - "alphabet" is less than "alternate"
- collation algorithm - the algorithm unicode has developed for sorting unicode 
- stable sorting - comparing two elements in a collection as equal, it may be important to maintain their relative ordering 
  - example a sorted collection of flight info already sorted by time 
  - then gets resorted by destination city 
  - after the resort the collection is ordered by destination city and time 
## Criteria for Choosing a Sorting Algorithm

- only a few items - insertion sort 
- items are mostly sorted already - insertion sort 
- concerned about worst-case scenarios - heap sort 
- interested in good average-case behavior - quick sort 
- items are drawn from a uniform dense universe - bucket sort 
- desire to write as little code as possible - insertion sort 
- require stable sort - merge sort 

## Transposition Sorting 
- find elements in a collection that are out of place and move them into their proper position by swapping (transposing) the elements 
### Insertion Sort 
```
  sort (A)
    for pos = 1 to n-1 do
      insert (A, pos, A[pos])
  end

  insert (A, pos, value)
    i = pos - 1
    while i >= 0 and A[i] > value do 1
      A[i+1] = A[i]
      i = i-1
    A[i+1] = value 2
  end
```
  - requires very little extra space to function 
  - best case scenario it will run in O(n)
  - worst case scenario O(n^2)
  - bad for value-based data due to the amount of memory that must be shifted to make room 

### Selection Sort 
- selection sort -
  - select the largest value from range A[0,n) and swap its location with the rightmost element A[n-1]
  - repeat on each successive smaller range A[0,n-1) until A is sorted 
  - slowest algorithm 
    - best case O(n^2)
    - worst case O(2^n)
    - not even going to put pseudocode for this 

### Heap Sort 
- heap - tree that satisifies these two properties 
  - shape 
    - a leaf node at depth k > 0 can exist only if all 2 nodes at depth k - 1 exist 
    - nodes at partially filled levels must be added from left to right 
    - root node has a depth of 0
  - heap 
    - each node in the tree contains a value greater than or equal to either of its two childeren
```
sort (A)
  buildHeap (A)
  for i = n-1 downto 1 do
    swap A[0] with A[i]
    heapify (A, 0, i)
end

buildHeap (A)
  for i = n/2-1 downto 0 do
    heapify (A, i, n)
end

# Recursively enforce that A[idx,max) is valid heap
heapify (A, idx, max)
  largest = idx 1
  left = 2*idx + 1
  right = 2*idx + 2

  if left < max and A[left] > A[idx] then
    largest = left 2
  if right < max and A[right] > A[largest] then
    largest = right 3
  if largest ≠ idx then
    swap A[idx] and A[largest]
    heapify (A, largest, max)
end
```
- always runs in O(n log(n))
- example 
  - [8, 11, 9, 2, 10, 16]
  - convert to heap 
                                                        16
                                                         |
                                                        / \
                                                      11   9
                                                      |    |
                                                     / \    \
                                                    2  10    8
- there are recursive and nonrecursive versions of heap sort 
  - nonrecursive is always faster, but recursive is easier to implement 

## Partition-Based Sorting 
- divide and conquer solves a problem by dividing it into two independent subproblems each about 1/2 the size of the original 
- 