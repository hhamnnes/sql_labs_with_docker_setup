import sqlite3

conn = sqlite3.connect('garn.db')
c = conn.cursor()

conn.commit()
conn.close()
print("Database opprettet!")