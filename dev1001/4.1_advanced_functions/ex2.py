# Callbacks Exercise
#
# 1. Write a function: perform_operation(a, b, math_callback).
# 2. This function should take two numbers and a callback.
# 3. The callback function itself should accept two numbers and return their result
#       (e.g., sum, product).
# 4. perform_operation() should then print this result.
# 5. Create two simple callbacks (e.g., add_them, multiply_them) and
#       test perform_operation with both.

def perform_operation(a, b, math_callback):
    result = math_callback(a, b)
    print(result)

def add_them(x, y):
    return x + y

def multiply_them(x, y):
    return x * y

perform_operation(5, 10, add_them)
perform_operation(5, 10, multiply_them)
