#!/usr/bin/env python
# coding: utf-8

# # Caesar Cipher Decryption with Python
# 
# This code demonstrates how to break a Caesar cipher encryption by brute-forcing all possible shifts and searching for a known keyword (`pumpkin`).  
# 
# We implement a function that decrypts the message and identifies the shift used.
# 
# The project is part of demonstrating practical decryption techniques and the weaknesses of simple substitution ciphers in modern computing.
# 

# # Problem Description 
# 
# The encryption is made by simply permuting or "rotating" or "shifting" the positions of the letters of the alphabet by a certain number. For example, if you rotate the alphabet by 6, you have the following encryption:
# 
# Plain:    abcdefghijklmnopqrstuvwxyz
# Cipher:   ghijklmnopqrstuvwxyzabcdef
# Then a message is encrypted as follows:
# 
# Plaintext:  the quick brown fox jumps over the lazy dog
# Ciphertext: znk waoiq hxuct lud pasvy ubkx znk rgfe jum
# 
# Given the following encrypted message by a Caesar cipher, we want to:
# 
#   Decrypt it by brute-forcing all possible shifts (0–25)  
#   Identify the shift where the decrypted message contains the keyword `pumpkin`  
#   Print the decrypted message and the shift used
# 
# Encrypted message: 
# 
# ghofhlpmlrfmwbulmcifldiadywblhvwglaomlgssalkswfrlpihlwhlwglhvslcbzmlkomlhvsgslqccywsglkwzzlpoysldfcdsfzmlobrlbchlhifblcihlqoysmlgdfsorlmcifldiadywblcbloldzohslobrldzoqsloldodsflhckszlcjsflhvslhcdlzwuvhzmldfsgglhclopgcfplhvslzweiwrlfsdsohlhvslghsdlohl
# zsoghltciflacfslhwasglgshlogwrslwblolgaozzlpckzlkvwgylhcushvsflhvsltzcifldiadywbldwslgdwqslpoywbulgcrolpoywbuldckrsflobrlgozhlgshlogwrslwblolzofuslpckzlqfsoalhvslgcthsbsrlpihhsflobrlpfckblgiuoflhcushvsflkwhvloblszsqhfwqlawlsflorrlwblhvslsuulmczygl
# obrljobwzzolobrlawlltcflcbslawbihslibhwzldozslobrltzittmlorrlwblhvsldiadywblobrlqcapwbslawllwblhvslrfmlwbufsrwsbhglgqccdlhvslrciuvlwbhclswuvhssblpozzglobrlfczzlhvsalwblhvslgdwqsrlgiuoflpoyslhvslqccywsglobrlhvsblzshlqcczlgzwuvhzmlpstcfslsbxcmwbu

# # Setup and Cipher Definition

# In[1]:


# Define the alphabet list
alphabet = list("abcdefghijklmnopqrstuvwxyz")

# Prepare the encoded message as a string
cipher = (
    'ghofhlpmlrfmwbulmcifldiadywblhvwglaomlgssalkswfrlpihlwhlwglhvslcbzmlkomlhvsgslqccywsglkwzzlpoysldfcdsfzmlobrlbchlhifblcihlqoysmlgdfsorlmcifldiadywblcbloldzohslobrldzoqsloldodsflhckszlcjsflhvslhcdlzwuvhzmldfsgglhclopgcfplhvslzweiwrlfsdsohlhvslghsdlohlzsoghltciflacfslhwasglgshlogwrslwblolgaozzlpckzlkvwgylhcushvsflhvsltzcifldiadywbldwslgdwqslpoywbulgcrolpoywbuldckrsflobrlgozhlgshlogwrslwblolzofuslpckzlqfsoalhvslgcthsbsrlpihhsflobrlpfckblgiuoflhcushvsflkwhvloblszsqhfwqlawlsflorrlwblhvslsuulmczyglobrljobwzzolobrlawlltcflcbslawbihslibhwzldozslobrltzittmlorrlwblhvsldiadywblobrlqcapwbslawllwblhvslrfmlwbufsrwsbhglgqccdlhvslrciuvlwbhclswuvhssblpozzglobrlfczzlhvsalwblhvslgdwqsrlgiuoflpoyslhvslqccywsglobrlhvsblzshlqcczlgzwuvhzmlpstcfslsbxcmwbu'
)


# # Define Decryption Function

# In[2]:


# Define your function here
def decrypt_caesarcipher_with_key(cipher, keyword="pumpkin"):
    # Defining the function for decrypting a single letter. The 'decryption_letter' function below takes care of individual letter decryption. It is a nested function with arguements letter & shift. 
    def decryption_letter(letter, shift):
        # Here we use the 'isalpha()' method to confirm the letter is alphabetic
        if letter.isalpha():
            # The ord() method is used for obtaining the unicode code point of the letter. From that we substract the shift value to get the decrypted letter
            shifted = ord(letter) - shift
            if letter.islower():
              # If a shifted value goes beyond Z or above A, we use shifted +=26 to ensure that there is a wrap around and the outcome is a alphabetic letter.
                if shifted < ord('a'):
                    shifted += 26
            elif letter.isupper():
                if shifted < ord('A'):
                    shifted += 26
                    # If the character is alphabetic, convert the shifted Unicode code point back to a letter using chr() and return it. 
            return chr(shifted)
        return letter  # Return the character unchanged if it's not alphabetic

    # The Caesar cipher has 26 possible shifts (one for each letter). We evaluate all of them to find the appropriate decryption
    # The decryption_letter function is applied on each letter in the cipher. The letters are then joined together in a string
    
    def shift_with_key(cipher, keyword):
        for shift in range(26):
            decrypted_text = ''.join([decryption_letter(char, shift) for char in cipher])
            if keyword in decrypted_text:
                return decrypted_text, shift
        return None, None  # Return None if keyword not found in any shifted text

    decrypted_text, shift_used = shift_with_key(cipher, keyword)
    print(decrypted_text)
    return shift_used


# # Run the Decryption

# In[3]:


# Call the function and print the shift used
shift_used = decrypt_caesarcipher_with_key(cipher, 'pumpkin')
print("\nShift used:", shift_used)


# # Summary 

# ## Summary of Results
# 
#   The Caesar cipher was successfully broken using a brute-force approach.  
#   The function identified the correct shift and decrypted the message containing the keyword `pumpkin`.
# 
# | Result        | Value    |
# |---------------|----------|
# | Shift used    | 14       |
# | Keyword found | pumpkin  |
# 
# This exercise demonstrates why simple ciphers like Caesar are not secure by modern standards —  they can be broken easily using basic brute-force methods, even without knowing the shift in advance.
# 

# In[ ]:




