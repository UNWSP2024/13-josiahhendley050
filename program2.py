import sqlite3

# Connect to the database
conn = sqlite3.connect("cities.db")
cur = conn.cursor()

# Select all data from Cities table
cur.execute("SELECT * FROM Cities")

# Fetch and display results
rows = cur.fetchall()

print("CityID | CityName | Population")
print("-----------------------------")

for row in rows:
    print(row)

# Close connection
conn.close()
