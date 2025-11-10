
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

### What the above flow chart shows

1.  You start with a Python function (e.g., `add`).
    
2.  Then you create a test case class using `unittest.TestCase`.
    
3.  Inside it, you define methods that start with `test_`.
    
4.  When you run the tests, Python checks all test cases.
    
5.  If everything passes → you see **“OK”** .
    
6.  If any test fails → you see an **AssertionError**  and can fix the issue.

---

### Diagram explaining `unittest.TestCase`


```mermaid

graph TD
    A[Your Test File: test_example.py] --> B[unittest Framework]
    B --> C[Discovers classes that inherit from unittest.TestCase]
    C --> D[Finds methods that start with test_]
    D --> E[Runs each test method in its own instance of TestCase]
    E --> F[Uses assert methods such as assertEqual or assertTrue to check results]
    F --> G{Pass or Fail}
    G -->|Pass| H[Record test passed]
    G -->|Fail| I[Record test failed and show traceback]
    H --> J[Generate summary of all tests]
    I --> J
    J --> K[Display final report in terminal]


```

#### **Explanation of above diagram**

1.  You write your test file (e.g., `test_math.py`).
    
2.  The `unittest` module looks for classes that inherit from `unittest.TestCase`.
    
3.  It scans those classes for methods that start with `test_`.
    
4.  Each test method runs independently — using assertions to check correctness.
    
5.  The framework collects all results (Pass/Fail).
    
6.  Finally, it prints a clear summary in the terminal.





