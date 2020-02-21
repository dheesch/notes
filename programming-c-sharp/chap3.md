# Types

## Classes
- simple class 
  ```C#
  public class Counter
  {
      private int _count;

      public int GetNextValue()
      {
          _count += 1;
          return _count;
      }
  }
  ```
- public and internal classes
  - public classes - what you'd imagine - they are free to use 
  - internal classes - available for use only within the component that defines it 
    - so you can have classes internal to your library for your use, but not the users of the lib
- class fields default to private 
- naming conventions 
  - first letter of a class name is capitalized 
    - camelcase after that 
    - underscores not allowed 
  - methods and properties are also PascalCased
  - method parameters use camelCase
- static members - not bound to an instance of the class 
  ```C# 
  private int _count; //unique to the instance of the class
  private static int _totalCount; //shared between instances of classes 
  ```
- this - you'll need to use this when there might be name collisions 
  - static methods don't use this 
- static classes - put static before class - public static class TestClass { ... }
  - compiler will give an error if you try and instantiate 
- if you're going to be using a static class a lot you can use them without explicit qualification by doing using static StaticClass;
  ```C#
  using static System.Console;
  using static System.Math;

  class Program
  {
      static void Main(string[] args)
      {
          WriteLine(Sin(PI / 4));
      }
  }
  ```
- all classes are a reference type 
  - an in