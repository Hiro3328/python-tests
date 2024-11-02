"""
Encrypts or Decrypts a string, based on a given key
Works similarly to a caesar cipher, except it also varies with the position of the character in the text


Made By: Hiro3328 /#/ Current Rev: 5.0.0
"""

characters = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!\"#$%&'()*+,-./:;<=>?@[\\]^_`{|}~ çÇáéíóúÁÉÍÓÚäëïöüÄËÏÖÜàèìòùÀÈÌÒÙãẽĩõũÃẼĨÕŨâêîôûÂÊÎÔÛ" 
charSize = len(characters)

def encrypt(message: str, key = 3218):
    """Encrypts a string, if no key is given defaults to 3218\n    
    Made By: Hiro3328"""
    return ''.join(
        characters[
        (characters.index(char) + int(key*pos))%charSize
    ] if char in characters 
        else char 
    for pos, char in enumerate(message))

def decrypt(message: str, key = 3218):
    """Decrypts a string, if no key is given defaults to 3218\n    
    Made By: Hiro3328"""                                
    return ''.join(
        characters[
        (characters.index(char) - int(key*pos))%charSize
    ] if char in characters 
        else char 
    for pos, char in enumerate(message))

