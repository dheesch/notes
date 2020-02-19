# Chap 2: The Observer Patten: Keeping your objects in the know 

## Observer Pattern 
- if you understand newspaper subscriptions you understand the observer pattern 
- Subject - the publisher 
- Observers - the subscribers 
- observer defines a one-to-many dependency b/w objects so when one object changes state, all of its dependents are notified and updated automatically 
- Subject Class 
  - registerObserver()
  - removeObserver()
  - notifyObservers()
  - can also have a getState() and setState() 
- Observer Class 
  - update()
  - other specific methods 
- Subject contains the state and controls it so there is one Subject w/ state 
- Since the subject is the sole owner of that data, observers are dependent on the subject to update them when data changes 
  - leads to cleaner OO design than allowing many objects to control the same data 


## The Power of Loose Coupling 
- Two objects loosely copled can interact, but have little knowledge of each other 
- Observer provides an object design where subjects and observers are loosely coupled 
- the only thing the subject knows about an observer is that it implements a certain interface 
- don't have to modify the subject to add new types of observers 
- we can reuse subjects or observers independently of each other 
- changes to either the subject or an observer will not affect the other 

## Summary
- Observer Pattern - defines a one-to-many relationship between objects 
- Subject - also known as Observables, update Observers using a common interface
- Observers - loosely coupled in that the Observable knows nothing about them, other than they implement an interface 
- you can pull data from the observable when using the pattern 
- GUI frameworks make heavy use of Observer 

