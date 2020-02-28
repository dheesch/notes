# What is Functional Programming

- Functional programming (FP) is based on a simple premise 
  - we construct our programs only using pure functions
- pure function - function with no side effects 
- side effect - function does something other than return a value 
  - modify a variable
  - setting a field on an object 
  - throwing an exception
  - printing to the console
  - read/write from file
  - drawing on screen 
- referential transparent - an expression e is referentially transparent if, for all programs p, all occurrences of e in p can be replaced by the result of evaluating e without affecting the meaning of p
  - a function is pure if the expression f(x) is referntially transparent for all referentially transparent x 
- referential transparency forces everything a function does to be represented by its return value 
- 

