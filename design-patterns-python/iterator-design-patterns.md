### Implementation of the iterator protocol

```mermaid
flowchart TD
    A["Start"] --> B["Take a Python object my_obj"]
    B --> C["Pass my_obj to built-in function iter(my_obj)"]
    C --> D["Python checks if my_obj supports the Iterator Protocol"]
    D --> E{"Is my_obj iterable?"}
    E -- No --> F["Raise TypeError"]
    E -- Yes --> G["Return an iterator object"]
    G --> H["my_obj is iterable if it implements __iter__() and __next__()"]
    F --> I["End"]
    H --> I

```

### Custom iterators can be created in 2 different ways
1. Where there is a single class acting as both iterable and iterator
2. Where there are 2 distinct classes (a) For iterable (b) for iterator

```mermaid
flowchart TD

A["Custom Iterator"]:::root

A --> B1["Single Class Design"]:::single
B1 --> B1a["Acts as Iterable (has __iter__() returning self)"]:::detail
B1 --> B1b["Acts as Iterator (has __next__())"]:::detail

A --> B2["Two-Class Design"]:::double
B2 --> B2a["Iterable Class (defines __iter__() returning new Iterator instance)"]:::detail
B2 --> B2b["Iterator Class (defines __next__() for iteration logic)"]:::detail

classDef root fill:#ffecb3,stroke:#b57f00,stroke-width:2px;
classDef single fill:#c8e6c9,stroke:#2e7d32,stroke-width:2px;
classDef double fill:#bbdefb,stroke:#1565c0,stroke-width:2px;
classDef detail fill:#f0f0f0,stroke:#555,stroke-width:1px;

```

