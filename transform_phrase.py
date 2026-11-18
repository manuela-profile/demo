"""Transform a phrase into uppercase reversed text with numbered vowels."""


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


if __name__ == "__main__":
    for sample in ("hello", "hello world", "Python is fun!", ""):
        print(f"{sample!r} -> {transform_phrase(sample)!r}")
