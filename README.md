# 🔐 ShieldPass - Secure Password Storage with Real-Time Breach Warnings

**ShieldPass** is an offline password manager designed to securely store user credentials while providing real-time breach alerts. It ensures that users do not reuse compromised passwords, enhancing their overall cybersecurity.

---

## 📌 Project Overview

With increasing cyber threats, ShieldPass helps users manage their passwords efficiently while keeping them safe from breaches. This system securely encrypts passwords and alerts users if their chosen password has been compromised in a data breach.

It operates **locally on a user's device**, ensuring data privacy and security without relying on external cloud storage.

---

## 🌿 Features

- ✅ **Offline Secure Password Storage** – Stores passwords securely using encryption.  
- ✅ **Real-Time Breach Alerts** – Checks passwords against known data breaches.  
- ✅ **User-Friendly Interface** – Simple GUI for storing and retrieving passwords.  
- ✅ **Encryption for Protection** – Uses AES/Fernet encryption to protect stored passwords.  
- ✅ **Logging System** – Keeps track of user actions, breaches, and retrievals.  
- ✅ **Duplicate Prevention** – Avoids saving the same credentials multiple times.  

---

## 🤖 Tech Stack

- **Python** (Core programming language)  
- **Tkinter** (GUI for user-friendly interaction)  
- **SQLite** (Local database for password storage)  
- **Cryptography (Fernet)** (For encrypting and decrypting passwords)  
- **Requests** (For breach detection via Have I Been Pwned API)  
- **Logging** (For tracking system activities and security alerts)  

---

## 📂 Dataset & API Used

- 🔹 **Have I Been Pwned API** - To check if a password is compromised.  
- 🔹 **SQLite Database** - Securely stores encrypted passwords.  

---

## 🔍 How It Works

### **🔐 Saving a Password**
1. Enter the website, username, and password.
2. ShieldPass checks if the password has been breached using the **Have I Been Pwned API**.
3. If the password is **safe**, it gets **encrypted and stored securely** in the local SQLite database.
4. If the password is **breached**, the system **alerts the user** and prevents saving.

### **🔓 Retrieving a Password**
1. Enter the website name.
2. ShieldPass searches the **encrypted database** for the credentials.
3. If found, it **decrypts the password** and displays the username & password.
4. The user can **copy the credentials securely** without displaying them in plaintext.

### **📜 Logging System**
ShieldPass maintains a detailed **log file (`activity.log`)** that records:
- **Breach Alerts** – When a user tries to save a compromised password.
- **Successful Saves** – When a password is securely stored.
- **Password Retrieval Attempts** – When a user requests stored credentials.

---

## 📊 Security Features

ShieldPass is designed with multiple security layers to **protect user credentials**.

### **🔒 Encryption Method**
- **AES/Fernet Encryption** – Encrypts all stored passwords for security.
- **One-Way Hashing (SHA-1 Prefix)** – Used for safe breach lookup without exposing full passwords.

### **⚠️ Breach Detection**
- Uses the **Have I Been Pwned API** to check if a password is leaked in previous data breaches.
- Warns the user if the password is compromised before saving.

---

## 📜 License
This project is licensed under the **MIT License**. You are free to use, modify, and distribute it as needed.

---

## 🙌 Acknowledgments

- **Have I Been Pwned API** – For breach detection.
- **Python Cryptography Library** – For AES/Fernet encryption.
- **SQLite** – For secure local password storage.

📌 **Stay Secure with ShieldPass!** 🔐

