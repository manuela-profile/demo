"""Transform a phrase into uppercase reversed text with numbered vowels."""

import random


def transform_phrase(phrase: str) -> str:
    """Return the phrase in uppercase and reversed, with a number placed
    before every vowel.

    The number is the position of the vowel among the letters only (spaces
    and punctuation are preserved in the output but are not counted).

    Example:
        >>> transform_phrase("hello world")
        'DLR4OW 6OLL9EH'
    """
    if not isinstance(phrase, str):
        raise TypeError("phrase must be a string")

    vowels = set("AEIOU")
    text = phrase.upper()[::-1]

    result = []
    letter_count = 0

    for ch in text:
        if ch.isalpha():
            letter_count += 1
        if ch in vowels:
            result.append(str(letter_count))
        result.append(ch)

    return "".join(result)


def multiply_phrase(
    phrase: str,
    min_multiplier: int = 1,
    max_multiplier: int = 10,
    *,
    number: int | None = None,
) -> str:
    """Repeat ``phrase`` a random number of times to form a new sentence.

    A random integer between ``min_multiplier`` and ``max_multiplier``
    (both inclusive) decides how many copies are joined together with a
    space. Pass ``number`` to skip the random draw (useful for tests).

    Example:
        >>> multiply_phrase("hi", number=3)
        'hi hi hi'
    """
    if not isinstance(phrase, str):
        raise TypeError("phrase must be a string")
    if min_multiplier < 1 or max_multiplier < min_multiplier:
        raise ValueError("expected 1 <= min_multiplier <= max_multiplier")

    if number is None:
        number = random.randint(min_multiplier, max_multiplier)
    elif not isinstance(number, int) or isinstance(number, bool):
        raise TypeError("number must be an int")
    elif number < 1:
        raise ValueError("number must be >= 1")

    return " ".join([phrase] * number)


if __name__ == "__main__":
    for sample in ("hello", "hello world", "Python is fun!", ""):
        final_phrase = transform_phrase(sample)
        print(f"{sample!r} -> {final_phrase!r}")
        print(f"  multiplied -> {multiply_phrase(final_phrase)!r}")
