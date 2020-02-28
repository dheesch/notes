# Getting started with functional programming in Scala

- higher-order functions -functions that take other functions as arguments and may return functions as their output 

## Scala code 
- object - object keyword creates a new singleton type 
  - will only ever have one instance 
- scala doesn't have a static keyword 
  - objects are often used when you might need static members 
- main is declared as 
```scala
  def main(args: Array[String]): Unit = {
    println(formatAbs(-42))
  }
```
- main - must include the args argument 
- Unit - is the scala equivalent of void
- Everything is an object even primitives like Int
- import objects as namespace.class
  - import scala.collection.mutable.Stack

## Writing loops functionally
```scala
def factorial(n: Int): Int = {
  def go(n: Int, acc: Int): Int = {
    if (n <= 0) acc
    else go(n-1, n*acc
  }
}
```
- functional loops use recursion to prevent mutating a loop variable 
- recursive loops generally use a helper function 
- functions can be defined in any block in scala


## Tail calls in Scala 
- tail position - a call to a function that does nothing other than return the vlaue of the recursive call
- if all recursive calls made by a function are in tail position, scala will compile the recursion to iterative loops 
  - won't consume call stack frames for each iteration 
- 

## Writing our first higher-order function 
- higher-order function - higher-order function take functions as arguments 
- 
