# The Factory Pattern: Baking with OO Goodness 

- when you instantiate a class you are programming to an implementation not an interface
  - nothing wrong with this, but things CHANGE 
- if code is written to an interface, it will work with any new classes implementing that interface 
- Factories handle the details of object creation 
  - encapsulating object cration in one class, you only have one place to change implementation 

## The Dependency Inversion Principle
- reducing dependencies to concrete classes in our code is a good thing
- Design Principle - depend upon sabstractions do not depend upon concrete classes 
- 

## A few guidelines 
- no variable should hold a reference to a concrete class 
- no class should derive from a concrete class
- no method should override an implemented method of any of its base classes 
  - if you override an implemented method, then your base class wasn't really an abstraction to start with 
- just guidelines - these get violated in just about every program 

## Abstract Factory Pattern 
- Abstract Factory Pattern - provides an interface for creating families of related or dependent objects without specifying their concrete classes 
  - abstract interface for creating related factories 
    - PizzaIngredientFactory - implemented by NYPizzaIngredientFactory and ChicagoPizzaIngredientFactory 

## Summary 
- all factories encapsulate object creation 
- simple factory, not a design pattern, but is a simple way to decouple clients from concrete classes
- factory method - relies on inheritance object creation is delegated to subclasses 
- abstract factory relies on object composition: object creation is implemented in methods exposed in the factory interface 
- all factory patterns promote loos coupling by reducing the dependency of your application on concrete classes 
- the intent of factory method is to allow a class to defer instantiation to its subclasses 
- the intent of abstract factories is to create families of related objects without having to depend on their concrete classes
- dependency inversion principle - avoid dependencies on concrete types and strive for abstractions 
- factories are powerful for coding to abstractions, not concrete classes 
 
