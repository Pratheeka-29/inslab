```markdown
# Vigenère Cipher

## Introduction
The **Vigenère Cipher** is a method of encrypting alphabetic text by using a series of different Caesar ciphers based on the letters of a keyword. It is a type of **polyalphabetic substitution cipher**, which means it uses multiple shifts based on the characters of a key, making it more secure than the Caesar cipher. In this script, the Vigenère Cipher is implemented with both encryption and decryption functionalities.

## Features of the Script
This Python script provides an easy-to-understand implementation of the **Vigenère Cipher**. The key features include:

- **Encryption**: Encrypts the input text by shifting each letter according to a key.
- **Decryption**: Decrypts the encrypted text by reversing the shift using the same key.
- Handles both **uppercase** and **lowercase** letters, while preserving non-alphabetical characters (such as spaces, punctuation, etc.).
- Allows dynamic input for both **plaintext** and **key**, and lets the user choose between **encryption** and **decryption** modes.

## How the Vigenère Cipher Works
The **Vigenère Cipher** works by using a key to determine the shift for each character in the plaintext. Each character in the text is shifted based on the corresponding character in the key. The cipher operates by shifting each letter in the plaintext by the number of positions defined by the corresponding key letter. If the key is shorter than the text, it repeats.

### 1. **Encryption**:
   - Each letter in the plaintext is shifted forward by a number of positions determined by the corresponding letter in the key.
   - The shift direction is forward (positive) for encryption.
   - Non-alphabetic characters remain unchanged during encryption.

### 2. **Decryption**:
   - The decryption process is the reverse of encryption, with the shift direction being backward (negative).
   - The same key is used, and the corresponding shifts are applied to reverse the encryption.

### 3. **Non-Alphabet Characters**:
   - Non-alphabetic characters (e.g., spaces, punctuation) are preserved and do not undergo any transformation during both encryption and decryption.

## Step-by-Step Instructions

### 1. Prerequisites
To run the Vigenère Cipher code, you need **Python 3.x** installed on your system. There are no additional libraries required for this script as it uses basic Python functionality.

### 2. Clone the Repository (Optional)
If you'd like to clone this repository to your local machine, use the following command:

```bash
git clone https://github.com/Pratheeka-29/vigenere-cipher.git
```

### 3. Navigate to the Project Folder (Optional)
If you cloned the repository, move to the project directory:

```bash
cd vigenere-cipher
```

### 4. Running the Script
To run the Vigenère Cipher encryption and decryption script, simply run:

```bash
python vigenere_cipher.py
```

### 5. Enter Input for Encryption
When prompted, enter the **plaintext** (the text you want to encrypt or decrypt) and the **key** (a string of your choice). The script will display the encrypted result and then automatically decrypt it.

## Example Run

### Input for Encryption:
```bash
Enter the text: HELLO
Enter the key: KEY
Enter mode: encrypt
```

### Output (Encryption):
```bash
Encrypted: RIJVS
```

### Input for Decryption:
```bash
Enter the text: RIJVS
Enter the key: KEY
Enter mode: decrypt
```

### Output (Decryption):
```bash
Decrypted: HELLO
```

## Code Explanation

### `vigenere_cipher(text, key, mode="encrypt")`
This function implements the Vigenère cipher for both encryption and decryption:
- **Encryption**: For each character in the plaintext, the shift is calculated using the corresponding character in the key. The key is repeated if it is shorter than the text.
- **Decryption**: The shift direction is reversed (shift is negative for decryption).
- Non-alphabetic characters are not changed.

## Customizing the Cipher
- **Key**: You can modify the key to customize the encryption and decryption process. The key should be a meaningful string, ideally of a similar length to the plaintext to ensure maximum security.
- **Text**: The script handles both uppercase and lowercase letters, as well as non-alphabetic characters (spaces, punctuation).

## Requirements
- Python 3.x

## Run the Code Online

You can also run the Vigenère Cipher code directly in your browser using the following link on **OnlineGDB**.

### Click the link to run the code:
[https://onlinegdb.com/5AoeL72nPa]

By clicking on the link, you can run the code, input your text and key, and observe both the encryption and decryption process live.

---

## Conclusion
The Vigenère Cipher is a powerful encryption method that is more secure than simpler ciphers like the Caesar Cipher. It utilizes a series of Caesar ciphers based on a keyword, offering more complexity and resistance to frequency analysis. This script provides both encryption and decryption functionalities, allowing you to experiment with different keys and texts for a deeper understanding of how polyalphabetic ciphers work.
```