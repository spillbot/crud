# ~/projects/main.py
import sqlite3

db = sqlite3.connect('data/db')
cursor = db.cursor()

def main():
    prompt = input("/.> ")
    if prompt == "create":
        create()
    elif prompt == "exit":
        exit
    elif prompt == "init":
        init()
    elif prompt == "ls":
        ls()
    else:
        main()
        
def create():
    name = input("Name: ")
    email = input("Email: ")
    password = input("Password: ")
    try:
        with db: 
            cursor.execute('''INSERT INTO users(name, email, password)
                              VALUES(?,?,?)''',(name,email,password))
            print(('User %s inserted') % (name))
    except sqlite3.IntegrityError:
        print('Record already exists')
    finally:

        db.commit()
        return main()

def ls():
    cursor.execute('''SELECT * from users''')
    all_rows = cursor.fetchall()
    for row in all_rows:
        print('{0} : {1}, \t {2}'.format(row[0], row[1], row[2]))
    return main()

def init():
    cursor = db.cursor()
    cursor.execute('''
        CREATE TABLE users(ID INTEGER PRIMARY KEY, name TEXT,
                           email TEXT unique, password TEXT)
   ''')
    db.commit()
    return main()

main()
