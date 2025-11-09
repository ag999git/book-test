
<img src="https://github.com/ag999git/images_figures/blob/master/Cover-Python-programming-by-Anurag-Gupta.jpeg" width="20%" alt="Image description">

### "Python Programming: Problem Solving, Packages and Libraries" authored by Anurag Gupta and G.P. Biswas
### You can get the book on Amazon [Here](https://amzn.in/d/92pgv9Y)

---

#### Example diagram for script for Composite design pattern 

```mermaid

flowchart TD
    A[Window: My Application] --> B[Label: 'Welcome to the App']
    A --> C[Button: OK]
    A --> D[Button: Cancel]

    classDef composite fill:#f9f,stroke:#333,stroke-width:2px;
    classDef leaf fill:#bbf,stroke:#333,stroke-width:2px;

    class A composite;
    class B,C,D leaf;


```

#### Explanation

* Label and Button are leaf components — they only know how to render themselves.

* Window is a composite component — it can contain and render multiple widgets.

* The pattern allows uniform treatment of simple and complex objects.
* Whether you render a Button, Label or an entire Window, the interface is the same: `component.render()`








