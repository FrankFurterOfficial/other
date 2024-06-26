import tkinter as tk

root = tk.Tk()
label = tk.Label(None, text='Close this window to play', font=('Arial', '45'),fg='black')
label.pack()
image = tk.PhotoImage(file="image.png")
label = tk.Label(image=image)
label.pack()
root.mainloop()