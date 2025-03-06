```markdown
# DES (Data Encryption Standard)

## Introduction
The **Data Encryption Standard (DES)** is a symmetric-key block cipher that was widely used for data encryption in the 1970s through the 1990s. It operates on 64-bit blocks of data and uses a 56-bit key to encrypt and decrypt the data. In this Python script, we implement a simplified version of the **DES algorithm** to generate encryption keys through bitwise operations and transformations. This implementation focuses on the key generation process, which is a crucial step in the DES algorithm.

## Features of the Script
This Python script provides a basic implementation of the **key generation process** for the **DES algorithm**. The features include:

- **Input**: Accepts a string of plaintext.
- **Key Generation**: Generates 8 different encryption keys based on bitwise transformations and random selections.
- Handles **binary data transformations** to create the DES keys.
- **Randomization**: Selects random bits to generate each round key.

## How DES Key Generation Works
The key generation process in DES involves multiple transformations and permutations on the input string (converted to binary). This script demonstrates how a **left-right split** and specific shifts are applied to generate different keys for each round of encryption. Below is a breakdown of the key steps:

### 1. **Input Processing**:
   - The input string is converted into its binary representation.
   
### 2. **Left-Right Split**:
   - The binary string is split into two halves: **left** and **right**.
   
### 3. **Left Shifts**:
   - A series of bit shifts are applied to both halves of the string. The shifts are defined by the `lt` list.
   
### 4. **Key Permutation**:
   - A permutation is applied to the left and right parts of the string after shifting, and random bit positions are selected to form the final key.
   
### 5. **Randomization**:
   - Random positions are selected to form the keys for each round, ensuring the diversity of encryption keys.

### 6. **Key Output**:
   - After generating the keys, the script prints out the 8 keys, each of which is used in different rounds of the DES encryption process.

## Step-by-Step Instructions

### 1. Prerequisites
To run the DES key generation code, you need **Python 3.x** installed on your system. There are no additional libraries required for this script, as it uses basic Python functionality.

### 2. Clone the Repository (Optional)
If you'd like to clone this repository to your local machine, use the following command:

```bash
git clone https://github.com/Pratheeka-29/des-key-generation.git
```

### 3. Navigate to the Project Folder (Optional)
If you cloned the repository, move to the project directory:

```bash
cd des-key-generation
```

### 4. Running the Script
To run the DES key generation script, simply run:

```bash
python des_key_gen.py
```

### 5. Enter Input
When prompted, enter the **plaintext string**. The script will generate and display the 8 round keys used for the DES algorithm.

## Example Run

### Input:
```bash
Enter a string: HELLO
```

### Output (Keys Generation):
```bash
key 1  =  010110010011010000110001010110101011011111100000
key 2  =  011101011101010010111100110010110101101000110000
key 3  =  011101010101101101010111100010101101110100100000
key 4  =  011010001100110010011000101010101010010000110000
key 5  =  010100010110110011100110101110110100111110110000
key 6  =  011101011101101101011011011000101101111101100000
key 7  =  010101100110111110110011001100100100100110100000
key 8  =  010010001101110000110011010110111101010010110000
```

## Code Explanation

### Key Generation Steps:

1. **Binary Conversion**:
   The input string is converted to binary using `format(ord(i),'08b')`, which converts each character into its 8-bit binary representation.
   
2. **Left-Right Split**:
   The binary string is split into two equal halves. The left half undergoes bitwise shifts based on the values in the `lt` list.

3. **Left Shifts and Permutations**:
   Shifting and permutation operations are performed on the left and right halves to generate different keys for each round.

4. **Randomization**:
   The permutation of keys involves selecting random positions and constructing the round keys by excluding selected positions.

5. **Key Output**:
   The script outputs 8 different keys, each used in a round of DES encryption.

## Customizing the DES Key Generation

- **Input String**: You can change the string that is input to generate different keys.
- **Shift Values**: The `lt` list defines the amount of shift to be applied. You can modify these values for different key generation strategies.
- **Randomization**: You can adjust the randomization process to control the final selection of the bits for each key.

## Requirements
- Python 3.x

## Run the Code Online

You can also run the DES key generation code directly in your browser using the following link on **OnlineGDB**.

### Click the link to run the code:
[https://onlinegdb.com/pwOBL_JcZ]

By clicking on the link, you can run the code, input your string, and observe the key generation process live.

---

## Conclusion
The DES key generation process is a vital part of the **Data Encryption Standard**. While DES itself is no longer considered secure, understanding its key generation process offers valuable insight into symmetric key ciphers. This script demonstrates the mechanics of key creation through bitwise operations, shifts, and randomization, forming a basic example of how DES keys are generated for each round of encryption.
```