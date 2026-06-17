"""
Problem 15 - Class gradebook   (Day 6 + 5: dict of lists, functions)   [STUB]

A gradebook maps each student name -> a list of their marks:
    {"Asha": [88, 92, 79], "Ravi": [70, 65, 80], "Meena": [95, 99, 91]}
Write:
  - averages(gradebook): return {name: average_rounded_2}
  - topper(gradebook):   return (name, average) of the student with the best average

Skills: looping a dict's .items(), sum()/len(), nested data (dict of lists),
        calling one function from another, "best so far".

Run:
    python q15_gradebook.py
"""

def averages(gradebook):
    """Return {name: average mark rounded to 2 decimals}."""
    # TODO: result = {}
    # TODO: for name, marks in gradebook.items():  result[name] = round(sum(marks)/len(marks), 2)
    # TODO: return result
    pass


def topper(gradebook):
    """Return (name, average) for the student with the highest average."""
    # TODO: get the averages dict
    # TODO: loop it, keep the (name, avg) with the biggest avg ("best so far")
    pass


if __name__ == "__main__":
    book = {"Asha": [88, 92, 79], "Ravi": [70, 65, 80], "Meena": [95, 99, 91]}
    print(averages(book))   # {'Asha': 86.33, 'Ravi': 71.67, 'Meena': 95.0}
    print(topper(book))     # ('Meena', 95.0)
