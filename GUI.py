import tkinter as tk
from tkinter.filedialog import askopenfilename

window = tk.Tk()
window.title('Greenwood Bill Emailer')
#filename = askopenfilename()
window.geometry("800x500")
window.attributes('-topmost', True)
window.update()
Button1 = tk.Label(
    text="Please select a button:",
    fg="Black",
    bg="grey",
    width=40,
    height=3
)
Button1.pack()
Button2 = tk.Button(
    text="Utilities",
    width=25,
    height=5,
    bg="blue",
    fg="yellow",
)
Button2 = tk.Button(
    text="Property Taxes",
    width=25,
    height=5,
    bg="blue",
    fg="yellow",
)
Button1.pack()
Button2.pack()


window.mainloop()
