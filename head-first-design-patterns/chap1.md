# Chap 1 - Intro to Design Patterns: Welcome to Design Patterns 

- Someone has already solved your problem - exploit the wisdom and lessons learned by other developers 
- Design Principle - identify the aspects of your application that vary and separate them from what stays the same 
  - fewer unintended consequences from code changes and more flexibility in your systems 
  - take the parts that vary and encapsulate them, so that later you can alter or extend the parts that vary without affecting those that don't 
  - Ducks -> some ducks can fly other's can't - Mallards, Redhead, RUBBER are similar, but not the same 
    - solve with multiple classes 
      - Duck class - what stays the same for each 
      - DuckBehavior interface - what's different - quacking and flying 
        - each behavior will implement this interface 
      - Duck class can change behavior on the fly using mutators 
        - public void setFlyBehavior(FlyBehavior fb) { ... } 
  - Pay attention to relationships 
    - Is-A
    - Has-A
    - Implements 
- Design Principle - Composition over inheritance 

- Strategy Pattern - defines a family of algorithms, encapsulates each one, and makes them interchangeable
  - Strategy lets the algorithm vary independently from clients that use it 
 

