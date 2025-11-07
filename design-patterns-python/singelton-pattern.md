###Singleton Pattern

#### Creating Singleton class using decorator

```python

def singleton(cls):
    instances = {}
    def get_instance(*args, **kwargs):
        if cls not in instances:
            instances[cls] = cls(*args, **kwargs)
        return instances[cls]
    return get_instance

@singleton
class Logger:
    def __init__(self):
        print("Logger initialized")

# Test
log1 = Logger()
log2 = Logger()
print("Are log1 and log2 same instance?->", log1 is log2) # True


```

### Flowchart for above code

```mermaid

flowchart TD
    A[Start] --> B["Define class Logger"]
    B --> C["@singleton applies → calls singleton(Logger)"]
    C --> D["singleton() creates empty dict: instances = {}"]
    D --> E["singleton() returns inner function get_instance()"]
    E --> F["Logger name now refers to get_instance"]
    F --> G["Call Logger() → actually calls get_instance()"]
    G --> H{"Is Logger in instances?"}
    H -- No --> I["Create new Logger instance: cls(*args, **kwargs)"]
    I --> J["Store in instances[Logger] = instance"]
    J --> K["Return stored instance"]
    H -- Yes --> L["Return existing instance from instances"]
    K --> M[End]
    L --> M[End]

```










