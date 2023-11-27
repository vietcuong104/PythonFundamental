from spellchecker import SpellChecker


def correctSpellings():
    corrector = SpellChecker()
    word = input("Enter a word: ")

    if word in corrector:
        print("Correct")
    else:
        correct_word = corrector.correction(word)
        print("The correct word is: ", correct_word)


correctSpellings()