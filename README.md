🔐 ShieldPass - Secure Password Storage with Real-Time Breach Warnings

ShieldPass is an offline password manager designed to securely store user credentials while providing real-time breach alerts. It ensures that users do not reuse compromised passwords, enhancing their overall cybersecurity.

📌 Project Overview

With increasing cyber threats, ShieldPass helps users manage their passwords efficiently while keeping them safe from breaches. This system securely encrypts passwords and alerts users if their chosen password has been compromised in a data breach.

It operates locally on a user's device, ensuring data privacy and security without relying on external cloud storage.

🌿 Features

✅ Offline Secure Password Storage – Stores passwords securely using encryption.✅ Real-Time Breach Alerts – Checks passwords against known data breaches.✅ User-Friendly Interface – Simple GUI for storing and retrieving passwords.✅ Encryption for Protection – Uses AES/Fernet encryption to protect stored passwords.✅ Logging System – Keeps track of user actions, breaches, and retrievals.✅ Duplicate Prevention – Avoids saving the same credentials multiple times.

🤖 Tech Stack

Python (Core programming language)

Tkinter (GUI for user-friendly interaction)

SQLite (Local database for password storage)

Cryptography (Fernet) (For encrypting and decrypting passwords)

Requests (For breach detection via Have I Been Pwned API)

Logging (For tracking system activities and security alerts)

📂 Dataset & API Used

🔹 Have I Been Pwned API - To check if a password is compromised.🔹 SQLite Database - Securely stores encrypted passwords.

🚀 Installation & Setup

1️⃣ Clone the Repository

git clone https://github.com/yourusername/ShieldPass.git
cd ShieldPass

2️⃣ Install Dependencies

pip install -r requirements.txt

3️⃣ Run the Application

python main.py

🔍 How It Works

🔐 Saving a Password

Enter the website, username, and password.

ShieldPass checks if the password has been breached.

If safe, it encrypts and saves the password securely.

If breached, it alerts the user and prevents saving.

🔓 Retrieving a Password

Enter the website name.

ShieldPass decrypts and displays the stored credentials.

User can copy and use the password securely.

📜 Logging System

All activities are recorded in activity.log, including:

Breach alerts

Successful password saves

Password retrieval attempts

📊 Model Evaluation

ShieldPass does not use a machine learning model but relies on real-time breach detection and strong encryption techniques to secure user credentials.

📜 License

This project is licensed under the MIT License. Feel free to modify and improve it!

🙌 Acknowledgments

Have I Been Pwned API for breach detection

Python Cryptography Library for encryption

SQLite for secure local storage

📌 Stay Secure with ShieldPass! 🔐

