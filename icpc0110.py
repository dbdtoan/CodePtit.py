import sqlite3

username = input("Enter username: ")
password = input("Enter password: ")

conn = sqlite3.connect('users.db')
c = conn.cursor()

query = "SELECT * FROM users WHERE username = '" + username + "' AND password = '" + password + "'"

c.execute(query)

result = c.fetchone()

if result:
    print("Login successful")
else:
    print("Login failed11111")
    
conn.close()
