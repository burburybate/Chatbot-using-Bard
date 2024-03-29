import tkinter as tk
from tkinter import ttk
from tkinter import *

def get_auth_info(): #Function to Take Cookies and Token required for Authentication.
    def submit():
        global input1, input2, input3
        input1 = entry1.get()
        input2 = entry2.get()
        input3 = entry3.get()
        entry1.config(state='readonly')
        entry2.config(state='readonly')
        entry3.config(state='readonly')
        root.quit()
    def quitAndOpenNew():
        root.destroy()  # Destroy the current master window
        get_auth_info()
    root = tk.Tk()
    root.title("Bard Authentication UI")
    menu = Menu(root)
    root.config(menu=menu)

    filemenu = Menu(menu)
    menu.add_cascade(label='File', menu=filemenu)
    filemenu.add_command(label='New', command=quitAndOpenNew)
    filemenu.add_command(label='Exit', command=root.quit)
    helpmenu = Menu(menu)
    menu.add_cascade(label='Help', menu=helpmenu)
    helpmenu.add_command(label='About')

    window_width = 800
    window_height = 250
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    x_position = (screen_width - window_width) // 2
    y_position = (screen_height - window_height) // 2
    root.geometry(f"{window_width}x{window_height}+{x_position}+{y_position}")

    root.configure(bg='#f0f0f0')

    

    label1 = tk.Label(root, text="PSID:", bg='#f0f0f0')
    label1.pack(pady=(10, 0))

    entry1 = tk.Entry(root)
    entry1.pack(pady=(0, 10), padx=10, fill=tk.X)

    label2 = tk.Label(root, text="PSIDCC:", bg='#f0f0f0')
    label2.pack(pady=(10, 0))

    entry2 = tk.Entry(root)
    entry2.pack(pady=(0, 10), padx=10, fill=tk.X)

    label3 = tk.Label(root, text="PSIDTS:", bg='#f0f0f0')
    label3.pack(pady=(10, 0))

    entry3 = tk.Entry(root)
    entry3.pack(pady=(0, 10), padx=10, fill=tk.X)

    submit_button = tk.Button(root, text="Submit and Next", command=submit, bg='#4caf50', fg='white', font=('Arial', 12))
    submit_button.pack(pady=(10, 10), padx=10, fill=tk.X)

    root.mainloop()

    return input1, input2, input3

def bard_ui(bard): #Main Chat Window code.
    import tkinter as tk
    def send_message():
        user_message = entry.get()
        chat_box.insert(tk.END, f"You: {user_message}\n")
        entry.delete(0, tk.END)
        question = user_message
        data = bard.get_answer(question)
        answer = data['content']
        response = f"Bot: {answer}\n"
        chat_box.insert(tk.END, response)
        chat_box.see(tk.END)
    def quitAndOpenNew():
        root.destroy()  # Destroy the current master window
        get_auth_info()
    root = tk.Tk()
    root.title("Chatbot")
    root.geometry("400x500")

    chat_frame = tk.Frame(root)
    chat_frame.pack(pady=10)

    scrollbar = tk.Scrollbar(chat_frame)
    scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

    chat_box = tk.Text(chat_frame, wrap=tk.WORD, yscrollcommand=scrollbar.set, height=15, width=40)
    chat_box.pack(side=tk.LEFT, fill=tk.BOTH)
    scrollbar.config(command=chat_box.yview)

    entry = tk.Entry(root, font=("Helvetica", 12))
    entry.pack(pady=10, padx=10, ipady=5, fill=tk.X, expand=True)

    send_button = tk.Button(root, text="Send", command=send_message, bg="#4CAF50", fg="white", font=("Helvetica", 12))
    send_button.pack(pady=5)
    send_button = tk.Button(root, text="New token", command=quitAndOpenNew, bg="#4CAF50", fg="white", font=("Helvetica", 12))
    send_button.pack(pady=5)

    return root