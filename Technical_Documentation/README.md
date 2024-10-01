# HBnB Project - UML Documentation

## Introduction

This document presents the Unified Modeling Language (UML) diagrams for the HBnB (Holberton Bed and Breakfast) project, a class assignment designed to demonstrate proficiency in software architecture and design principles.

## Purpose

The purpose of this documentation is to:
1. Showcase understanding of UML diagram types and their applications.
2. Illustrate the proposed architecture and design of the HBnB system.
3. Serve as a reference for implementing the project's code.

## Contents

This documentation includes:
1. A high-level package diagram depicting the layered architecture of HBnB.
2. A detailed class diagram of the Business Logic layer.
3. Sequence diagrams for key API operations.
4. Explanations of design choices and diagram elements.

## Project 1 Context

HBnB is a simplified Airbnb-like application developed as part of the Holberton curriculum. It aims to demonstrate skills in:
- Object-Oriented Programming (OOP)
- Software architecture design
- UML diagramming
- API design and implementation

Note: This is a theoretical design for educational purposes and may not reflect all real-world complexities of a production system.

## Summary

- [HBnB Project - UML Documentation](#hbnb-project---uml-documentation)
  - [Introduction](#introduction)
  - [Purpose](#purpose)
  - [Contents](#contents)
  - [Project 1 Context](#project-1-context)
  - [Summary](#summary)
  - [Glossary](#glossary)
  - [UML in Python OOP](#uml-in-python-oop)
    - [TL;DR on UML Diagrams and Their Relationships](#tldr-on-uml-diagrams-and-their-relationships)
  - [UML Class Diagram: The Pet Shop](#uml-class-diagram-the-pet-shop)
    - [Basic format](#basic-format)
    - [UML Class Relationships](#uml-class-relationships)
    - [Summary of Symbols:](#summary-of-symbols)
  - [UML Sequence Diagram: Ordering a Pizza](#uml-sequence-diagram-ordering-a-pizza)
    - [Basic format](#basic-format-1)
    - [UML Sequence Diagram Relationship Representations:](#uml-sequence-diagram-relationship-representations)
    - [Summary of Symbols for Sequence Diagrams:](#summary-of-symbols-for-sequence-diagrams)
  - [UML Package Diagram: E-Commerce Application](#uml-package-diagram-e-commerce-application)
    - [Basic format](#basic-format-2)
    - [UML Package Diagram Relationship Representations:](#uml-package-diagram-relationship-representations)
    - [Summary of Symbols for Package Diagrams:](#summary-of-symbols-for-package-diagrams)
  - [Conclusion](#conclusion)
  - [Author](#author)

## Glossary

**A**
- **API (Application Programming Interface)**: A set of protocols, routines, and tools for building software applications.
- **Aggregation**: A specialized form of association that represents a "whole-part" relationship where the "part" can exist independently of the "whole".
- **Association**: A relationship between two classes where one class uses or interacts with another.
- **Attribute**: A data member (variable) of a class.

**C**
- **Class**: In OOP, a blueprint for creating objects (a particular data structure), providing initial values for state (member variables or attributes), and implementations of behavior (member functions or methods).
- **Class Diagram**: A structural diagram that shows the system's classes, their attributes, methods, and the relationships among objects.
- **Composition**: A stronger form of aggregation where the "part" cannot exist without the "whole".

**D**
- **Dependency**: A relationship where a change in one element may affect another element.

**F**
- **Facade Pattern**: A design pattern that provides a simplified interface to a complex subsystem.

**I**
- **Inheritance**: A relationship where one class (subclass) is based on another class (superclass).

**L**
- **Lifeline**: In sequence diagrams, a vertical line that represents the existence of an object over time.

**M**
- **Message**: In sequence diagrams, a communication between objects.
- **Method**: A function that belongs to a class.

**O**
- **Object**: An instance of a class.
- **OOP (Object-Oriented Programming)**: A programming paradigm based on the concept of "objects", which can contain data and code.

**P**
- **Package**: A general-purpose mechanism for organizing elements into groups.
- **Package Diagram**: A structural diagram that depicts how a system is split up into logical groupings by showing the dependencies among these groupings.

**R**
- **Relationship**: A connection between classes or objects in UML diagrams.

**S**
- **Sequence Diagram**: A behavioral diagram that shows how objects interact in a particular scenario of a use case.

**U**
- **UML (Unified Modeling Language)**: A standardized visual modeling language used in software engineering to create blueprints of a system.

## UML in Python OOP

**Definition:** Unified Modeling Language (UML) is a standardized way to visualize the design of a system, especially for Object-Oriented Programming (OOP). It acts as a **blueprint** for you code, like architectural blueprints for buildings.

**Syntax:**

There is no direct syntax for UML since there are different types of UML structures. Here as the main three **Class Diagrams**, **Sequence Diagrams**, **Package Diagrams**.

### TL;DR on UML Diagrams and Their Relationships

**1. Class Diagrams**  
- **Purpose**: Show the static structure of a system's classes, their attributes, methods, and relationships.  
- **Key Relationships**:  
  - **Association (`--->`)**: Represents a connection between classes (e.g., a Book is associated with an Author).  
  - **Aggregation (`<>`)**: A "whole-part" relationship where the part can exist independently (e.g., Library has Books).  
  - **Composition (`*--`)**: A stronger whole-part relationship where parts cannot exist without the whole (e.g., a House has Rooms that can't exist without the House).  
  - **Generalization (`--|>`)**: Inheritance relationship (e.g., Dog is a subclass of Animal).  
  - **Dependency (`..>`)**: One class depends on another for functionality.

**2. Sequence Diagrams**  
- **Purpose**: Show how objects interact in a particular sequence of messages or actions over time.  
- **Key Relationships**:  
  - **Message (`-->`)**: Represents the flow of communication between objects (e.g., an Order object sends a confirmation message to a Customer).  
  - **Return (`<--`)**: Shows the return of a response to a sent message.  
  - **Self-call (`↺`)**: An object calls its own method during an interaction.  
  - **Create (`-->>`)**: Represents the instantiation of a new object during a sequence.

**3. Package Diagrams**  
- **Purpose**: Organize large systems into packages (or modules) and show the dependencies between them.  
- **Key Relationships**:  
  - **Dependency (`..>`)**: One package depends on another for its operation (e.g., PackageA depends on PackageB).  
  - **Association (`--->`)**: Packages interact or communicate with each other.  
  - **Generalization (`--|>`)**: Shows inheritance or hierarchical relationships between packages (e.g., PackageChild inherits from PackageParent).  
  - **Containment (`+--->`)**: One package contains another (e.g., PackageOuter contains PackageInner).  
  - **Import (`<|>`)**: Indicates that one package imports elements from another package.

These diagrams are fundamental to designing object-oriented systems, allowing developers to visualize class structures, interactions, and dependencies within and across systems.


## UML Class Diagram: The Pet Shop

**Definition**
A class diagram is a type of UML diagram that shows the structure of a system by displaying its classes, attributes, operations, and relationships between objects.

### Basic format

A class in UML is represented by a rectangle divided into three sections:
1. Top: Class name
2. Middle: Attributes (properties)
3. Bottom: Operations (methods)

*Example:*

```scss
+---------------+          +-------------+          +--------------+
|   PetShop     |<>------->|    Pet      |<>------->|   Owner      |
+---------------+          +-------------+          +--------------+
| - location    |          | - name      |          | - name       |
| - inventory   |          | - species   |          | - contactInfo|
+---------------+          | - age       |          +--------------+
| + addPet()    |          +-------------+          | + adoptPet() |
| + removePet() |          | + feed()    |          +--------------+
+---------------+          | + play()    | 
                           +-------------+

```

**Explanations, breakdown of the example:**

- **Class Names**: Animal, Dog, and Cat
- **Attributes**: 
  - Animal has name (String) and age (int)
  - Dog has breed (String)
  - Cat has furColor (String)
- **Operations**: 
  - Animal has makeSound() and eat()
  - Dog has fetch()
  - Cat has scratch()
- **Relationships**: The arrows pointing from Dog and Cat to Animal represent inheritance (Dog and Cat are subclasses of Animal)

**Mnemonics and Analogies:**

1. `CAM` - Remember the three parts of a class: `C`lass name, `A`ttributes, and `M`ethodes.

2. Think of the class diagram as a "pet shop catalog". Each box is like a page in the catalog describing a type of pet (class), its features (attributes), and what it can do (methods).

3. The inheritance arrows are like family trees - they show which "pet families" are related.

### UML Class Relationships

**Definition**
UML class diagrams depict the relationships between different classes in a system. These relationships are represented using various types of associations, which are indicated by different types of lines and arrows.

1. **Association (`--->`):**
   - **Description**: A basic connection between two classes where one class uses or interacts with the other.
   - **Example**: A `Customer` can place an `Order`.
   - **Symbol**: `--->`

   ```sql
   +-----------+     --->     +-----------+
   | Customer  |              |  Order    |
   +-----------+              +-----------+
   ```

2. **Bidirectional Association (`<--->`):**
   - **Description**: Both classes are aware of each other and can communicate back and forth.
   - **Example**: An `Employee` works in a `Department`, and the `Department` knows its `Employees`.
   - **Symbol**: `<--->`

   ```sql
   +------------+    <--->    +------------+
   |  Employee  |              | Department |
   +------------+              +------------+
   ```

3. **Aggregation (`<>--->`):**
   - **Description**: A "whole-part" relationship where the part can exist independently of the whole.
   - **Example**: A `Team` consists of `Players`, but players can exist without the team.
   - **Symbol**: `<>--->`

   ```sql
   +----------+    <>--->    +---------+
   |  Team    |              | Player  |
   +----------+              +---------+
   ```

4. **Composition (`*--->`):**
   - **Description**: A "whole-part" relationship where the part cannot exist without the whole. If the whole is destroyed, the part is destroyed too.
   - **Example**: A `House` consists of `Rooms`. If the house is destroyed, the rooms are also destroyed.
   - **Symbol**: `*--->`

   ```sql
   +----------+    *--->     +--------+
   |  House   |              |  Room  |
   +----------+              +--------+
   ```

5. **Generalization/Inheritence (`--|>`):**
   - **Description**: Represents an "is-a" relationship between a superclass and subclass (inheritance).
   - **Example**: A `Dog` is a type of `Animal`.
   - **Symbol**: `--|>`

   ```sql
   +--------+    --|>     +--------+
   |  Dog   |              | Animal |
   +--------+              +--------+
   ```

6. **Realization (`..|>`):**
   - **Description**: Represents the relationship between a class and an interface it implements.
   - **Example**: A `Button` class realizes the `Clickable` interface.
   - **Symbol**: `..|>`

   ```sql
   +---------+   ..|>     +------------+
   |  Button |            |  Clickable |
   +---------+            +------------+
   ```

7. **Dependency (`..-->`):**
   - **Description**: Represents that one class depends on another to perform a function (e.g., method parameters or local variables).
   - **Example**: A `Car` depends on an `Engine` to function.
   - **Symbol**: `..-->`

   ```sql
   +-------+   ..-->    +---------+
   |  Car  |            |  Engine |
   +-------+            +---------+
   ```

### Summary of Symbols:
- **Association**: `--->`
- **Bidirectional Association**: `<--->`
- **Aggregation**: `<>--->`
- **Composition**: `*--->`
- **Generalization (Inheritance)**: `--|>`
- **Realization**: `..|>`
- **Dependency**: `..-->`

## UML Sequence Diagram: Ordering a Pizza

**Definition**
A UML sequence diagram is a type of interaction diagram that shows how objects interact with each other over time. It depicts the messages (or method calls) exchanged between objects in the order they occur.

### Basic format

In a sequence diagram, you have:
1. **Lifelines** - Vertical lines representing the objects involved in the interaction.
2. **Messages** - Horizontal arrows between lifelines representing the flow of information or method calls.
3. **Time** - Time flows from top to bottom.

*Example:*

```sql
         Customer       Restaurant
           |               |
           |     placeOrder()
           |--------------->|
           |               |  processOrder()
           |<---------------| 
           |               |   prepareOrder()
           |<---------------|
           |     deliverOrder()
           |--------------->|
           |               |   receiveOrder()
           |<---------------|
```

**Explanations, breakdown of the example:**

1. The Customer and Restaurant are the two objects/lifelines involved in this interaction.
2. The Customer initiates the interaction by calling the `placeOrder()` method on the Restaurant.
3. The Restaurant processes the order, prepares it, and then delivers the order back to the Customer.
4. The Customer receives the order.

**Mnemonics and Analogies:**

1. The vertical lifelines can be seen as "timelines" for each object, showing how they interact over time.

### UML Sequence Diagram Relationship Representations:

1. **Synchronous Message (`---->`):**
   - **Description**: A message sent from one object to another where the sender waits for the receiver to finish processing the message before continuing. This is the most common type of message.
   - **Example**: A `Customer` sends a `placeOrder()` message to the `Order` object.
   - **Symbol**: `---->`

   ```sql
   +------------+      ---->      +------------+
   |  Customer  |                 |   Order    |
   +------------+                 +------------+
   ```

2. **Return Message (`<----`):**
   - **Description**: Represents the return of control from the receiver object to the sender object. This usually happens after processing a synchronous message.
   - **Example**: After processing `placeOrder()`, the `Order` object returns confirmation to the `Customer`.
   - **Symbol**: `<----`

   ```sql
   +------------+     <----      +------------+
   |  Customer  |                |   Order    |
   +------------+                +------------+
   ```

3. **Asynchronous Message (`---->>`):**
   - **Description**: A message sent from one object to another where the sender does not wait for the receiver to complete the operation before moving on. It typically represents events or signals.
   - **Example**: A `Sensor` sends a `signal()` to the `AlarmSystem` and continues its operation without waiting for a response.
   - **Symbol**: `---->>`

   ```sql
   +------------+     ---->>      +------------+
   |   Sensor   |                 | AlarmSystem|
   +------------+                 +------------+
   ```

4. **Self Message (`---->`) (on the same object):**
   - **Description**: A message an object sends to itself to invoke its own methods. Often used to represent recursion or internal operations.
   - **Example**: A `User` object sends an internal `authenticate()` message to itself.
   - **Symbol**: `---->` (looping back to the same object)

   ```sql
   +----------+
   |   User   |
   +----------+
        |
   ---->|
   authenticate()
   ```

5. **Activation Box**:  
   - **Description**: The vertical rectangle on an object’s lifeline that shows the duration of the object's method execution. Often used in synchronous messages.
   - **Example**: The `Server` object is active while handling a `request()` from the `Client`.
   - **Symbol**: A vertical bar on the lifeline during message handling.

   ```sql
   +----------+         +---------+
   |  Client  |         |  Server |
   +----------+         +---------+
       |                 |
       ----> request()   |
       |  [Activation]   |
       |                 |
   ```

6. **Lifeline (`|`)**:  
   - **Description**: Represents the existence of an object over time during the interaction. Messages are exchanged along the lifelines.
   - **Example**: `Client` and `Server` lifelines during their interaction.
   - **Symbol**: `|`

   ```sql
   +----------+         +---------+
   |  Client  |         |  Server |
   +----------+         +---------+
        |                 |
   ```

7. **Destruction (`X`)**:
   - **Description**: Represents the termination of an object’s existence after it finishes executing a certain method. It usually appears as a cross (X) at the bottom of the object's lifeline.
   - **Example**: The `Session` object is destroyed after completing a task.
   - **Symbol**: `X`

   ```sql
   +----------+
   | Session  |
   +----------+
        |
        X
   ```

### Summary of Symbols for Sequence Diagrams:
- **Synchronous Message**: `---->`
- **Return Message**: `<----`
- **Asynchronous Message**: `---->>`
- **Self Message**: `---->` (looping to the same object)
- **Activation Box**: Vertical bar on the lifeline during method execution.
- **Lifeline**: Vertical line representing an object’s existence.
- **Destruction**: `X` at the end of an object's lifeline.

## UML Package Diagram: E-Commerce Application

**Definition**
A UML package diagram is a type of structural diagram that shows the organization and dependencies between packages (modules or subsystems) within a system. Packages are used to group related classes, interfaces, and other elements together.

### Basic format

In a package diagram, you have:
1. **Packages** - Represented by rectangles with a tab at the top.
2. **Dependencies** - Represented by dashed arrows between packages, indicating that one package depends on another.

*Example:*

```sql
+--------------------+
|   E-Commerce App   |
+--------------------+
|     +-------+      |
|     |Orders |      |
|     +-------+      |
|     +-------+      |
|     |Payments      |
|     +-------+      |
|     +-------+      |
|     |Shipping|     |
|     +-------+      |
+--------------------+
        |
        |
        v
+--------------------+
|      Database      |
+--------------------+
```

**Explanations, breakdown of the example:**

1. The main **package** is the **"E-Commerce App"**, which contains three sub-packages: *Orders*, *Payments*, and *Shipping*.
2. The sub-packages depend on the "Database" package, as indicated by the dashed arrows. This means that the functionality of the sub-packages relies on the data stored in the database.

**Mnemonics and Analogies:**

1. Think of the package diagram as a "building blueprint" - the **main package** is the **overall building**, and the **sub-packages** are the different **rooms** or **floors** within the building.

2. Imagine a **grocery store**. The **main package** would be the **grocery store**, and the **sub-packages** could be the **different departments** like **Produce**, **Dairy**, and **Bakery**. The departments depend on the central inventory (database) to function.

### UML Package Diagram Relationship Representations:

1. **Dependency (`..>`)**:
   - **Description**: Represents a dependency relationship between two packages, meaning one package depends on another to function. It shows that changes in the target package may impact the dependent package.
   - **Example**: `PackageA` depends on `PackageB` for certain functionalities.
   - **Symbol**: `..>`

   ```sql
   +-----------+     ..>     +-----------+
   | PackageA  |             | PackageB  |
   +-----------+             +-----------+
   ```

2. **Association (`--->`)**:
   - **Description**: Represents an association between two packages. It shows that one package uses or communicates with another.
   - **Example**: `PackageX` is associated with `PackageY`.
   - **Symbol**: `--->`

   ```sql
   +-----------+     --->     +-----------+
   | PackageX  |              | PackageY  |
   +-----------+              +-----------+
   ```

3. **Generalization (`--|>`)**:
   - **Description**: Represents an inheritance relationship between two packages. The child package inherits from the parent package.
   - **Example**: `PackageChild` inherits functionalities from `PackageParent`.
   - **Symbol**: `--|>`

   ```sql
   +--------------+    --|>     +---------------+
   | PackageChild |             | PackageParent |
   +--------------+             +---------------+
   ```

4. **Realization (`..|>`)**:
   - **Description**: Represents the implementation of an interface by a package. The package realizes the operations declared by the interface package.
   - **Example**: `ConcretePackage` implements the `InterfacePackage`.
   - **Symbol**: `..|>`

   ```sql
   +-------------------+    ..|>    +-------------------+
   | ConcretePackage   |            | InterfacePackage  |
   +-------------------+            +-------------------+
   ```

5. **Containment (`+--->`)**:
   - **Description**: Represents a containment relationship, where one package contains another package inside it. This is often used to depict a package hierarchy.
   - **Example**: `PackageOuter` contains `PackageInner`.
   - **Symbol**: `+--->`

   ```sql
   +----------------+     +--->     +----------------+
   | PackageOuter   |                | PackageInner   |
   +----------------+                +----------------+
   ```

6. **Merge (`<>--->`)**:
   - **Description**: Represents a merge relationship between two packages, where elements of one package are merged into another package, forming a combined package.
   - **Example**: `PackageA` merges into `PackageB`.
   - **Symbol**: `<>--->`

   ```sql
   +-----------+   <>--->    +-----------+
   | PackageA  |             | PackageB  |
   +-----------+             +-----------+
   ```

7. **Import (`<|>`)**:
   - **Description**: Represents an import relationship where one package imports elements from another package. This is similar to a dependency but with more emphasis on reusable components.
   - **Example**: `PackageA` imports elements from `PackageB`.
   - **Symbol**: `<|>`

   ```sql
   +-----------+    <|>     +-----------+
   | PackageA  |             | PackageB  |
   +-----------+             +-----------+
   ```

### Summary of Symbols for Package Diagrams:
- **Dependency**: `..>`
- **Association**: `--->`
- **Generalization**: `--|>`
- **Realization**: `..|>`
- **Containment**: `+--->`
- **Merge**: `<>--->`
- **Import**: `<|>`

## Conclusion

This whole course aimed to be a - kind of - concise course about the three types of UML diagrams necessary to do the project HBNB. It only aimed to be educational for myself


## Author

Anne-Cécile Besse (Arc)