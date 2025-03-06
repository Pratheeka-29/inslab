
```markdown
# Monoalphabetic Cipher

## Introduction
The **Monoalphabetic Cipher** is a simple substitution cipher in which each letter in the plaintext is replaced by another letter of the alphabet. The mapping between the letters of the alphabet is one-to-one, meaning each letter is substituted by a unique corresponding letter. In this case, the cipher uses a custom substitution key to encrypt and decrypt the text.

## Features of the Script
This Python script implements the **Monoalphabetic Cipher** with both encryption and decryption functionalities. The key features include:

- **Encryption**: Encrypts the input text by substituting each letter in the plaintext with a corresponding letter from a predefined cipher key.
- **Decryption**: Reverses the encryption by mapping the cipher letters back to the original plaintext letters.
- Handles both **uppercase** and **lowercase** letters, preserving non-alphabetical characters (such as spaces and punctuation).
- The script prompts the user to input the **text** for encryption and decryption dynamically.

## How the Monoalphabetic Cipher Works
The **Monoalphabetic Cipher** uses a substitution method where each letter in the plaintext is replaced by a corresponding letter from a custom cipher key. The alphabet is mapped to a custom cipher for encryption and decryption.

### 1. **Encryption**:
   - Each letter in the plaintext is replaced by a letter from the cipher string.
   - The plaintext is first converted to lowercase for uniformity.
   - Non-alphabetic characters (spaces, punctuation, etc.) are left unchanged.

### 2. **Decryption**:
   - Decryption reverses the substitution by mapping each letter in the encrypted text back to its corresponding letter in the plaintext.
   - Non-alphabetic characters are preserved in the decrypted text.

## Step-by-Step Instructions

### 1. Prerequisites
To run the Monoalphabetic Cipher code, you will need **Python 3.x** installed on your system. There are no additional libraries required for this script as it uses basic Python functionality.

### 2. Clone the Repository (Optional)
If you want to clone this repository to your local machine, use the following command:

```bash
git clone https://github.com/YourUsername/monoalphabetic-cipher.git
```

### 3. Navigate to the Project Folder (Optional)
Once cloned, move into the project directory:

```bash
cd monoalphabetic-cipher
```

### 4. Running the Script
To run the Monoalphabetic Cipher encryption and decryption script, use the following command:

```bash
python monoalphabetic_cipher.py
```

### 5. Enter Input for Encryption
When prompted, enter the **text** you want to encrypt or decrypt. The script will process the text and display both the encrypted and decrypted results.

## Example Run

### Input for Encryption:
```bash
Enter the string of your choice: hello world
```

### Output (Encryption):
```bash
Encrypted text: itssg vgksr
```

### Input for Decryption:
```bash
Enter the string of your choice: itssg vgksr
```

### Output (Decryption):
```bash
Decrypted text: hello world
```

## Code Explanation

### `encrypt(text)`
This function encrypts the given text by replacing each letter with its corresponding letter from the **Monoalphabetic** cipher:
- It converts the text to lowercase for uniformity.
- It checks each character: if it's a letter, it replaces it with the letter from the cipher.
- Non-alphabet characters (e.g., spaces, punctuation) are added to the result unchanged.

### `decrypt(text)`
This function decrypts the encrypted text by reversing the substitution cipher:
- It replaces each letter from the cipher string with the corresponding letter from the plain alphabet.
- Non-alphabet characters are preserved in the decrypted text.

## Customizing the Cipher
- **Cipher Key**: The cipher key used for substitution can be customized. Currently, the cipher key is `'qwertyuiopasdfghjklzxcvbnm'`. You can modify this key to change the encryption scheme, but make sure the length matches the alphabet (26 characters).
- **Text**: The script processes both lowercase and uppercase input text.

## Requirements
- **Python 3.x** (No additional libraries required)

## Run the Code Online

You can also run the **Monoalphabetic Cipher** code directly in your browser using the following link on **OnlineGDB**:

### Click the link to run the code:
[]

By clicking the link, you can run the code, input your text, and observe both the encryption and decryption processes in action.

---

## Conclusion
The Monoalphabetic Cipher offers a straightforward and easy-to-understand method for encrypting and decrypting text using a custom cipher key. Although this cipher is not secure by modern standards, it provides an excellent introduction to basic encryption techniques. This script demonstrates how to implement a substitution cipher with both encryption and decryption capabilities.
```


