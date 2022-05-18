"""1.For a list of words, print out each word on a separate line, 
    but in all uppercase. How can you change a word to uppercase? 
    Ask Python for help on what you can do with strings!

2.Turn that into a function, print_upper_words. Test it out. 
(Don’t forget to add a docstring to your function!)

3.Change that function so that it only prints words that start with 
the letter ‘e’ (either upper or lowercase).

4.Make your function more general: you should be able to pass in a set of 
letters, and it only prints words that start with one of those letters."""

"""Print each word on seporate line, uppercased"""
def print_upper_words(words):
    """ >>> print_upper_words(["Programming", "is", "pretty", "fun"])
        PROGRAMMING
        IS
        PRETTY
        FUN"""
    for word in words:
        print(word.upper())

"""Print words that start with 'e or E'"""
def print_upper_words2(words):
    for word in words:
        if word.startswith('e') or word.startswith('E'):
            print(word)

def print_upper_words3(words, must_start_with):
    for word in words:
        for letter in must_start_with:
            if word.startswith(letter):
                print(word.upper())
                