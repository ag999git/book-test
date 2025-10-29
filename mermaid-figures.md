```mermaid
graph TD;
    A-->B;
    A-->C;
    B-->D;
    C-->D;
```

Creational design pattern

```mermaid
mindmap
  root((Creational Design Patterns))
    Singleton
      : Ensure only one instance of a class exists.
    Factory
      : Create objects without specifying exact class.
    Abstract Factory
      : Create families of related objects.
    Builder
      : Construct complex objects step by step.
    Prototype
      : Clone existing objects instead of creating new ones.
```

Structural Design Patterns (Class & Object Composition)


```mermaid
mindmap
  root((Structural Design Patterns))
    Adapter
      : Converts one interface into another.
    Bridge
      : Decouples abstraction from implementation.
    Composite
      : Treat individual and composite objects uniformly.
    Decorator
      : Dynamically add behavior to objects.
    Facade
      : Provides a simplified interface to a subsystem.
    Flyweight
      : Shares objects to support large numbers efficiently.
    Proxy
      : Controls access to another object.


```

Behavioral Design Patterns (Object Interaction)


```mermaid
mindmap
  root((Behavioral Design Patterns))
    Chain of Responsibility
      : Passes requests along a chain of handlers.
    Command
      : Encapsulates a request as an object.
    Iterator
      : Sequentially access elements in a collection.
    Mediator
      : Simplifies communication between classes.
    Memento
      : Captures and restores object’s internal state.
    Observer
      : Notifies dependents of state changes.
    State
      : Changes behavior when internal state changes.
    Strategy
      : Selects algorithm behavior at runtime.
    Template Method
      : Defines algorithm skeleton, lets subclasses override steps.
    Visitor
      : Separates algorithms from object structure.


```

Separation of Concerns Hierarchy in Python

```mermaid
graph TD
    A[Function Level] --> B[Class Level]
    B --> C[Module Level]
    C --> D[Package Level]
    D --> E[Layer Level]
    E --> F[System Level]

    subgraph "Separation of Concerns Hierarchy in Python"
        A
        B
        C
        D
        E
        F
    end

    A:::level1
    B:::level2
    C:::level3
    D:::level4
    E:::level5
    F:::level6

    classDef level1 fill:#E3F2FD,stroke:#1E88E5,stroke-width:2px;
    classDef level2 fill:#E8F5E9,stroke:#43A047,stroke-width:2px;
    classDef level3 fill:#FFF3E0,stroke:#FB8C00,stroke-width:2px;
    classDef level4 fill:#F3E5F5,stroke:#8E24AA,stroke-width:2px;
    classDef level5 fill:#FBE9E7,stroke:#E53935,stroke-width:2px;
    classDef level6 fill:#ECEFF1,stroke:#37474F,stroke-width:2px;


```

Creational Design Patterns

```mermaid
mindmap
  root((Creational Design Patterns))
    description(Deals with object creation mechanisms)
    Factory Method
      note(Lets subclasses decide which class to instantiate)
    Abstract Factory
      note(Creates families of related objects)
    Builder
      note(Constructs complex objects step by step)
    Prototype
      note(Creates new objects by cloning existing ones)
    Singleton
      note(Ensures only one instance of a class)
    Object Pool
      note(Reuses limited resources instead of recreating)


```


```mermaid


```


```mermaid


```


```mermaid


```
