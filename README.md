Streamlit Calculator App:
This is a simple web-based calculator built using Streamlit that evaluates mathematical expressions entered by the user. It provides a clean interface with HTML formatting and displays supported operations using an expander.

Features:
1. User-friendly UI with center-aligned heading using HTML.

2. Expander section showing all supported operations:

+ : Addition

- : Subtraction

* : Multiplication

/ : Division

// : Integer Division

% : Modulo (remainder)

** : Exponentiation (Power)

3. Input field for entering expressions.

4. Validates the input to prevent alphabetic characters.

5. Error handling for invalid input.

6. Displays the result below the entered expression.

Getting Started:
1. Prerequisites
2. Python 3.x

Streamlit

Install Streamlit using pip if you don't have it:
pip install streamlit

How to Run:
Save the code in a Python file, for example calculator_app.py, and run it using:
streamlit run calculator_app.py
The app will open in your default web browser.

Example:
If you enter:
12 + 7 * 3
It will display:
12 + 7 * 3 = 33

Note:
This calculator uses Python's eval() to compute expressions. Avoid entering unsafe or non-mathematical input.

Currently, the app checks for alphabetic characters and basic input validation, but consider additional security for production usage.

