
# Vigenère Cipher Encryption

## 🔐 About the Project
This project implements the **Vigenère Cipher**, a method of encrypting alphabetic text using a series of Caesar ciphers based on the letters of a keyword. It enhances security over the traditional Caesar cipher by using a multi-letter shifting system.

This project includes two versions of the Vigenère Cipher:
1. **First Version** - Uses ASCII values (`ord` and `chr`) to compute the shift.
2. **Second Version** - Uses a predefined alphabet string (`ALPHABET.index()`) to determine shifts.

Each version is implemented in the `vigenere_cipher_functions.py` file.

## 📜 How It Works
- **First Version** (`vigenere()` and `rodar()`): This version uses ASCII values to calculate the letter shifts.
- **Second Version** (`vigenere2()` and `rodar2()`): This version uses an alphabet string to determine shifts.

## 🚀 Getting Started

### Prerequisites
You need Python 3 installed. You can check your Python version by running:
```bash
python --version
```

### Installation
Clone the repository or download the Python file manually:
```bash
git clone https://github.com/BernardoMarta/Vigenere-Cipher
cd Vigenere-Cipher
```

You can also download the `vigenere_cipher_functions.py` file directly.

## 🛠️ Usage

### Using the First Version:
To use the first version of the Vigenère Cipher, import and call the `vigenere()` function from `vigenere_cipher_functions.py`:
```python
from vigenere_cipher_functions import vigenere

key = "keyword"
plaintext = "hello"
ciphertext = vigenere(key, plaintext)
print("Encrypted text:", ciphertext)
```

### Using the Second Version:
To use the second version, import and call the `vigenere2()` function:
```python
from vigenere_cipher_functions import vigenere2

key = "keyword"
plaintext = "hello"
ciphertext = vigenere2(key, plaintext)
print("Encrypted text (version 2):", ciphertext)
```

## 🔄 Example
**Input:**
```python
key = "key"
text = "hello"
```

**Output (First Version):**
```text
Encrypted text: riijg
```

**Output (Second Version):**
```text
Encrypted text (version 2): riijg
```

## 📌 Features
✅ Implements Vigenère Cipher  
✅ Two different implementations (ASCII-based and ALPHABET-based)  
✅ Simple, lightweight, and easy to use  

## 🤝 Contributing
Feel free to fork this repository and submit pull requests to [BernardoMarta's repository](https://github.com/BernardoMarta/Vigenere-Cipher)!

You can reach me at: **bernardomarta@outlook.pt**

## 📜 License
This project is licensed under the MIT License.

## 🌟 Acknowledgments
Thanks to the cryptography community for inspiration!
