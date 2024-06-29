def is_it_palindrome(txt: str):
    reversed_string = ""
    for char_index in range(len(txt) -1, -1, -1):
        reversed_string += txt[char_index]


    return txt == reversed_string

print( is_it_palindrome('test') )