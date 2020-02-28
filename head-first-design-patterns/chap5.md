# Chap 5. The Singleton Pattern: One of a Kind Objects 

- singleton - one instance of a class 
  - not as straightforward as you'd expect
  - remember static 
```
public class Singleton {
  private static Singleton uniqueInstance;

  //private constructor so no one can instantiate this class 
  private Singleton () {}

  //lets us instantiate and return an instance of it 
  public static Singleton getInstance() {
    if (uniqueInstance == null) {
      uniqueInstance = new Singleton();
    }
    return uniqueInstance 
  }

  //other useful methods 
}
```
- the singleton pattern ensures a class has only one instance, and provides a global point of access to it 
- if running in a thread application you will have to do some additional work 
  - if using java make getInstance a synchronized method 
    - every thread will wait its turn before it can enter the method 
    - synchronization is expensive 
- can we improve multithreading 
  - do nothing if the performance of getInstance() isn't critical 
    - synchronizing is straightforward and effective 
    - if it is performance critical you'll need to do something else
  - move to an eagerly created instance than a lazily created one 
    - private static Singleton uniqueInstance = new Singleton();
    - creates a unique instance when class is loaded before any thread accesses that variable 
  - use double checked locking to reduce the use of synchronization in getInstance()
  ```
  // won't work in Java 5 or earlier 
  public static Singleton getInstance() {
    if(uniqueInstance == null) {
      //only synchronized the first time through 
      synchronized (Singleton.class) {
        if(uniqueInstance == null) {
          uniqueInstance = new Singleton()
        }
      }
    }

    return uniqueInstance 
  }
  ```
  ### Analysis 
  - implementing singletons correctly can be tricky, but you should use them whenever you need to control the number of instances you are creating 
  - if your class is self-contained and doesn't depend on complex initialization you can make a class where all methods and variables are static 
  - two class loaders can each end up with their own instance of a singleton - be careful 
  - singletons are not globals 
    - global variable can provide global access, but can't enforce there is only one instance 
    - global variables tend to pollute the namespace 
