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

### Python script for creating a custom iterator in a single class design (But which can only be used once)

```python
class MyIterator:
    def __init__(self, end):
        self.current = 0
        self.end = end

    def __iter__(self):
        return self

    def __next__(self):
        if self.current < self.end:
            value = self.current
            self.current += 1
            return value
        else:
            raise StopIteration

# Create an iterator object
my_iter = MyIterator(5)  # will produce numbers 0 to 4

# Manually loop through iterator
while True:
    try:
        num = next(my_iter)  # get next element
    except StopIteration:
        break  # stop when iterator is exhausted
    print(num)
print("Done!")

```

### Python script for creating a custom iterator in a single class design (Which can be used again because it has a `reset()` method)

```python
class MyIterator:
    def __init__(self, end):
        self.end = end
        self.current = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.current < self.end:
            value = self.current
            self.current += 1
            return value
        else:
            raise StopIteration

    def reset(self):
        """Reset iteration so it can start again."""
        self.current = 0

# --- Demo ---
my_iter = MyIterator(5)

# First iteration
print("First pass:")
for num in my_iter:
    print(num)

# Reset and reuse
my_iter.reset()

print("\nSecond pass (after reset):")
for num in my_iter:
    print(num)


```


#### Flow chart for the above script

```mermaid
flowchart LR
    A[Start] --> B["Create MyIterator\(end\)"]
    B --> C["Call iter\(my_iter\)"]
    C --> D["Return self (same object)"]
    D --> E["Use next() until StopIteration"]
    E --> F{Want to reuse?}
    F -- No --> G[End]
    F -- Yes --> H["Call reset\(\)"]
    H --> I["Set current = 0"]
    I --> C

```

#### Two class design

```python

class MyIterable:
    def __init__(self, end):
        self.end = end

    def __iter__(self):
        # Return a new iterator every time
        return MyIterator(self.end)

class MyIterator:
    def __init__(self, end):
        self.current = 0
        self.end = end

    def __next__(self):
        if self.current < self.end:
            value = self.current
            self.current += 1
            return value
        else:
            raise StopIteration

# --- Demo ---
my_obj = MyIterable(5)

print("First pass:")
for num in my_obj:
    print(num)

print("\nSecond pass (fresh iterator automatically):")
for num in my_obj:
    print(num)


```


