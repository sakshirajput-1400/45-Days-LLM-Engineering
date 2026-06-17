"""
Problem 13 - Word frequency   (SOLUTION)

Run:
    python q13_word_frequency_solution.py

Logic note:
  counts.get(word, 0) returns the current count or 0 if the word is new -- that
  single line replaces an "if word in counts / else" branch. For the top word,
  use the "best so far" pattern while looping the dictionary's items.
"""

def word_freq(sentence):
    """Return a dict mapping each lower-cased word to its count."""
    counts = {}
    for word in sentence.lower().split():
        counts[word] = counts.get(word, 0) + 1
    return counts


def most_common(sentence):
    """Return (word, count) for the most frequent word."""
    counts = word_freq(sentence)
    best_word = ""
    best_count = 0
    for word, count in counts.items():
        if count > best_count:
            best_word = word
            best_count = count
    return (best_word, best_count)


if __name__ == "__main__":
    text = "the cat sat on the mat the cat ran"
    print("counts :", word_freq(text))
    print("top    :", most_common(text))
