# 05 — Classes & Objects

A **class** is a blueprint for a new *type* of thing. An **object** (or **instance**) is one item built
from that blueprint. Classes bundle **data** (attributes) with **behaviour** (methods, Module 06) —
the foundation of how every library you'll use is built (`ChatSession`, `Document`, `Agent`…).

```python
class Dog:                          # blueprint (capital-C class name by convention)
    def __init__(self, name, breed):    # the "constructor" — sets up each new dog
        self.name = name                # store data ON this instance
        self.breed = breed

rex = Dog("Rex", "Labrador")        # create an INSTANCE (calls __init__)
luna = Dog("Luna", "Beagle")        # a different, independent instance
print(rex.name)                     # "Rex"  -> read an attribute
print(luna.breed)                   # "Beagle"
```

## `__init__` and `self` (the two confusing bits)
- **`__init__`** runs automatically when you create an instance. It's where you set up the object's
  starting data. (It's a "dunder" — *double underscore* — method.)
- **`self`** is the instance being worked on — "this particular object." You never pass it yourself;
  Python passes it for you. `self.name = name` means "store `name` *on this object*."

```python
rex = Dog("Rex", "Labrador")
#         └ becomes `name`; `self` is the new object being built
```

## Class vs the things you already know
A dict can hold a dog's data: `{"name": "Rex", "breed": "Labrador"}`. A **class** does that *and*
gives the type a name, guarantees the fields via `__init__`, and (Module 06) attaches behaviour. When
data and the operations on it belong together, reach for a class.

## 🎤 Talking points (what to say & focus on)
- **"Class = cookie cutter; object = a cookie."** One blueprint, many independent instances. `rex` and
  `luna` don't share data — prove it by changing one and printing the other.
- **`__init__` = setup, runs on creation.** Don't call it yourself; `Dog(...)` calls it. The arguments
  to `Dog(...)` land in `__init__`'s parameters. Trace that flow on the board.
- **`self` demystified:** it's just "this object." Every instance method's first parameter. `self.x`
  reads/writes data *on this instance*. The #1 OOP confusion — go slow, repeat it.
- **Motivate from a dict.** Show a dog-as-dict, then a dog-as-class. The class names the type and
  guarantees the shape. "When the data has behaviour, it wants to be a class."
- **Naming conventions:** ClassNames are CapWords; instances/attrs are lower_snake. Small thing,
  signals fluency.

## ⚠️ Common mistakes to call out
- Forgetting `self` in a method's parameter list → `TypeError` about arguments.
- Writing `__init__` with one underscore or misspelled → it won't run as the constructor.
- Confusing the class (`Dog`) with an instance (`rex`) — you call methods on instances.
- Setting attributes outside `__init__` and being surprised they're missing on other instances.

Run the examples:

```bash
python classes_and_objects.py
```

➡ Next: **[06-instance-methods](../06-instance-methods/)**
