


### 1. unittest Framework Basics

```mermaid

mindmap
  root("unittest Framework")

    TestCase
      "Base class for writing test cases"
      "Provides assertion methods and test fixtures"

    Assertions
      "Validate expected vs actual outcomes"
      "Examples: assertEqual, assertTrue, assertRaises"

    Test Runner
      "Executes and reports tests"
      "Examples: unittest, nose2, pytest"



```
---

### 2. Test Lifecycle

```mermaid



mindmap
  root("Python Unit Test Lifecycle")

    Execution Order
      "setUpClass -> runs once before all tests"
      "setUp -> runs before each test method"
      "test_... -> actual test logic"
      "tearDown -> runs after each test method"
      "tearDownClass -> runs once after all tests"

    Purpose of Each Method
      setUpClass
        "Purpose"
        "Create shared resources like DB connections or files"
        "Runs once per class"
      setUp
        "Purpose"
        "Prepare fresh test data before

```

### 3. Test Doubles


```mermaid

mindmap
  root("Test Doubles")

    Overview
      "Stand-ins for real objects"

    Stub
      "Canned responses"
      "Returns fixed data"

    Fake
      "Simplified working implementation"
      "In-memory database example"

    Mock
      "Simulates objects"
      "Records interactions"

    Spy
      "Wraps real object"
      "Tracks method calls"

    Tools
      "unittest.mock module"
      "MagicMock tracks calls"
      "patch replaces objects"



```


### 4 Test Design & Results

```mermaid

mindmap
  root("Test Design and Results")

    Unit Test
      "Tests individual isolated components"
      "Smallest testable part of an application"

    Integration Test
      "Tests multiple components working together"
      "Broader than unit tests"

    System Test
      "Tests the entire application in real environment"
      "Includes external dependencies"

    Test Outcomes
      "ok - test passed"
      "FAIL - AssertionError occurred"
      "ERROR - unexpected exception occurred"

    Side Effects
      "Changes to environment outside return value"
      "Should be controlled to keep tests repeatable"

    Test Principles
      "Isolation - tests do not rely on external state"
      "Automation - run tests automatically"
      "Fast - tests provide immediate feedback

```


### 5. Python Unit Test suites

```mermaid

mindmap
  root("Python unittest Test Suites")

    Manual Creation
      "Create TestSuite object"
      "Add specific test methods"
      "Add entire TestCase classes"
      "Gives full control over which tests run"

    Test Loader
      "Use TestLoader to find tests automatically"
      "loadTestsFromModule loads all tests from module"
      "discover finds tests recursively in folder"
      "Easier for large projects"

    Test Runner
      "Use TextTestRunner or other runners"
      "Runs all tests in the suite"
      "Shows results: dot=pass, F=fail, E=error"
      "Provides summary of test run"

    Example Workflow
      "Manual: create suite, add tests, run suite"
      "Loader: discover tests, run discovered suite"

```

#### What does the above diagram show
1. Root Node
* "Python unittest Test Suites" → This is the central topic. Everything branches out from here.
2. Manual Creation
* Create TestSuite object → You start by creating an empty suite.

* Add specific test methods → You can add individual test methods from TestCase classes.

* Add entire TestCase classes → You can add all tests from a TestCase at once.

* Gives full control over which tests run → You control exactly what runs, useful for small or targeted tests.

3. Test Loader
* Use TestLoader to find tests automatically → Loader automates finding tests.

* loadTestsFromModule loads all tests from module → Automatically adds all tests from a single module.

* discover finds tests recursively in folder → Automatically searches folders for files matching test_*.py and loads all tests.

* Easier for large projects → This saves manual work as your project grows.

4. Test Runner
*  Use TextTestRunner or other runners → Executes the suite.

* Runs all tests in the suite → All tests added to the suite are executed.

* Shows results: dot=pass, F=fail, E=error → The output indicates which tests passed, failed, or errored.

* Provides summary of test run → Shows total tests run, failures, errors, and time taken.

5. Example Workflow
* Manual: create suite, add tests, run suite → Visualizes how manual suites are executed.

* Loader: discover tests, run discovered suite → Visualizes automatic discovery workflow.



### Simple diagram showing how `TestLoader` works with `TestSuite` and `TestRunner` in Python’s unittest framework:


```mermaid

flowchart TD
    A[TestLoader] --> B[TestSuite]
    B --> C[TestCase1]
    B --> D[TestCase2]
    B --> E[TestCase3]
    F[TestRunner] --> B

    subgraph Discovery
        G[Load from Module] --> B
        H[Discover Tests in Directory] --> B
    end

    style A fill:#f9f,stroke:#333,stroke-width:2px
    style B fill:#bbf,stroke:#333,stroke-width:2px
    style F fill:#bfb,stroke:#333,stroke-width:2px




```










