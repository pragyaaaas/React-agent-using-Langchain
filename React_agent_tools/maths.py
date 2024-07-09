from math import *
from langchain.agents import tool

@tool

def calculate(expression):
    """
    Evaluate a mathematical expression and return the result.

    Args:
        expression (str): The mathematical expression to evaluate.

    Returns:
        str: The result of evaluating the expression, or an error message if the expression is invalid or an error occurs.

    This function uses the built-in `eval` function to evaluate the given mathematical expression.
    It attempts to convert the result to a string and returns it with the prefix "Result: ".
    If the expression contains a name error or syntax error, it returns an "Invalid expression" message with the error details.
    If any other exception occurs, it returns an "An error occurred" message with the exception details.

    Note: This function should be used with caution, as `eval` can be a security risk if the input is not properly sanitized.

    Example:
        >>> calculate("2 + 3")
        "Result: 5"

        >>> calculate("10 / 2")
        "Result: 5.0"

        >>> calculate("sqrt(16)")
        "Result: 4.0"

        >>> calculate("invalid_expression")
        "Invalid expression: name 'invalid_expression' is not defined"
    """
    try:
        result = str(eval(expression))
        return f"Result: {result}"
    except (NameError, SyntaxError) as e:
        return f"Invalid expression: {e}"
    except Exception as e:
        return f"An error occurred: {e}"

