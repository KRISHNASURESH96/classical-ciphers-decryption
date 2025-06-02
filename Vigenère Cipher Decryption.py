#!/usr/bin/env python
# coding: utf-8

# # Vigenere Cipher Decryption with Python
# 
# This code demonstrates how to break a Vigenère cipher encryption by using brute-force techniques to deduce the keyword and decrypt the message.
# 
# We apply this to a provided encrypted message that is known to contain the word `gingerbread`.
# 

# # Problem Description
# 
# 
# The Vigenère cipher is a classical encryption technique that uses a repeating keyword to shift letters according to a Vigenère table.
# 
# Given an encrypted message and the knowledge that:
#   
#   The decrypted message contains the word `gingerbread`  
#   The keyword is **four letters long**
# 
# Our task is to:
# - Deduce the encryption keyword
# - Decrypt the full message
# - Print both the decrypted message and the keyword used
# 
# 

# #  Define Cipher Text

# In[1]:


# Prepare the encoded message as a string
encrypted_text = "kbokzzrbisolqkchwgzxilrhjoenzazhgfolgokhdikdgfoltcnxzglqcfokprowqzrcusjhwbksnlwvwtwizosywhodycowkbldggokfrooiuokprofcbzvnookprolgokhwbksnltyopzxgrosplrhosuswaolqkchyvzcmlwvqiihudzmggolcyzxiljyfookprocczkhwbksnltyopzxgrogkhyhvvvhowootlfxzzfgzuikfirvnmokfrontmospuiofwvxvgodqlnovlzxifvnksedulrczkvvnlrcztiouvoqkbxotlrxflfbcbxoznvcvllxvwchfclqjlaeuhomqavczhfqghyotlusxwuozrfeivosplykntokpromtsrdglkgqlusuqjhyfrzzsrmjlzxzdckuhzmzkikrlrxfltrkzchwbksnlwstaokdcldzhnyzhfhvvioglyywfjhrfvrgokhqjvxzhfhqbvhjientsuhcbuhgwxrvmokprovkbvhvkfhnoiqglskmweqzgyoghjhywkrzdrbevdophozcdvbzdckesoypsonkgthqtonqixrzcehclcsivkvalwvqiiofljettrmglrxfliynzoephzvzvrvhlrhesedkavdtsodjwtuzqldzcldzuzxisiltsrnztzqwfvczkzdjlrhusmopltophzwghiozkzngltevhvbzoenzhikpgwotlkyzprukbxhuvvovgolcyvhwbksnljvkuydnmozwtwoflrxfljovlespsodqlkopldspikouluorsenkbxhqbodjsocknvhqtoiqiihecfuksomwhkotgovghomqcchqbolcyzxiljrgskcztfbztzfgldspikoulsohciozhikpgwotfzxilkyzoomqccspuobcqbhvcomqcchecdznskonm"


# # Define Decryption Function
# 

# In[2]:


# The function vigenere_decrypt is defined with the parameters cipher, known_word & key_length. 
# Cipher is the encrypted text, known_word is gingerbread which should be contained in the decrypted text, 
# key_length denotes the length of the keyword
def vigenere_decrypt(cipher, known_word="gingerbread", key_length=11):
    
    # Function to decrypt a single character (char) from encrypted text using a single character from the keyword (key)
    def decrypt_char(char, key):  
        
        # ord(char) & ord(key) are used for finding the unicode code values of single characters from the encrypted text (char) and from the keyword (key)
        # substracting the unicode code value of key from that of encrypted text gives the shift done by the vinegere cipher
        # %26 in this case is used to ensure that the value stays between a - z
        # ord('a') encaplsulates the value into lowercase alphabetic letters
        return chr((ord(char) - ord(key)) % 26 + ord('a')) 

    # Function to deduce the encryption key using known plaintext and corresponding ciphertext
    def deduce_key(known_word, encrypted_portion):
        
        # Calculates the encryption key using the known word & the corresponding encrypted portion of the keyword
        # We take a window sliding approach, with each window of size 11 (corresponding to the length of known word gingerbread). 
        # For each window, we try to deduce the key from the encrypted portion and plaintext(gingerbread) 
        # For each character, it calculates the part of the key using the logic described in decrypt_char, but in reverse order.
        # join() combines all the decrypted characters to form the encryption key
        return ''.join([chr((ord(encrypted_portion[i]) - ord(known_word[i])) % 26 + ord('a')) for i in range(len(known_word))])

    # Step to decrypt the entire message using a guessed key
    def decrypt_message(cipher, key):
        
        # In the vigenere cipher each character in the plaintext or ciphertext corresponds to a character in the key. If the key is shorter than the plaintext or ciphertext it needs to be repeated. 
        # The // operator divides and rounds of to the nearest integer. len(cipher) // key_length calculates how many times the key can be fully repeated to cover the length of the ciphertext.
        # The operator % gives the remainder of a division. Thus, len(cipher) % key_length calculates the remainder of characters after fully repeating the key.
        full_key = key * (len(cipher) // key_length) + key[:len(cipher) % key_length]
        
        # Decrypts the entire ciphertext using the full_key. The list comprehension iterates over the ciphertext, decrypts each character, and then join() combines them into a single string.
        return ''.join([decrypt_char(cipher[i], full_key[i]) for i in range(len(cipher))])
        
        # The loop iterates over the ciphertext to check each segment of length known_word to deduce the potential encryption key.
    for i in range(len(cipher) - len(known_word) + 1):
        encrypted_portion = cipher[i:i+len(known_word)]
        
        # Deduces the key segment corresponding to the encrypted_portion using the known_word.
        guessed_key_portion = deduce_key(known_word, encrypted_portion)
        
        # Extract potential keys by taking 4 consecutive characters from the guessed_key_portion
        for j in range(len(guessed_key_portion) - key_length + 1):
            
            # Extracts a key of length key_length from the guessed_key_portion
            key = guessed_key_portion[j:j+key_length]
            decrypted_text = decrypt_message(cipher, key)
            
            if known_word in decrypted_text:
                print(decrypted_text)
                return key

    return None  # Return None if decryption failed



# # Run the Decryption

# In[3]:


# Call your function here
keyword = vigenere_decrypt(encrypted_text, "gingerbread", 4)
print(f"\nThe keyword used for encryption is: {keyword}")


# # Summary of Results

# The Vigenère cipher was successfully broken using brute-force methods.
# 
# | Result               | Value   |
# |-----------------------|---------|
# | Keyword used         | cork    |
# | Known word matched   | gingerbread |
# 
# The decrypted message reveals a delicious gingerbread recipe, confirming the success of the decryption.
# 

# In[ ]:




