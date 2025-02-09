# Vigenère Cipher Implementation

## About the Project
This project implements the Vigenère Cipher, a polyalphabetic substitution cipher used for encrypting alphabetic text. It includes two different versions of the cipher implementation.

## How It Works
The project consists of two main functions for each version:

1. **First Version** (`vigenere` and `rodar`):
   - Uses ASCII values to compute the shift.
   - Implements the cipher using character-to-integer conversions.

2. **Second Version** (`vigenere2` and `rodar2`):
   - Uses a predefined alphabet string to determine shifts.
   - Implements the cipher using index-based operations on the alphabet.

## Getting Started

### Prerequisites
You need Python 3 installed. You can check your Python version by running:

python --version
text

### Installation
Clone the repository or download the Python file manually:
git clone https://github.com/BernardoMarta/Vigenere-Cipher
cd Vigenere-Cipher
text

## Usage

### Using the First Version:
key = "key"
plaintext = "hello"
ciphertext = vigenere(key, plaintext)
print("Encrypted text:", ciphertext)
text

### Using the Second Version:
key = "key"
plaintext = "hello"
ciphertext = vigenere2(key, plaintext)
print("Encrypted text (version 2):", ciphertext)
text

## Example

**Input:**
key = "key"
text = "hello"
text

**Output (Both Versions):**
Encrypted text: rijvs
text

## Features
- Two different implementations of the Vigenère Cipher
- Supports lowercase alphabetic input
- Simple and easy-to-understand code structure

## Code Snippet
ALPHABET='abcdefghijklmnopqrstuvwxyz'
def vigenere(chave,txt):
txt_cifrado=''
for i in range(len(txt)):
txt_cifrado += rodar(chave[i%len(chave)],txt[i])
return txt_cifrado
def rodar(chave2,letra):
n=ord(letra)-ord('a')
nova_letra = chr((n+ord(chave2)-ord('a'))%26+ord('a'))
return nova_letra
text

## Contributing
Feel free to fork this repository and submit pull requests to [BernardoMarta's repository](https://github.com/BernardoMarta/Vigenere-Cipher)!

You can reach me at: **bernardomarta@outlook.pt**

## License
This project is licensed under the MIT License.

## Acknowledgments
Thanks to the cryptography community for the Vigenère Cipher concept and implementation ideas.
