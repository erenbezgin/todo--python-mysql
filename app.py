import tkinter as tk
from tkinter import messagebox
from crud import add_task, update_task_status, delete_task, show_tasks

# ana pencere
root = tk.Tk()
root.title("TO-DO LİST")
root.geometry("400x500")

# görev giris
task_entry = tk.Entry(root, width=45)
task_entry.pack(pady=10)  # üstten altan 10 br bosluk

# listeleme alanı
task_list = tk.Listbox(root, width=50, height=20)
task_list.pack(pady=10)


def refresh_list():
    task_listbox.delete(0, tk.END)


root.mainloop()


def add_task_gui():
    task = tast_enty.get()
    if task != "":
        add_task(task)
        task_entry.delete(0, tk.END)
        refresh_list()
    else:
        messagebox.showwarning("Uyarı", "Lütfen bir görev girin.")


def delete_taskgui():
    try:
        selected_task = task_listbox.get(task_listbox.curselection())
        task_id = selected_task.split(" ")[1]
        delete_task(task_id)
        refresh_list()
    except:
        messagebox.showwarning("Uyarı", "Lütfen silinecek bir görev seçin.")


def refhesh_list():
    task_list.delete(0, tk.END)
    tasks = show_tasks()
    for task in tasks:
        task_list.insert(tk.END, f"ID {task[0]|task[1]} [{task[2]}]")


add_button = tk.Button(
    root, text="Görev Ekle", command=add_task_gui, bg="lightblue", fg="black"
)
add_button.pack(pady=5)

delete_button = tk.Button(
    root, text="Görev Sil", command=delete_taskgui, bg="lightcoral", fg="white"
)
delete_button.pack(pady=5)

refresh_list()
