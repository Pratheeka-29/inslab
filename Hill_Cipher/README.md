 ##Hill Cipher 

## Introduction
The **Hill Cipher** is a polygraphic substitution cipher that encrypts plaintext in blocks using matrix multiplication. This encryption algorithm is based on linear algebra and is a classical method of cryptography. It is commonly used to encrypt text by transforming it into a more complex form using a key matrix.

## Features of the Script
This Python script provides a simple implementation of the Hill Cipher with the following features:

- Encrypts plaintext using the **Hill Cipher** algorithm with a user-defined key matrix.
- Converts all input text to uppercase, ensuring case insensitivity.
- Pads the plaintext with the letter "X" when necessary to ensure the length of the text matches the block size of the key matrix.
- Efficiently handles plaintext in blocks for accurate and systematic encryption.

## How the Hill Cipher Works
The **Hill Cipher** uses a square matrix (e.g., 2x2, 3x3) as the key for encryption. The core concept relies on the matrix multiplication of plaintext blocks and the key matrix. Here's a breakdown of the encryption process:

1. **Key Matrix**: A square matrix is used as the encryption key. The matrix should be invertible modulo 26 for decryption to be possible.
2. **Padding**: If the length of the plaintext is not divisible by the size of the key matrix, the plaintext is padded with "X" characters to ensure compatibility.
3. **Encryption**:
   - Convert each letter in the plaintext to a corresponding number (A=0, B=1, ..., Z=25).
   - Split the plaintext into blocks based on the size of the key matrix.
   - Multiply each block by the key matrix (using modulo 26 arithmetic) to generate the ciphertext.
   - Convert the resulting numeric values back to letters.

## Step-by-Step Instructions

### 1. Prerequisites
To run the Hill Cipher code, you will need **Python 3.x** and the **NumPy** library. If you don't have NumPy installed, you can install it using the following command:
pip install numpy


### 2. Clone the Repository
Clone this repository to your local machine using the following command:
git clone https://github.com/Pratheeka-29/inslab.git


### 3. Navigate to the Project Folder
Once cloned, move to the project directory:
cd inslab


### 4. Running the Script
Run the Hill Cipher encryption script by executing the following command:
python hill_cipher.py


### 5. Enter Input for Encryption
When prompted, input the plaintext and the key matrix. The script will perform the encryption and display the resulting ciphertext.

## Example Run

### Input:
Enter the plaintext: HELLO
Enter the key matrix: [[6,24,1],[13,16,10],[20,17,15]]

### Output:

Encrypted: TFJJZX

## Code Explanation
### `hill_cipher_encrypt(plaintext, key)`
This is the core function of the script. It performs the following tasks:
- Converts the plaintext to uppercase and removes any spaces.
- If necessary, pads the plaintext with "X" characters to make its length a multiple of the matrix size.
- Encrypts the text by multiplying the plaintext vector by the key matrix using modular arithmetic (mod 26).
- Returns the resulting ciphertext as a string of uppercase letters.

## Customizing the Cipher
- **Key Matrix**: You can modify the key matrix to customize the encryption process. Ensure that the matrix is invertible in modulo 26 for encryption and decryption to work properly.
- **Plaintext**: You can adjust the plaintext as needed. The script automatically handles padding if the plaintext length is not divisible by the size of the key matrix.
- **Decryption**: To implement decryption, you would need to calculate the inverse of the key matrix in modulo 26 and apply it to the ciphertext.

## Requirements
- Python 3.x
- NumPy Library: Install using `pip install numpy`

## Run the Code Online

You can also run the Hill Cipher code directly in your browser using the following link on **OnlineGDB**.

### Click the link to run the code:
https://onlinegdb.com/BOS_As6Si

By clicking on the link, you can run the code, input your plaintext and key matrix, and observe the encryption process live.


## Conclusion
The Hill Cipher offers a powerful and flexible method for encrypting text based on matrix operations. While it is not secure by modern standards, it provides an excellent introduction to cryptography and matrix-based encryption methods. This script serves as a simple but effective example of how matrix multiplication can be used for text encryption.



