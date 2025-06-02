# classical-ciphers-decryption
Python implementations for breaking classical ciphers: Caesar cipher and Vigenère cipher, using brute-force techniques and keyword search.
This repository contains two Python Jupyter Notebooks demonstrating how to break two famous classical ciphers:
- The **Caesar cipher** (rotation/shift cipher)
- The **Vigenère cipher** (polyalphabetic substitution cipher)

Both projects use brute-force or keyword search strategies to decrypt encrypted messages and reveal their hidden contents.

---

## Files

| File                                  | Description                                                           |
|---------------------------------------|-----------------------------------------------------------------------|
| `caesar_cipher_decryption.ipynb`      | Decrypts a message encrypted with an unknown Caesar shift by brute force, identifying the correct shift based on the presence of the word `pumpkin`. |
| `vigenere_cipher_decryption.ipynb`    | Decrypts a message encrypted with a Vigenère cipher using a four-letter keyword, recovering the keyword by searching for the word `gingerbread`. |

---

## Project Overview

These notebooks were created as part of a cryptography exercise to demonstrate how easily classical encryption methods can be broken using modern computation.

### Caesar Cipher Decryption
- Brute-forces all 26 possible shifts.
- Detects the correct decryption by searching for a known keyword in the plaintext.

###  Vigenère Cipher Decryption
- Deduces the four-letter keyword by sliding a known plaintext (`gingerbread`) over the ciphertext.
- Decrypts the full message once the correct key is identified.

---

##  How to Use

1. Clone or download the repository.
2. Open the `.ipynb` files in Jupyter Notebook or Jupyter Lab.
3. Run all cells to reproduce the decryption steps and view results.

---

##  License

This repository is provided for educational and demonstration purposes.
