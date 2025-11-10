
<img src="https://github.com/ag999git/images_figures/blob/master/Cover-Python-programming-by-Anurag-Gupta.jpeg" width="20%" alt="Image description">

### "Python Programming: Problem Solving, Packages and Libraries" authored by Anurag Gupta and G.P. Biswas
### You can get the book on Amazon [Here](https://amzn.in/d/92pgv9Y)

---

### Unit Test Flow chart


```mermaid

flowchart TD
    A["Write Python function, for example: add(a, b)"] --> B["Create Test Case Class using unittest.TestCase"]
    B --> C["Define Test Methods such as test_addition"]
    C --> D["Run tests with unittest.main()"]
    D --> E{"Do all tests pass?"}
    E -->|Yes| F["Display OK message"]
    E -->|No| G["Show failure message (AssertionError)"]
    G --> H["Fix the code or the test"]
    H --> D

```

### What ithe above flow chart shows

1.  You start with a Python function (e.g., `add`).
    
2.  Then you create a test case class using `unittest.TestCase`.
    
3.  Inside it, you define methods that start with `test_`.
    
4.  When you run the tests, Python checks all test cases.
    
5.  If everything passes → you see **“OK”** .
    
6.  If any test fails → you see an **AssertionError**  and can fix the issue.

---

