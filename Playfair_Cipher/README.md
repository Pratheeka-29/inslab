
```markdown
# Playfair Cipher

## Introduction
The **Playfair Cipher** is a classical encryption technique that encrypts pairs of letters in the plaintext using a 5x5 matrix. It is a digraph cipher, meaning it encrypts pairs of letters at a time, unlike simple substitution ciphers that encrypt one letter at a time. The Playfair Cipher was one of the first digraph ciphers and is known for its complexity and relatively stronger security than monoalphabetic substitution ciphers.

## Features of the Script
This Python script implements the **Playfair Cipher** with encryption functionality. The key features include:

- **Encryption**: Encrypts the input text by dividing the plaintext into digraphs (pairs of letters) and encrypting them using a key matrix.
- Handles both **uppercase** and **lowercase** letters, converting all input text to uppercase and replacing 'J' with 'I'.
- Adds padding ('X') to the plaintext if the length of the text is odd, ensuring that each pair of letters is processed.
- Preserves non-alphabetical characters (such as spaces) during encryption.

## How the Playfair Cipher Works
The **Playfair Cipher** works by first creating a 5x5 matrix of letters from a key and then using this matrix to encrypt pairs of letters from the plaintext. The cipher encrypts pairs of letters based on their positions in the matrix.

### 1. **Encryption**:
   - The key is used to create a 5x5 matrix, with each letter of the alphabet (excluding 'J') placed in it.
   - The plaintext is processed in pairs (digraphs). If the length of the plaintext is odd, an 'X' is added at the end.
   - Depending on the positions of the two letters in the matrix:
     - If both letters are in the same row, each letter is replaced by the letter to its immediate right (wrapping around if necessary).
     - If both letters are in the same column, each letter is replaced by the letter immediately below it (wrapping around if necessary).
     - If the letters are not in the same row or column, they form a rectangle, and each letter is replaced by the letter in its row and the other letter's column.

### 2. **Handling Padding**:
   - If there is a pair of identical letters (e.g., "LL"), the letter 'X' is inserted between them to break the pair.

### 3. **Key Matrix**:
   - The matrix is created from the key, where all duplicate letters are removed, and the remaining letters of the alphabet are placed in the matrix. The letter 'J' is replaced with 'I' to fit the 25-character requirement.

## Step-by-Step Instructions

### 1. Prerequisites
To run the Playfair Cipher code, you will need **Python 3.x** installed on your system. There are no additional libraries required for this script as it uses basic Python functionality.

### 2. Clone the Repository (Optional)
If you want to clone this repository to your local machine, use the following command:

```bash
git clone https://github.com/Pratheeka-29/playfair-cipher.git
```

### 3. Navigate to the Project Folder (Optional)
Once cloned, navigate to the project directory:

```bash
cd playfair-cipher
```

### 4. Running the Script
To run the Playfair Cipher encryption script, use the following command:

```bash
python playfair_cipher.py
```

### 5. Enter Input for Encryption
When prompted, enter the **plaintext** to be encrypted and the **key** used to generate the cipher matrix.

### Example Input:
```bash
Enter the plaintext: HELLO
Enter the key: KEYWORD
```

### Example Output:
```bash
Encrypted: BIPULX
```

## Code Explanation

### `create_playfair_matrix(key)`
This function creates a 5x5 matrix from the given key:
- The key is converted to uppercase, with any duplicate letters removed.
- The matrix is filled with the key letters, followed by the remaining unused letters of the alphabet (excluding 'J').

### `find_position(matrix, char)`
This function finds the position (row and column) of a character in the 5x5 matrix.

### `playfair_encrypt(plaintext, key)`
This is the core function for encrypting the plaintext:
- It creates the key matrix using the provided key.
- It processes the plaintext into digraphs, adding padding ('X') if necessary.
- It then encrypts the digraphs based on their positions in the matrix, following the Playfair Cipher rules.

## Customizing the Cipher
- **Key**: You can modify the key to customize the encryption process. The key determines the characters in the 5x5 matrix.
- **Plaintext**: You can adjust the plaintext as needed. The script automatically handles converting it to uppercase and removing spaces.

## Requirements
- **Python 3.x** (No additional libraries required)

## Run the Code Online

You can also run the Playfair Cipher code directly in your browser using the following link on **OnlineGDB**:

### Click the link to run the code:
[https://onlinegdb.com/0bJcJEpcj]

By clicking the link, you can run the code, input your plaintext and key, and observe the encryption process in action.

---

## Conclusion
The **Playfair Cipher** offers a more complex and secure method of encryption compared to simpler ciphers like the Caesar Cipher. While it is not as secure by modern standards, it provides a valuable introduction to digraph ciphers and matrix-based encryption methods. This script demonstrates how the Playfair Cipher can be used to encrypt plaintext based on a keyword, providing a practical example of this historical encryption technique.
```
