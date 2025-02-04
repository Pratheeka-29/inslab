---

# **Hill Cipher Encryption in Python**

## **Overview**
This Python script implements the **Hill Cipher**, a polygraphic substitution cipher that encrypts blocks of plaintext letters using matrix multiplication. The Hill cipher leverages linear algebra concepts, making it a classical method for encrypting alphabetic text in cryptography.

## **Features**
- ✅ Encrypts plaintext using the **Hill Cipher** algorithm with a specified key matrix.
- ✅ Handles case insensitivity by converting all input to uppercase.
- ✅ Automatically pads the plaintext with "X" to match the matrix size if necessary.
- ✅ Efficiently processes plaintext in blocks, ensuring accurate encryption.

## **How to Run the Code**

### **1. Prerequisites**
Ensure you have **Python 3.x** and **NumPy** installed. You can install NumPy using pip:
```bash
pip install numpy
```

### **2. Clone the Repository**
Clone this repository to your local machine:
```bash
git clone https://github.com/Pratheeka-29/inslab.git
```

### **3. Navigate to the Project Folder**
Move to the project directory:
```bash
cd inslab
```

### **4. Run the Code**
To run the Hill Cipher encryption script:
```bash
python hill_cipher.py
```

## **How It Works**
- **Key Matrix**: A square matrix (e.g., 2x2, 3x3) is used as the encryption key. The matrix should be invertible in modulo 26 arithmetic for decryption.
- **Padding**: If the plaintext length is not a multiple of the matrix size, it is padded with "X" to fit the required block size.
- **Encryption Process**:
  - Convert each letter to its corresponding number (A=0, B=1, ..., Z=25).
  - Split the plaintext into blocks based on the size of the key matrix.
  - Multiply each block by the key matrix (mod 26) to generate the ciphertext.
  - Convert the resulting numbers back into letters.

## **Example Execution**

### **Input:**
```bash
Enter the plaintext: HELLO
Enter the key matrix: [[6,24,1],[13,16,10],[20,17,15]]
```

### **Output:**
```bash
Encrypted: EQNVZ
```

## **Code Explanation**

### **Functions**
1. `hill_cipher_encrypt(plaintext, key)`:
   - Converts plaintext to uppercase and removes spaces.
   - Pads plaintext with "X" to match the key matrix size.
   - Encrypts the plaintext by multiplying the plaintext vector by the key matrix.
   - Returns the ciphertext as an uppercase string.

## **Customization**
- Modify the `key` matrix to change the encryption. Ensure that the matrix is invertible in modulo 26 for proper encryption and potential decryption.
- Adjust the plaintext as needed; the script will handle padding automatically.
- To add decryption, implement matrix inversion in modular arithmetic and apply it to the ciphertext.

## **Requirements**
- **Python 3.x**
- **NumPy Library**: Install via `pip install numpy`

## **Additional Information**
The Hill cipher can be extended to include decryption by calculating the inverse of the key matrix in modular arithmetic. Additionally, users can experiment with different key sizes, provided they maintain square matrices for valid encryption.

---

