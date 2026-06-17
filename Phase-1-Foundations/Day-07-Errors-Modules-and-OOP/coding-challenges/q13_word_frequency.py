"""
Problem 13 - Word frequency   (Day 6: dictionaries)   [STUB]

Count how many times each word appears in a sentence (case-insensitive) and
return the count dictionary. Then find the single most common word.
Example: "the cat the dog the" -> {"the": 3, "cat": 1, "dog": 1}; top = ("the", 3)

Skills: .lower(), .split(), dict, dict.get(key, 0), looping over .items().

Run:
    python q13_word_frequency.py
"""

def word_freq(sentence):
    """Return a dict mapping each lower-cased word to its count."""
    # TODO: counts = {}
    # TODO: for word in sentence.lower().split():
    # TODO:     counts[word] = counts.get(word, 0) + 1   # 0 if unseen
    # TODO: return counts
    pass


def most_common(sentence):
    """Return (word, count) for the most frequent word."""
    # TODO: get counts via word_freq(sentence)
    # TODO: loop the items, keep the word with the highest count
    pass


if __name__ == "__main__":
    print(word_freq("the cat the dog the"))   # {'the': 3, 'cat': 1, 'dog': 1}
    print(most_common("the cat the dog the")) # ('the', 3)
