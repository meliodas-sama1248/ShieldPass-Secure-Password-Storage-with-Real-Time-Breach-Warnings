import sqlite3

# Setup database
def setup_database():
    conn = sqlite3.connect("passwords.db")
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS passwords (
                        id INTEGER PRIMARY KEY, 
                        website TEXT, 
                        username TEXT, 
                        password TEXT)''')
    conn.commit()
    conn.close()

def save_password(website, username, encrypted_password):
    conn = sqlite3.connect("passwords.db")
    cursor = conn.cursor()

    # Check if the website + username already exist
    cursor.execute("SELECT * FROM passwords WHERE website = ? AND username = ?", (website, username))
    existing_entry = cursor.fetchone()

    if existing_entry:
        print("🚨 Duplicate website & username detected!")  # Debugging line
        conn.close()
        return False  # Prevent duplicate saving

    # If not duplicate, save password
    cursor.execute("INSERT INTO passwords (website, username, password) VALUES (?, ?, ?)",
                   (website, username, encrypted_password))
    conn.commit()
    conn.close()
    return True

# Retrieve encrypted password
def get_password(website):  # Ensure this function exists
    conn = sqlite3.connect("passwords.db")
    cursor = conn.cursor()
    cursor.execute("SELECT username, password FROM passwords WHERE website = ?", (website,))
    result = cursor.fetchone()
    conn.close()
    return result  # Returns None if no result is found
