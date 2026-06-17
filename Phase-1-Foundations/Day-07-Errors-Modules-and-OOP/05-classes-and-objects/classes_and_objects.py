"""
Classes & objects — your own types. Blueprint (class) -> instances (objects).

Run:
    python classes_and_objects.py
"""

# =====================================================================
# 1) A first class: __init__ sets up each instance; self = "this object"
# =====================================================================
class Dog:
    def __init__(self, name, breed):    # runs automatically on Dog(...)
        self.name = name                # store data ON this instance
        self.breed = breed

# Create two INDEPENDENT instances from the one blueprint:
rex = Dog("Rex", "Labrador")            # the args fill __init__'s parameters
luna = Dog("Luna", "Beagle")

print("rex.name   :", rex.name)
print("luna.breed :", luna.breed)

# They don't share data — change one, the other is untouched:
rex.name = "Rex Jr."
print("after rename -> rex:", rex.name, "| luna:", luna.name)
print()

# =====================================================================
# 2) Why a class beats a bare dict (when data has structure/behaviour)
# =====================================================================
# As a dict: works, but nothing guarantees the fields or names the type.
dog_dict = {"name": "Bruno", "breed": "Pug"}
print("dog as dict :", dog_dict["name"])

# As a class: the TYPE has a name, and __init__ guarantees every dog has
# a name and breed. (Module 06 adds behaviour the dict can't carry.)
bruno = Dog("Bruno", "Pug")
print("dog as class:", bruno.name, "is a", type(bruno).__name__)
print()

# =====================================================================
# 3) REAL USE: model a course student (data that belongs together)
# =====================================================================
class Student:
    def __init__(self, name, roll_no, marks):
        self.name = name
        self.roll_no = roll_no
        self.marks = marks              # a list of marks (any type allowed)

asha = Student("Asha", "BTECH-21-007", [88, 72, 95])
print(f"{asha.name} (roll {asha.roll_no}) has {len(asha.marks)} marks recorded")
print("average so far:", sum(asha.marks) / len(asha.marks))
# Module 06 turns "sum(asha.marks)/len(...)" into a clean asha.average() method.
