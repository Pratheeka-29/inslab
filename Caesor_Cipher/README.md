
```markdown
# Caesar Cipher

## Introduction
The **Caesar Cipher** is one of the simplest and most widely known encryption techniques. It is a substitution cipher where each letter in the plaintext is shifted by a certain number of positions in the alphabet. This method is historically significant, and it provides a great introduction to basic encryption techniques.

## Features of the Script
This Python script provides an easy-to-understand implementation of the **Caesar Cipher** with both encryption and decryption functionalities. The features include:

- **Encryption**: Encrypts the input text by shifting each letter in the plaintext by a user-defined number.
- **Decryption**: Decrypts the encrypted text by reversing the shift applied during encryption.
- Handles both **uppercase** and **lowercase** letters, while preserving non-alphabetical characters (such as spaces, punctuation, etc.).
- The script allows for dynamic input, asking for the **text** and **shift** from the user.

## How the Caesar Cipher Works
The Caesar Cipher works by shifting each letter in the plaintext by a specified number of positions down or up the alphabet.

1. **Encryption**:
   - Each letter in the plaintext is replaced by a letter some fixed number of positions down the alphabet.
   - If the letter is an uppercase letter (A-Z), it shifts within the uppercase alphabet. Similarly, lowercase letters (a-z) shift within the lowercase alphabet.
   
2. **Decryption**:
   - Decryption reverses the encryption process by shifting each letter in the encrypted text backward by the same number of positions as used during encryption.
   
3. **Non-Alphabet Characters**:
   - Characters that are not part of the alphabet (e.g., spaces, punctuation) remain unchanged during both encryption and decryption.

## Step-by-Step Instructions

### 1. Prerequisites
To run the Caesar Cipher code, you need **Python 3.x** installed on your system. There are no additional libraries required for this script as it uses basic Python functionality.

### 2. Clone the Repository (Optional)
If you'd like to clone this repository to your local machine, you can do so using the following command:

```bash
git clone https://github.com/YourUsername/caesar-cipher.git
```

### 3. Navigate to the Project Folder (Optional)
If you cloned the repository, move to the project directory:

```bash
cd caesar-cipher
```

### 4. Running the Script
To run the Caesar Cipher encryption and decryption script, simply run:

```bash
python caesar_cipher.py
```

### 5. Enter Input for Encryption
When prompted, enter the **text** you want to encrypt or decrypt and the **shift value** (an integer). The script will display both the encrypted and decrypted results.

## Example Run

### Input for Encryption:
```bash
Enter the text: HELLO
Enter the shift: 3
```

### Output (Encryption):
```bash
Encrypted: KHOOR
```

### Input for Decryption:
```bash
Enter the text: KHOOR
Enter the shift: 3
```

### Output (Decryption):
```bash
Decrypted: HELLO
```

## Code Explanation

### `caesar_cipher_encryption(text, shift)`
This function encrypts the given text by shifting each letter forward by the specified number of positions (shift value):
- It checks if each character is an alphabet letter (A-Z or a-z).
- If the character is a letter, it applies the shift and wraps around the alphabet using modulo arithmetic (`% 26`).
- Non-alphabetic characters (e.g., spaces, punctuation) are added to the result without modification.

### `caesar_cipher_decryption(encryption, shift)`
This function decrypts the encrypted text by shifting each letter backward by the specified number of positions:
- Similar to the encryption process, but the shift is reversed (subtracted instead of added).
- Non-alphabetic characters are unchanged.

## Customizing the Cipher
- **Shift Value**: You can change the shift value to customize the encryption and decryption. Positive values shift to the right (forward), while negative values shift to the left (backward).
- **Text**: The script handles both uppercase and lowercase letters, along with spaces and punctuation.

## Requirements
- Python 3.x

## Run the Code Online

You can also run the Caesar Cipher code directly in your browser using the following link on **OnlineGDB**.

### Click the link to run the code:
[https://onlinegdb.com/BOS_As6Si]

By clicking on the link, you can run the code, input your text and shift value, and observe both the encryption and decryption process live.

---

## Conclusion
The Caesar Cipher is a simple yet effective encryption method that helps demonstrate the fundamentals of cryptography. While it is not secure by modern standards, it is a great introductory algorithm to learn and implement. This script provides both encryption and decryption capabilities for better understanding of how shift-based ciphers work.
```

