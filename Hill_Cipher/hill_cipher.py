import numpy as np
def hill_cipher_encrypt(plaintext,key):
    n=len(key)
    plaintext=plaintext.upper().replace(" ","")
    if len(plaintext)%n!=0:
        plaintext+="X"*(n-len(plaintext)%n)
    plaintext_vector=[ord(char)-ord('A')for char in plaintext]
    ciphertext=""
    for i in range(0,len(plaintext_vector),n):
        block=plaintext_vector[i:i+n]
        result=np.dot(key,block)%26
        ciphertext+="".join(chr(num+ord('A'))for num in result)
    return ciphertext
#example
plaintext="HELLO"
key=np.array([[6,24,1],[13,16,10],[20,17,15]])#3x3 matrix
print("Encrypted:",hill_cipher_encrypt(plaintext,key))

def mod_inverse_matrix(matrix,mod):
    matrix=Matrix(matrix)
    det=int(matrix,det())
    det_inv=pow(det,-1,mod)
    adjugate=matrix.adjugate()
    inverse_matrix=(det_inv*adjugate)%mod
    return np.array(inverse_matrix).astype(int)
def hill_decrypt(ciphertext,key_matrix):
    n=key_matrix.shape[0]
    plain_num=[]
    cipher_num=text_to_num(ciphertext)
    key_inv_matrix=mod_inverse_matrix(key_matrix,26)
    for i in range(0,len(cipher_num),n):
        vector=np.array(cipher_num[i:i+n])
        vector_mul=np.dot(key_inv_matrix,vector)%26
        plain_num.extend(vector_mul)
    plain_text=char_to_text(plain_num)
    return plain_text
decrypted_text=hill_decrypt(encrypted_text,key_matrix)
print("the decrypted text is:",decrypted_text)
