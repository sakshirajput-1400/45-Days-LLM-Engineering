"""
Problem 02 - BMI Calculator   (Day 1: arithmetic & exponent)   [STUB]

BMI = weight (kg) / height (m) squared.  Round to 1 decimal place.
Example: 72 kg, 1.75 m  ->  23.5

Skills: division, the exponent operator **, round().

Run:
    python q02_bmi_calculator.py
"""

def bmi(weight_kg, height_m):
    """Return the Body Mass Index, rounded to 1 decimal place."""
    # TODO: height squared is  height_m ** 2
    # TODO: bmi value = weight_kg / (height squared)
    # TODO: return it rounded to 1 decimal  (round(value, 1))
    pass


if __name__ == "__main__":
    print(bmi(72, 1.75))    # expected: 23.5
    print(bmi(50, 1.60))    # expected: 19.5
