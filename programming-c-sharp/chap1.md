# Introducing C#

## Features 
- CLR - common language runtime - think JVM
- managed code - compiler compiles to an intermediate language 
- favors general-purpose language features over specialized ones 

## C# Standards and Implementations 
- Many .NETS - .NET Framework, Mono, .NET Core 
- .NET Framework - OG - only for windows 
- Mono - Open source version originally not backed by Microsoft 
  - Got rolled into Xamarin which MS purchased in 2016
- .NET Core - Cross platform open source version of .NET backed by MS
- .NET Standard - targets multiple versions 
  - .NET Standard 1.0 will run on 
    - .NET Framework 4.5+
    - .NET Core 1.0+
    - Mono 4.6+

## Visual Studio
- VS Code - text editor
- Visual Studio - IDE 
- Project - builds a single output, or target 
  - a .exe or a library or even a website
- automated tests are generally put in a separate project
- Solutions can hold multiple projects
- Projects can belong to multiple solutions, but a project must be part of a solution for VS to open that project 
- To reference a project in another project you can add that project as a dependency in the reference manager 

## Namespaces 
- Collections of classes 
- System namespace contains the core libraries 
  - System isn't a reserved keyword you can add classes to this if you want, but generally bad practice unless you're contributing to the core library  
- Microsoft namespace contains ms provided libraries 
- provide uniqueness multiple namespaces can have a class with the same name 
  - System.IO.Path and System.Windows.Shapes.Path 
  - resolve ambiguities with aliases 
    using IoPath = System.IO.Path;
    using WpfPath = System.Windows.Shapes.Path
- you can nest namespaces 
  namespace App {
    
    namespace Storage { ...
- you can also nest namespaces with a single declaration 
  namespace App.Storage { ... }
- nested namespaces can reference classes in its namespace and its parent namespaces without qualification 

## Program Entry Point
- Main - must be static 

## Annotations 
- annotations don't do anything but are useful for documentation purpose 
  [TestClass]
  public class WhenProgramRuns { ... 
- you can annotate classes and methods - you'll know when to use them 



