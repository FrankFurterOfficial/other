import tkinter as tk
label = tk.Label(None, text='cool eagle', font=('Arial', '45'),fg='red')
label.pack()
root = tk.Tk()
image = tk.PhotoImage(file="cool eagle.png")
label = tk.Label(image=image)
label.pack()
root.mainloop()