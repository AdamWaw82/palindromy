def is_it_palindrome(word: str):
    """
        The function checks whether the given word is a palindrome
        Arguments:
        word
    """
    reversed_string = ""
    for char_index in range(len(word) -1, -1, -1):
        reversed_string += word[char_index]


    return word == reversed_string
