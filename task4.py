import sys
from decimal import Decimal

print("========================================")
print("  FLOATING-POINT ARITHMETIC    ")
print("========================================\n")

# ---------------------------------------------------------
# 1. BASIC ROUNDING ERROR (The 0.1 + 0.2 Problem)
# ---------------------------------------------------------
print("--- 1. Rounding Error Example ---")
result_float = 0.1 + 0.2
print(f"Standard Float: 0.1 + 0.2 = {result_float}")
print(f"Is it exactly 0.3? {result_float == 0.3}\n")


# ---------------------------------------------------------
# 2. CATASTROPHIC CANCELLATION & MACHINE EPSILON
# ---------------------------------------------------------
print("--- 2. Catastrophic Cancellation ---")
# Machine epsilon is the smallest number that can be added to 1.0
epsilon = sys.float_info.epsilon
print(f"Machine Epsilon: {epsilon}")

# Demonstrating the limit of precision
a = 1.0000000000000001
b = 1.0000000000000000
c = a - b
print(f"a - b = {c} (Expected ~1e-16, but precision is lost)\n")


# ---------------------------------------------------------
# 3. OVERFLOW AND UNDERFLOW
# ---------------------------------------------------------
print("--- 3. Overflow / Underflow ---")
max_float = sys.float_info.max
print(f"Max Float: {max_float}")
print(f"Max Float * 2 (Overflow): {max_float * 2}\n")


# ---------------------------------------------------------
# 4. INSTRUCTION C & E: MODIFIED PROGRAM (THE SOLUTION)
# ---------------------------------------------------------
print("--- 4. Real-World Solution: Financial Ledger ---")
print("Using Decimal module to fix precision errors:")

# Standard floats (Prone to error)
amount_1 = 0.1
amount_2 = 0.2
print(f"Float Addition:      {amount_1 + amount_2}")

# Modified inputs using Decimal strings (Exact precision)
decimal_1 = Decimal('0.1')
decimal_2 = Decimal('0.2')
print(f"Decimal Addition:    {decimal_1 + decimal_2}")
print("Conclusion: Decimal module prevents rounding errors in financial applications.")
