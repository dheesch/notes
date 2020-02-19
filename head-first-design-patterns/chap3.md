# The Decorator Pattern: Decorating Objects 

- Design Principle - Classes should be open for extension, but closed for modification 
  - apply this to areas that are most likely to change, not an absolute rule since it will add some complexity 
- inheritance is one form of extension, but not necessarily the best way to achieve flexibility in our designs 
- in designs we should allow behavior to be extended without the need to modify existing code 
- composition and delegation can often be used to add new behaviors at runtime 
- decorator pattern provides an alternative to subclassing for extending behavior 
- the decorator pattern involves a set of decorator classes that are used to wrap concrete components
- decorator classes mirror the type of the component they decorate 
- decorators change the behavior of their components by adding new functionality befor and/or after method calls to the component 
- you can wrap a component with any number of decorators 
- decorators are typically transparent to the client of the component, unless the client is relying on the component's concrete type 
- decorators can result in many small objects in our design, and overuse can be complex 


