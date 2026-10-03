import sqlite3
 
# Create/connect to database
conn = sqlite3.connect("tution.db")
 
# Create a cursor
cursor = conn.cursor()
# Create a table
cursor.execute("""
    CREATE TABLE IF NOT EXISTS student(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT,
        dob DATE,
        age INTEGER,
        gender TEXT,
        mobile number INTEGER,
        email address TEXT,
        password TEXT
    )
""")

cursor.execute("""
    insert into student values(
        104,
        'neethu',
        '15-01-2007',
        19,
        'female',
        7012273121,
        'abcde123@gmail.com',
        'qwertyu'
    )
""")
 
# Save changes
conn.commit()
 
# Close connection
conn.close()
 
print("Database created successfully!")



