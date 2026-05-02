import tkinter as tk
from tkinter import messagebox
from crud import add_task, update_task_status, delete_task, get_tasks

#  Pencere 
root = tk.Tk()
root.title("TO-DO LIST")
root.geometry("400x600")

#  Görev Giriş
task_entry = tk.Entry(root, width=45)
task_entry.pack(pady=10)

# -FONKSİYONLAR

def refresh_list():
    task_list.delete(0, tk.END)
    tasks = get_tasks()
    for task in tasks:
        task_list.insert(tk.END, f"ID: {task[0]} | {task[1]} [{task[2]}]")

def add_task_gui():
    task = task_entry.get() 
    if task != "":
        add_task(task)
        task_entry.delete(0, tk.END)
        refresh_list()
    else:
        messagebox.showwarning("Uyarı", "Lütfen bir görev girin.")

def delete_taskgui():
    try:
        selected_task = task_list.get(task_list.curselection()) 
        task_id = selected_task.split(" ")[1]
        delete_task(task_id)
        refresh_list()
    except:
        messagebox.showwarning("Uyarı", "Lütfen silinecek bir görev seçin.")

def complete_task_gui():
    try:
        selected_task = task_list.get(task_list.curselection())
        task_id = selected_task.split(" ")[1]
        update_task_status(task_id, "Completed")
        refresh_list()
    except:
        messagebox.showwarning("Uyarı", "Lütfen tamamlanacak bir görev seçin.")

# ARAYÜZ 

# Liste
task_list = tk.Listbox(root, width=50, height=15)
task_list.pack(pady=10)

# Buton
add_button = tk.Button(root, text="Görev Ekle", command=add_task_gui, bg="lightblue", fg="black")
add_button.pack(pady=5)

delete_button = tk.Button(root, text="Görev Sil", command=delete_taskgui, bg="lightcoral", fg="white")
delete_button.pack(pady=5)

complete_button = tk.Button(root, text="Görev Tamamla", command=complete_task_gui, bg="lightgreen", fg="black")
complete_button.pack(pady=5)


refresh_list()


root.mainloop()