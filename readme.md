# Calculator Prueba

This project contains a simple arithmetic module that performs basic mathematical operations.

## Arithmetic Module

The `arithmetic` module provides a class `Arithmetic` that can perform the following operations:

- Addition
- Subtraction
- Multiplication
- Division

### Usage

To use the `Arithmetic` class, you need to create an instance of the class with two numbers and then call the desired method.

```python
from calculator_prueba.arithmetic import Arithmetic

# Create an instance of Arithmetic
calc = Arithmetic(10, 5)

# Perform operations
print(calc.add())       # Output: 15
print(calc.subtract())  # Output: 5
print(calc.multiply())  # Output: 50
print(calc.divide())    # Output: 2.0
```

### Division by Zero

The `divide` method raises a `ValueError` if an attempt is made to divide by zero.

```python
calc = Arithmetic(10, 0)
calc.divide()  # Raises ValueError: Cannot divide by zero
```
