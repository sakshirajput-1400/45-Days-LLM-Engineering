"""
Problem 02 - BMI Calculator   (SOLUTION)

Run:
    python q02_bmi_calculator_solution.py

Logic note:
  ** is the power operator, so height_m ** 2 is height squared. Mind the
  parentheses: weight / height ** 2 already works (** binds tighter than /),
  but wrapping the denominator makes the intent obvious.
"""

def bmi(weight_kg, height_m):
    """Return the Body Mass Index, rounded to 1 decimal place."""
    value = weight_kg / (height_m ** 2)
    return round(value, 1)


if __name__ == "__main__":
    people = [("Asha", 72, 1.75), ("Ravi", 50, 1.60), ("Meena", 95, 1.70)]
    for name, kg, m in people:
        print(f"{name:6} BMI = {bmi(kg, m)}")
