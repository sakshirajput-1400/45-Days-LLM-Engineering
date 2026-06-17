"""
Problem 05 - Clean & title-case a messy string   (Day 2: string methods)   [STUB]

Tidy a messy heading: collapse extra spaces and capitalise each word.
Example: "  hELLo    wORLD  "  ->  "Hello World"

Skills: .split(), .capitalize(), " ".join(list), building a list.

Run:
    python q05_clean_title.py
"""

def clean_title(messy):
    """Return messy with single spaces and each word capitalised."""
    # TODO: .split() with no args -> a list of words, extra spaces gone
    # TODO: build a new list where each word is .capitalize()-d
    # TODO: join that list back together with single spaces: " ".join(words)
    pass


if __name__ == "__main__":
    print(clean_title("  hELLo    wORLD  "))   # expected: Hello World
    print(clean_title("the  TODO   list"))     # expected: The Todo List
