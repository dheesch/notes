# Basic Coding in C#

- statically typed, but does support implicit variables with var 
  ```C#
  String test = "test test"
  var test = "test test"
  ```
- var variables are still statically typed so don't fool yourself into thinking you can write JS in this 
  ```C#
    var test = "test";
    test = 42 // not gonna work bro 
  ```
- you can be lazy and write var, but I'd still write out the type 
- scope works the way you'd expect 
  - variables are only in scope to the end of their block 
  - if you declare a variable in a nested block, its not accessible outside of that block 
    ```C#
    int someValue = GetValue();
    
    if  (someValue > 100)
    {
      int willNotWork = someValue - 100;
    }
    Console.WriteLine(willNotWork); 
    ```
  - I wouldn't do this out of a matter of style
- Why you would try and do this in the first place, but C# will throw an error 
  ```C#
  int someValue = GetValue(); 
  
  if (someValue > 100) 
  {     
    int anotherValue = someValue - 100;  // Compiler error     
    Console.WriteLine(anotherValue); 
  }  

  int anotherValue = 123;
  ```

- nothing particularly interesting here - it behaves as you'd expect 

## Preporcessing Directives 
- #define - lets you define a compilation symbol 
  - generally used with #if to do something for certain things like a debug build or something 
- it's more common to define compilation symbols in the compiler build settins
- example 
  ```C#
  #if DEBUG     
    Console.WriteLine("Starting work"); 
  #endif     
  DoWork(); 
  #if DEBUG     
    Console.WriteLine("Finished work"); 
  #endif 
  ```
- you can also use conditional methods 
  ```C#
  [System.Diagnostics.Conditional("DEBUG")]
  static void ShowDebugInfo(object o) 
  {
    Console.WriteLine(o);
  }
  ```
- conditional method calls will be omitted in builds without the relevant symbol 
- .NET class library's Debug and Trace usie conditional methods 
  - be careful with this since if you rely on calls to those methods they will not be present in every build 
- #error and #warning - can be used to throw compiler warnings and errors
  #if NETSTANDARD
    #error .NET Standard is not a supported target for this source file 
  #endif 
- #line - tells the compiler the line and optionally the file the error occured 
  ```C#
  #line 123 "Foo.cs"
  intt x; // deliberate mistake 
  ```

  - mostly useful for generated code 
- #pragma - can be used to disabel selected compiler warnings and override checksum values 
  - primarily for code generation scenarios 
  - can be useful to disable warnings if you want 
- #nullable - allows control of the nullable annotation context 
  - only in C# 8.0
- #region and #endregion - they do nothing 
  - compiler only verifies there is a matching #endregion 
  - can be nested 
  - used for text editors for expand and collapse 

## Fundamental Data Types 

### Integer Types 
- byte to long 
- byte - 8 bits 
- sbyte - signed 8 bits 
- short - 16 bits 
- ushort - unsigned 16 bits 
- int - 32 bits 
- uint - unsigned 32 bits 
- long - 64 bits 
- ulong - 64 bits 

### Floating-point Types 
- Float - 32 bits 
- double - 64 bits 
- decimal - 128 bits - different from normal floats provides well-defined level of decimal precision 
  - the general solution is to store floats you need precision for as a collection of integers 
    - which is what it does 
    - sign bit 
    - 96 bit integer for the value 
    - 29 bit integer for the decimal 
      - really only accurate to 28 bits 
    - 96 + 129 + 1 = 128
  - arithmetic is significantly slower with decimal 
    - 128 bits is tricky for most cpus 
- if you're dealing with big numbers you can add underscores in the literal to break things up like a comma and they'll be ignored by the compiler 
   - 1_000_000_000
- you can also write binary literals as 0b_0010_1010

### Numeric Conversions 
- implicit conversions - operations on ints and floats/doubles will convert the int to a double 
- C# will never convert a floating-point number to an integer 
- explicit conversions - use a cast 
    ```C# 
    int i2 = (int) 42.0;
    ```
### Checked Contexts 
- checked keyword can be put in front of either a block or an expression making it a checked context 
- all artihmetic operations, including casts, will be checked for range overflow at runtime 
- will throw a System.OverflowException if there's an error 
- checked blocks only affect lines of code inside the block 
  -if there are method calls they will not be checked 
- there's also an unchecked context 
- you can set the compiler to make sure everything is checked

### BigInteger 
- not a basic type, but can be used like basic type 
- there are no theoretical limits on it ranges 

### Bools 
- bool - true or false - C# will not let you use integers it has to be the keywords true or false 

### Strings and Characters
- strings - use double quotes - sequence of chars 
- char - 16-bit value representinga UTF-16 code unit 
- Strings are immutable 
-StringBuilder - not a basic type, but will behave similar to a string - use it if you need mutability 
- C# supports interpolation similar to js - $"{name} is {ages} old";

### Verbatim String Literals 
- You can use @ for verbatim string literals so characters don't get escaped 
  - @"Hello ""World""" - yields Hello "World" - use double quotes in a row for quotes 
  - @C:\Windows\System32 - comes out as expected and not C:indowsystem32
    - you would have had to write "C:\\Windows\\System32" without the @ sign 
- verbatim string literals can also span multiple lines 
- beware of CRLF and LF 
  - C# can handle either 
  - git will convert crlf to lf 
  - but multiline literals might behave differently in windows than mac/linux
  - .gitattributes will let you define the behavior you want  

### Tuples 
- think C structs
- how to use 
  ```C#
  (int X, int Y) point = (10, 5);
  Console.WriteLine($"X: {point.X, Y: {point.Y}");
  ```
- you can also initialize tuples with implicit variables 
  ```C#
  var point = (X: 10, Y: 5);
  Console.WriteLine($"X: {point.X, Y: {point.Y}");
  ``` 


