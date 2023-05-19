def four_char_strings(a_string):
    # Remove any leading or trailing spaces from the input string
    input_string = a_string.strip()
    print(input_string)
    # Create a list to store the 4-character strings
    four_char_strings = []
    # Iterate over the input string, extracting 4-character substrings
    i = 0
    while i < (len(input_string)):
        four_char_strings.append(input_string[i:i + 4])
        i = i + 4

    return four_char_strings

input_str = "monty pythons flying circus"
four_chars = four_char_strings(input_str)
print(four_chars)


#Example: ['mont', 'y py', 'thon', 's fl', 'ying', ' cir', 'cus']
