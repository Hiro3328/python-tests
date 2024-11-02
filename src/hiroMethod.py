"""
Encrypts or Decrypts a string, based on a given key, default is 3218


Made By: Hiro3328 /#/ Current Rev: 4.1
"""
characters = "0123456789aáäàâãbcçdefghiíïìĩîjklmnoóöòõôpqrstuúüùũûvwxyzAÁÄÀÂÃBCÇDEÉËÈẼÊFGHIÍÏÌĨÎJKLJKLMNOÓÖÒÕÔPQRSTUÚÜÙŨÛVWXYZ!\"#$%&'()*+,-./:;<=>?@[\\]^_`{|}~ "

 
charSize = len(characters)

def encrypt(message: str, key = 3218):
    """Encrypts a string, based on a given key, default is 3218\n    
    Made By: Hiro3328"""
    return ''.join(
        characters[
        (characters.index(char) + int(key*pos))%charSize
    ] if char.lower() in characters 
        else char 
    for pos, char in enumerate(message))

def decrypt(message: str, key = 3218):
    """Decrypts a string, based on a given key, default is 3218\n    
    Made By: Hiro3328"""                                
    return ''.join(
        characters[
        (characters.index(char) - int(key*pos))%charSize
    ] if char.lower() in characters 
        else char 
    for pos, char in enumerate(message))

