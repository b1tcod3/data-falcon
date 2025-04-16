# This code creates a simple Tkinter GUI application that interacts with an SQLite database.
# It allows users to add new entries and view all existing entries in the database
import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
import sqlite3

def create_database():
    conn = sqlite3.connect('example.db')
    c = conn.cursor()
    c.execute('''
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY,
            name TEXT NOT NULL,
            age INTEGER NOT NULL
        )
    ''')
    conn.commit()
    conn.close()

def insert_user(entry_name,entry_age,tree):
    
    name = entry_name.get().strip()
    age = entry_age.get().strip()
    
    if not name or not age:
        messagebox.showwarning('Error','Datos Incompletos')
        return
    if not name.isalpha():
        messagebox.showwarning('Error','Nombre Incorrecto')
        return
    if not validate_age(age):
        messagebox.showwarning('Error','Edad Incorrecta')
        return  
    
    conn = sqlite3.connect('example.db')
    c = conn.cursor()
    c.execute('''
            INSERT INTO users (name, age)
            VALUES (?, ?)
        ''', (name, age))
    entry_name.delete(0,tk.END)
    entry_age.delete(0,tk.END)
    messagebox.showinfo('Èxito','Datos guardados exitosamente')
    update_table(tree)
    conn.commit()
    conn.close()

def validate_age(age):
    if age.isdigit():
        age_num = int(age)
        return 0 <= age_num <= 99
    return False
    

def fetch_users():
    conn = sqlite3.connect('example.db')
    c = conn.cursor()
    c.execute('SELECT * FROM users')
    rows = c.fetchall()
    conn.close()
    return rows

def show_users():
    users = fetch_users()
    if not users:
        messagebox.showinfo("No Users", "No users found in the database.")
        return

    user_list = "\n".join([f"ID: {user[0]}, Name: {user[1]}, Age: {user[2]}" for user in users])
    messagebox.showinfo("Users", user_list)

def update_table(tree):
    for row in tree.get_children():
        tree.delete(row)

    users = fetch_users()
    for user in users:
        tree.insert('', tk.END, values=(user[0], user[1], user[2]))

def main():
    window = tk.Tk()
    window.title("User Database")
    create_database()
    
    tk.Label(window, text="Name:").grid(row=0,column=0)
    entry_name = tk.Entry(window)
    entry_name.grid(row=0,column=1)
    tk.Label(window, text="Age:").grid(row=1,column=0)
    entry_age = tk.Entry(window)
    entry_age.grid(row=1,column=1)
    
    #configuración de la tabla
    columns = ('ID','NOmbre','Edad')
    tree = ttk.Treeview(window,columns=columns,show="headings")
    tree.grid(row=4,column=0,columnspan=2)
    
    for col in columns:
        tree.heading(col,text=col)
        tree.column(col,width=100)
    update_table(tree)
    
    btn_save = tk.Button(window, text="Add User", command=lambda:insert_user(entry_name,entry_age,tree))
    btn_save.grid(row=2,columnspan=2)
    btn_show_users = tk.Button(window, text="Show Users", command=show_users)
    btn_show_users.grid(row=3,columnspan=2)
    
    
    
    window.mainloop()
    
    
    
if __name__ == "__main__":  
    main()

    
