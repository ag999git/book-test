
<img src="https://github.com/ag999git/images_figures/blob/master/Cover-Python-programming-by-Anurag-Gupta.jpeg" width="20%" alt="Image description">

### "Python Programming: Problem Solving, Packages and Libraries" authored by Anurag Gupta and G.P. Biswas
### You can get the book on Amazon [Here](https://amzn.in/d/92pgv9Y)

---

#### Class diagram for observer design pattern

```mermaid

classDiagram
    %% Publisher (Subject)
    class Publisher {
        -subscribers : list
        +add_subscriber(subscriber)
        +notify_subscribers(message)
    }

    %% Subscriber (Observer)
    class Subscriber {
        -name : str
        +update(message)
    }

    %% Relationships
    Publisher "1" --> "*" Subscriber : notifies

```

### Explanation of the Diagram

1.  **Classes**:
    
    *   `Publisher` → maintains a list of subscribers and notifies them.
        
    *   `Subscriber` → receives updates via `update(message)`.
        
2.  **Attributes**:
    
    *   `subscribers` → list of all attached subscribers.
        
    *   `name` → unique identifier for each subscriber.
        
3.  **Methods**:
    
    *   `add_subscriber(subscriber)` → attach a subscriber.
        
    *   `notify_subscribers(message)` → send updates to all subscribers.
        
    *   `update(message)` → reaction of the subscriber.



#### Flowchart of the script in book

```mermaid

flowchart TD
    %% Publisher and Subscribers
    A[Publisher: news_publisher] -->|add_subscriber| B[Subscriber: Alice]
    A -->|add_subscriber| C[Subscriber: Bob]

    %% Notification Flow for first message
    D[Set message: Breaking News: New Python version released!] --> A
    A --> B
    A --> C

    %% Notification Flow for second message
    E[Set message: Update: Python release date confirmed!] --> A
    A --> B
    A --> C

    %% Subscriber reactions
    B --> F[Print: Alice received notification]
    C --> G[Print: Bob received notification]


```
        
4.  **Relationship**:
    
    *   Publisher **notifies multiple subscribers** (`1 → *` relationship).


