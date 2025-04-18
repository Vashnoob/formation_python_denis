from string import punctuation

def clean_line(phrase):

    punct = punctuation.replace("-", "")

    phrase = phrase.lower()

    for c in punct:
        phrase = phrase.replace(c, " ")
    return phrase
