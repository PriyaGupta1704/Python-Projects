# 🔐 Password Manager (Python)

A simple and secure **Password Manager** built using **Python** and **Fernet encryption** from the `cryptography` library.  
This project allows users to **store and view passwords securely** using symmetric encryption.

---

## 🚀 Features

- 🔑 Generates and stores an encryption key securely
- 🔒 Encrypts passwords before saving
- 🔓 Decrypts passwords while viewing
- 📁 Stores encrypted passwords in a local file
- ❌ Prevents sensitive files from being pushed to GitHub

---

## 🛠️ Technologies Used

- Python 3
- cryptography (Fernet)
- OS module
- File handling

---

## 📂 Project Structure
Python_Project/
│
├── Password_Manager.py # Main password manager script
├── passwords.txt # Stores encrypted passwords (ignored in Git)
├── key.key # Encryption key (ignored in Git)
├── .gitignore # Prevents sensitive files from being pushed
└── README.md # Project documentation


---

## ⚙️ How It Works

1. On first run, the program generates an encryption key (`key.key`)
2. Passwords are encrypted using **Fernet symmetric encryption**
3. Encrypted passwords are stored in `passwords.txt`
4. While viewing, passwords are decrypted using the same key

---

## ▶️ How to Run the Project

### 1️⃣ Install dependencies
```bash
pip install cryptography

2️⃣ Run the program
python Password_Manager.py

🧪 Usage

Choose Add to store a new password

Choose View to display stored passwords

Press q to quit the program

🔐 Security Notes

❗ key.key and passwords.txt are NOT pushed to GitHub

These files are added to .gitignore for security

Never share encryption keys publicly

📌 Important

This project is for learning and demonstration purposes.
For production use, additional security layers should be implemented.

👩‍💻 Author

Priya Gupta
Python & DevOps Enthusiast 🚀

📜 License

This project is open-source and free to use for learning purposes.

