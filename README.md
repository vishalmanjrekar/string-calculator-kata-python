# String Calculator Kata (Python - TDD)

This repository contains the **String Calculator Kata**, implemented in Python using **Test-Driven Development (TDD)**.

## Features Implemented

- Handles empty strings
- Supports summing numbers separated by commas
- Allows newline (`\n`) as a delimiter
- Supports custom delimiters
- Throws an error for negative numbers

---

## **Installation & Setup**

### **1. Clone the Repository**

```bash
git clone https://github.com/vishalmanjrekar/string-calculator-kata-python
cd string-calculator-kata-python
```

### **2. Create and Activate Virtual Environment**

```bash
# On macOS/Linux
python3 -m venv venv
source venv/bin/activate

# On Windows
python -m venv venv
venv\Scripts\activate
```

---

## **Running Tests**

Run the test suite to verify the implementation:

```bash
python -m unittest discover
```

### **Expected Output**

```
.......
----------------------------------------------------------------------
Ran 7 tests in 0.001s

OK
```

---

## **Usage Example**

Run in Python:

```python
from string_calculator import StringCalculator

calculator = StringCalculator()
print(calculator.add("1,2,3"))  # Output: 6
print(calculator.add("//;\n1;2;3"))  # Output: 6
```

---

## **Commit Guidelines**

- **Commit frequently** to showcase the evolution of the implementation through TDD steps.
- Use meaningful commit messages (e.g., `"Test: Support newline as delimiter"` or `"Imp: Custom delimiter support"`).

---

## TDD Workflow (Commit History)
This project follows the Red-Green-Refactor cycle of TDD:

- Write a failing test (Red)
- Implement just enough code to pass the test (Green)
- Refactor the code while keeping all tests green

## Contribution

Want to improve this kata or add more test cases? Feel free to fork the repo and submit a pull request!

## **Author**

Vishal Manjrekar
