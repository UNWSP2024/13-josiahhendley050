import sqlite3

conn = sqlite3.connect("phonebook.db")
cur = conn.cursor()

def add_entry():
    name = input("Enter name: ")
    phone = input("Enter phone number: ")
    cur.execute("INSERT OR REPLACE INTO Entries (name, phone) VALUES (?, ?)", (name, phone))
    conn.commit()
    print("Entry added.")

def lookup():
    name = input("Enter name to search: ")
    cur.execute("SELECT phone FROM Entries WHERE name=?", (name,))
    result = cur.fetchone()
    if result:
        print("Phone number:", result[0])
    else:
        print("Not found.")

def update():
    name = input("Enter name to update: ")
    new_phone = input("Enter new phone number: ")
    cur.execute("UPDATE Entries SET phone=? WHERE name=?", (new_phone, name))
    conn.commit()
    print("Updated.")

def delete():
    name = input("Enter name to delete: ")
    cur.execute("DELETE FROM Entries WHERE name=?", (name,))
    conn.commit()
    print("Deleted.")

def show_all():
    cur.execute("SELECT * FROM Entries")
    for row in cur.fetchall():
        print(row)

while True:
    print("\n--- Phone Book Menu ---")
    print("1. Add Entry")
    print("2. Look Up Number")
    print("3. Update Number")
    print("4. Delete Entry")
    print("5. Show All")
    print("6. Exit")

    choice = input("Choose: ")

    if choice == "1":
        add_entry()
    elif choice == "2":
        lookup()
    elif choice == "3":
        update()
    elif choice == "4":
        delete()
    elif choice == "5":
        show_all()
    elif choice == "6":
        break
    else:
        print("Invalid choice")

conn.close()
