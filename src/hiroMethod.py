"""
Encrypts or Decrypts a string, based on a given key, default is 3218


Made By: Hiro3328 /#/ Current Rev: 3.3
"""

def encrypt(message: str, key = 3218):
    """Encrypts a string, based on a given key, default is 3218\n    
    Made By: Hiro3328"""
    characters = ["e","a","r","i","o","t","n","s","l","c","u","d","p","m","h","g","b","f","y","w","k","v","x","z","j","q"]
    return ''.join(characters[(characters.index(char.lower()) + int(key*pos))%26] if char.lower() in characters else char for pos, char in enumerate(message))

def decrypt(message: str, key = 3218):
    """Decrypts a string, based on a given key, default is 3218\n    
    Made By: Hiro3328"""                                
    characters = ["e","a","r","i","o","t","n","s","l","c","u","d","p","m","h","g","b","f","y","w","k","v","x","z","j","q"]
    return ''.join(characters[(characters.index(char.lower()) - int(key*pos))%26] if char.lower() in characters else char for pos, char in enumerate(message))


