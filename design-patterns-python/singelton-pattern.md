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

### Python script which shows use of decorator function to implement the Singleton pattern

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


### Flowchart which shows how the decorator works

```mermaid

flowchart TD
    A[Start of Python Script] --> B["Python encounters the class definition: <br><b>class Logger:</b>"]
    B --> C["Python executes the class body to collect methods and attributes"]
    C --> D["Python calls <b>type()</b> internally to create the class object <br><b>Logger = type('Logger', ...)</b>"]
    D --> E["Now the class object <b>Logger</b> exists in memory (not instantiated yet)"]
    E --> F["Decorator syntax <b>@singleton</b> triggers a call: <br><b>singleton(Logger)</b>"]
    F --> G["Inside decorator: Python executes <b>singleton()</b> function"]
    G --> H["<b>singleton()</b> defines inner function <b>get_instance()</b> and returns it"]
    H --> I["Returned value replaces the class name: <br><b>Logger = get_instance</b>"]
    I --> J["At this point, no instance of Logger exists yet <br>(so __init__ has not run)"]
    J --> K["Later in code: <b>log1 = Logger()</b> is called"]
    K --> L["Since Logger now refers to <b>get_instance()</b>, <br>this calls <b>get_instance()</b> function"]
    L --> M["Inside get_instance(): check if Logger is in instances dict"]
    M --> N{"Is Logger already stored?"}
    N -- No --> O["Call the original class constructor: <br><b>cls(*args, **kwargs)</b>"]
    O --> P["This triggers <b>Logger.__init__()</b> → prints 'Logger initialized'"]
    P --> Q["Store instance in dictionary: <b>instances[Logger] = instance</b>"]
    N -- Yes --> R["Return the existing instance (skip __init__)"]
    Q --> S[End]
    R --> S[End]


```












