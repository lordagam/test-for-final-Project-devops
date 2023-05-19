"""With this string:
'monty pythons flying circus'
Create a function that returns a sorted string with no duplicate characters
(keep any whitespace):
Example: ' cfghilmnoprstuy'
Create a function that returns the words in reverse order:
Example: ['circus', 'flying', 'pythons', 'monty']
Create a function that returns a list of 4 character strings:
Example: ['mont', 'y py', 'thon', 's fl', 'ying', ' cir', 'cus']
### git comment
"""
import pytest



def reversed_words(a_string):
    # Split the sentence into words
    words = a_string.split()
    # Reverse the order of the words
    print(words)
    reversed_words = words[::-1]
    return reversed_words

input_sentence = "monty pythons flying circus"
reversed_words = reversed_words(input_sentence)
print(reversed_words)  # Output: ['circus', 'flying', 'pythons', 'monty']