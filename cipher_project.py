from tkinter import *
from tkinter import ttk

def dictionary(x):
    """Explain what this function does"""
    dictionary = {}
    for i in range(len(x)):
        dictionary[i] = x[i]
    return dictionary

def swap_dict(dict):
    return {v: k for k,v in dict.items()}

# Text sets, list with two values: A string with every character in the set and an integer for the length of the string
ascii_chars = ['0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ! "#$%&\'()*+,-./:;<=>?@[]^_`{|}~', 93]
alphabet_chars = ['ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz', 52]
alphabet_chars_wUnderscore = ['ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz_', 53]
uppercase_alphabet_chars = ['ABCDEFGHIJKLMNOPQRSTUVWXYZ', 26]
lowercase_alphabet_chars = ['abcdefghijklmnopqrstuvwxyz', 26]


def caesarEncrypt(message, key, textset):
    """Explain what this function does"""
    a_dictionary = dictionary(list(message))
    ascii_dict = swap_dict(dictionary(list(textset[0])))
    encrypt_list = []
    encrypt_phrase = []

    for i in a_dictionary:
        encrypt_list.append((ascii_dict[a_dictionary[i]] + key) % textset[1])

    for char in encrypt_list:
        encrypt_phrase.append(dictionary(list(textset[0]))[char])
    return "".join(encrypt_phrase)

def caesarDecrypt(message, key, textset):
    """Explain what this function does"""
    a_dictionary = dictionary(list(message))
    ascii_dict = swap_dict(dictionary(list(textset[0])))
    encrypt_list = []
    encrypt_phrase = []

    for i in a_dictionary:
        encrypt_list.append((ascii_dict[a_dictionary[i]] - key) % textset[1])

    for char in encrypt_list:
        encrypt_phrase.append(dictionary(list(textset[0]))[char])

    return "".join(encrypt_phrase)

def vigenereEncrypt(messagev, keyv, textset): 
    """Explain what this function does"""
    a_dictionary = dictionary(list(keyv))
    b_dictionary = dictionary(list(messagev))
    ascii_dict = swap_dict(dictionary(list(textset[0])))
    encrypt_list = []
    b_encrypt_list = []
    encrypt_phrase = []

    for i in a_dictionary:
        encrypt_list.append((ascii_dict[a_dictionary[i]]) % textset[1])
    for i in b_dictionary:
        b_encrypt_list.append((ascii_dict[b_dictionary[i]]) % textset[1])
    
    fin_encrypt_list = []

    for i in b_dictionary:
        x = encrypt_list[i % (len(encrypt_list))] + b_encrypt_list[i]
        fin_encrypt_list.append(x)

    encrypt_phrase = []

    for char in fin_encrypt_list:
        encrypt_phrase.append(dictionary(list(textset[0]))[char % textset[1]])

    return "".join(encrypt_phrase)

def vigenereDecrypt(messagev, keyv, textset): 
    """Explain what this function"""
    a_dictionary = dictionary(list(keyv))
    b_dictionary = dictionary(list(messagev))
    ascii_dict = swap_dict(dictionary(list(textset[0])))
    encrypt_list = []
    b_encrypt_list = []
    encrypt_phrase = []

    for i in a_dictionary:
        encrypt_list.append((ascii_dict[a_dictionary[i]]) % textset[1])
    for i in b_dictionary:
        b_encrypt_list.append((ascii_dict[b_dictionary[i]]) % textset[1])
    
    fin_encrypt_list = []

    for i in b_dictionary:
        x = b_encrypt_list[i] - encrypt_list[i % (len(encrypt_list))]
        fin_encrypt_list.append(x)

    encrypt_phrase = []

    for char in fin_encrypt_list:
        encrypt_phrase.append(dictionary(list(textset[0]))[char % textset[1]])

    return "".join(encrypt_phrase)


# Below this point is the user input ... section?... area...? I wouldn't know what to call it. 
def begin(): 
    input_action = input("Encryption or decryption (e/d): ")

    if input_action == 'e':
        input_cipher = input("Caesar or vigenere? (c/v): ")
        if input_cipher == 'c':
            # Caesar Cipher
            message = input("Enter a message: ")
            key = int(input("Enter a key: "))

            if int(key) is not int:
                print("KEYS ONLY ACCEPT INTEGERS FOR CAESAR CIPHER")
                return begin()
            else:
                try:
                    print(caesarEncrypt(message, key, uppercase_alphabet_chars))
                except:
                    print(caesarEncrypt(message, key, ascii_chars))
                return begin()
        
        elif input_cipher == 'v':
            # Vigenere Cipher
            message = input("Enter a message: ")
            key = input("Enter a key: ")
            try:
                print(vigenereEncrypt(message, key, uppercase_alphabet_chars))
            except:
                print(vigenereEncrypt(message, key, ascii_chars))
            return begin()
        
        else:
            print("Sorry, this version does not support that cipher.")
            return begin()
        
    elif input_action == 'd':
        input_cipher = input("Caesar or vigenere? (c/v): ")
        if input_cipher == 'c':
            message = input("Enter a message: ")
            key = int(input("Enter a key: "))
            try:
                print(caesarDecrypt(message, key, uppercase_alphabet_chars))
            except:
                print(caesarDecrypt(message, key, ascii_chars))
            return begin()
        
        elif input_cipher == 'v':
            message = input("Enter a message: ")
            key = input("Enter a key: ")
            text = input("")
            try:
                print(vigenereDecrypt(message, key, uppercase_alphabet_chars))
            except:
                print(vigenereDecrypt(message, key, ascii_chars))
            return begin()
        else:
            print("Sorry, this version does not support that cipher.")
            return begin()
    else:
        print("Please select method")
        begin()

begin()