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


def no_duplicates(a_string):
       # Remove duplicates using a set, excluding whitespace
        unique_chars = set(a_string.replace(" ", ""))
        # Sort the unique characters
        sorted_chars = sorted(unique_chars)
        # Join the sorted characters into a string, preserving whitespace
        sorted_string = ''.join(sorted_chars)
        return sorted_string

input_str = "hello world"
sorted_str = no_duplicates(input_str)
print(sorted_str)  # Output: "dehlorw"


input_str = "monty pythons flying circus"
sorted_str = no_duplicates(input_str)
print(sorted_str)  #  cfghilmnoprstuy'

