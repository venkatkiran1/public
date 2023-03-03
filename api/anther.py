import tkinter as tk
from tkinter import messagebox
from qrcode import make
from PIL import Image, ImageTk

def generate_qr_code():
    url = entry.get()
    img = make(url)
    img.save("qrcode.png")
    img = Image.open("qrcode.png")
    img = img.resize((250, 250), Image.ANTIALIAS)
    img = ImageTk.PhotoImage(img)
    label.config(image=img)
    label.image = img

root = tk.Tk()
root.geometry("350x350")
root.title("QR Code Generator")

label = tk.Label(root)
label.pack()

entry = tk.Entry(root)
entry.pack()

generate_button = tk.Button(root, text="Generate QR Code", command=generate_qr_code)
generate_button.pack()

root.mainloop()
