
```markdown
# Feistel Cipher

## Introduction
The **Feistel Cipher** is a symmetric encryption algorithm that applies a series of transformations to the input data, breaking it into two halves and applying a series of rounds using a key. It is widely used in cryptographic algorithms such as the **DES (Data Encryption Standard)**. In this script, the Feistel cipher operates on the binary representation of a string, combining basic operations like XOR and binary addition.

## Features of the Script
This Python script provides an implementation of the **Feistel Cipher** with both encryption and decryption functionalities. The features include:

- **Encryption**: Encrypts the input string by applying the Feistel network to the binary representation of the input string and a key.
- **Decryption**: Decrypts the encrypted text by reversing the operations applied during encryption.
- Handles both **uppercase** and **lowercase** letters, while preserving non-alphabetical characters (such as spaces and punctuation).
- The script allows dynamic input for both the **plaintext** and the **key**.

## How the Feistel Cipher Works
The **Feistel Cipher** works by splitting the plaintext into two halves and repeatedly applying a round function that involves binary operations. The Feistel network follows a symmetric structure, meaning that the encryption and decryption processes are similar, but the rounds are applied in reverse order during decryption.

### 1. **Encryption**:
   - The plaintext string is first converted into its binary representation.
   - The binary string is divided into two halves.
   - A key is used to modify the right half in each round, combining it with the left half using XOR and binary addition operations.
   - The final ciphertext is obtained after several rounds of these transformations.

### 2. **Decryption**:
   - The decryption process reverses the operations applied during encryption, using the same key.
   - The binary string is split again, and the transformations are applied in reverse order to recover the original plaintext.

### 3. **Non-Alphabet Characters**:
   - Characters that are not part of the alphabet (e.g., spaces, punctuation) are preserved in the final result during both encryption and decryption.

## Step-by-Step Instructions

### 1. Prerequisites
To run the Feistel Cipher code, you need **Python 3.x** installed on your system. There are no additional libraries required for this script as it uses basic Python functionality.

### 2. Clone the Repository (Optional)
If you want to clone this repository to your local machine, use the following command:

```bash
git clone https://github.com/Pratheeka-29/feistel-cipher.git
```

### 3. Navigate to the Project Folder (Optional)
If you cloned the repository, move to the project directory:

```bash
cd feistel-cipher
```

### 4. Running the Script
To run the Feistel Cipher encryption and decryption script, simply run:

```bash
python feistel_cipher.py
```

### 5. Enter Input for Encryption
When prompted, enter the **plaintext** (the text you want to encrypt) and the **key** (a string of your choice). The script will display the encrypted result and then automatically decrypt it.

## Example Run

### Input for Encryption:
```bash
Enter a string: HELLO
Enter a key: KEY
```

### Output (Encryption):
```bash
Encrypted: 1101100110110001100110001100100011110001111011111100110111000111
```

### Output (Decryption):
```bash
Decrypted: HELLO
```

## Code Explanation

### `create_playfair_matrix(key)`
This function creates the 5x5 matrix used in the cipher, based on the provided key. It removes duplicate characters and treats 'J' as 'I'.

### `find_position(matrix, char)`
This function finds the position (row, column) of a given character in the matrix.

### `playfair_encrypt(plaintext, key)`
This function performs the encryption of the input plaintext using the Feistel cipher algorithm:
- It first converts the plaintext into binary.
- Then it applies the round function using the key.
- The result is the final ciphertext in binary form.

## Customizing the Cipher
- **Key**: You can modify the key to customize the encryption and decryption process. Ensure that the key is a meaningful string.
- **Text**: The script handles both uppercase and lowercase letters, converting them to binary representation for processing.

## Requirements
- Python 3.x

## Run the Code Online

You can also run the Feistel Cipher code directly in your browser using the following link on **OnlineGDB**.

### Click the link to run the code:
[https://onlinegdb.com/HM9QEBVlw]

By clicking on the link, you can run the code, input your text and key, and observe the encryption and decryption process live.

---

## Conclusion
The Feistel Cipher is a symmetric key cipher that is widely used in cryptographic algorithms. This script demonstrates the encryption and decryption process using binary operations in a Feistel network, giving a good understanding of the basics of symmetric encryption. While not as widely used today in its original form, it is an essential concept in the study of cryptography.

```


