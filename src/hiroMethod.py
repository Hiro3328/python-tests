"""
Encrypts or Decrypts a string, based on a given key, default is 3218


Made By: Hiro3328 /#/ Current Rev: 3.3
"""
from string import ascii_letters as characters
print(characters)

def encrypt(message: str, key = 3218):
    """Encrypts a string, based on a given key, default is 3218\n    
    Made By: Hiro3328"""
    return ''.join(
        characters[
        (characters.index(char.lower()) + int(key*pos))%26
    ] if char.lower() in characters 
        else char 
    for pos, char in enumerate(message))

def decrypt(message: str, key = 3218):
    """Decrypts a string, based on a given key, default is 3218\n    
    Made By: Hiro3328"""                                
    return ''.join(
        characters[
        (characters.index(char.lower()) - int(key*pos))%26
    ] if char.lower() in characters 
        else char 
    for pos, char in enumerate(message))


