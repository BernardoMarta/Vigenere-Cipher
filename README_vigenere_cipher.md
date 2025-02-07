
# Vigenère Cipher Encryption

## 🔐 About the Project
This project implements the **Vigenère Cipher**, a method of encrypting alphabetic text using a series of Caesar ciphers based on the letters of a keyword. It enhances security over the traditional Caesar cipher by using a multi-letter shifting system.

## 📜 How It Works
This project includes **two different implementations** of the Vigenère Cipher:
1. **First Version** - Uses ASCII values (`ord` and `chr`) to compute the shift.
2. **Second Version** - Uses a predefined alphabet string (`ALPHABET.index()`) to determine shifts.

Each version consists of:
- **vigenere()** and **rodar()** for the ASCII-based approach.
- **vigenere2()** and **rodar2()** for the alphabet-based approach.

## 🚀 Getting Started

### Prerequisites
You need Python 3 installed. You can check your Python version by running:
```bash
python --version
```

### Installation
Clone the repository or download the Python file manually.
```bash
git clone https://github.com/BernardoMarta/Vigenere-Cipher
cd Vigenere-Cipher
```

## 🛠️ Usage
Run the script and test the encryption function:
```python
from vigenere import vigenere

key = "keyword"
plaintext = "hello"
ciphertext = vigenere(key, plaintext)
print("Encrypted text:", ciphertext)
```

To use the second version:
```python
from vigenere import vigenere2

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
**Output (Version 1):**
```text
Encrypted text: riijg
```
**Output (Version 2):**
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
