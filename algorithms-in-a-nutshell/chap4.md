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
  largest = idx
  left = 2*idx + 1
  right = 2*idx + 2

  if left < max and A[left] > A[idx] then
    largest = left 
  if right < max and A[right] > A[largest] then
    largest = right
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
- find the median element in the collection and swap it with the middle element of A 
- swap elements in the left half that are greater than A[mid] w/ elements in the right half that are less than or equal to A[mid]
  - this subdivides the original array into two distinct subarrays that can be recusively sorted in place to sort the original collection A

### Quicksort 
- introduced by C.A.R Hoare in 1960 
- selects an element in the collection to partition an array into two subarrays 
  - sometimes randomly, sometimes the leftmost, sometimes the middle one 
- averages O(n log n)
- worst case - )(n^2)

```
sort(A)
  quicksort(A, 0, n-1)

quicksort(A, left, right)
  if left < right then
    pivot  = partition(A, left, right)
    quicksort(A, left, pivot - 1)
    quicksort(A, pivot + 1, right)
```
- quicksort often defaults to insertion sort when the size of the subarray to be sorted falls below a certain size
- using a random element as pivot enables Quicksort to provide average-case performance that usually outperforms other sorting algos 
- the sorting method of choice on most systems 
- can be optimized 
  - using a stack to store subtasks to be processed - eliminates recursion
  - choose the pivot based on median-of-three strategy 
  - set minimum particition size to use insertion instead 
    - in JDK 1.8 that was set to 7
  - minimize the total size of the recursive stack by solving the smaller subproblem first 
  - none of the optimizations will elminate the O(n^2) worst case scenario 
- the only way to get O(n log n) is by using a partition function that can guarantee it finds a reasonable approximation to the actual median of the set 

### Bucket Sort 
- bucket sort constructs a set of n ordered buckets into which the elements of the input are partitioned 
- if hash function can uniformly partition the input set of n elements into n buckets, bucket sort can sort in O(n) time 
- use bucket sort when these two properties hold 
  - uniform distribution - the input data must be uniformly distributed for a given range 
    - based on this distribution, n buckets are created to evenly partition the input range 
  - ordered hash function 
    - the buckets are ordered if i < j elements inserted into bucket b[i] are lexicographically smaller than elements in bucket b[j]
```
sort (A)
  create n buckets B
  for i = 0 to n-1 do 1
    k = hash(A[i])
    add A[i] to the k-th bucket B[k]
  extract (B, A) 2
end

extract (B, A)
  idx = 0
  for i = 0 to n-1 do
    insertionSort (B[i]) 3
    foreach element e in B[i] 4
      A[idx++] = e
end
```
- too few buckets will lead to O(n^2) performance 
  - insertion sort is used to sort buckets 

## Sorting with Extra Storage 
- Most sorting algorithms sort a collection in place without requiring any noticeable extra storage 
### Merge Sort 
- worst case O(n log n) while using O(n) extra storage 
- can be used to efficiently sort data stored externally in a file 
- divide collection into two even smaller collections, each of which is then sorted 
- the two collections are then merged back into a single collection 
```
sort (A)
  if A has less than 2 elements then
    return A
  else if A has 2 elements then
    swap elements of A if out of order
    return A

  sub1 = sort(left half of A)
  sub2 = sort(right half of A)

  merge sub1 and sub2 into new array B
  return B
end
```

