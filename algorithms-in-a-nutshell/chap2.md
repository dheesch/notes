# The Mathematics of Algorithms

## Size of a Problem Instance 
- an instance of a problem is a particular input data set given to a program 
- in most problems, the execution time of a program increases with the size of this data set
  - at the same time, overly compact representations (possibly using compression) may unnecessarily slow down the execution
- measuring the size of an instance if off only by a multiplicative constant 
  - sorting 64-bit ints will take longer than 32-bit ints 
- asymptotically equivalent - basically an algorithm will more or less be equivalent depending on input 
  - an algorithm for 32-bit integers will behave similarly with 64-bit integers 
- rate of growth of functions 
  - rate of growth of execution time describes the behavior of an algorithm as a function of the size of the input problem instance 
  - rate of growth detemines how it will perform on increasingly larger problem instances 
  - remember that 
     - constants matter 
     - size of n is not always large 

## Analysis in the Best, Average, and Worst Cases
- worst case - as the name implies 
  - generally used to describe properties of the input that prevent an algorithm from running efficiently
- average case - expected behavior when executing the algorithm on random problem instances 
  - some instances will require greater time, the vast majority will not 
- best case - as the name implies - rarely occurs in reality 
- lower bound - best case scenario 
- upper bound - worst case scenario 
- Big O in decreasing efficiency
  - Constant: O(1) - duh
  - Logarithmic: O(log n) - very efficient 
  - Sublinear: O(n^d) for d < 1 
  - Linear: O(n)
  - Linearithmic: O(n log n) - common behavior in efficient algorithms 
  - Quadratic: O(n^2)
  - Exponential: O(2^n)

