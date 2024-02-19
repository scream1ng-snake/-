import os
import sys
import customtkinter
from PIL import Image, ImageTk

# это надо чтобы картнки упаковались в ехе-шку
def get_path(filename):
    if hasattr(sys, "_MEIPASS"):
        return os.path.join(sys._MEIPASS, filename)
    else:
        return filename
    
class PathSelector(customtkinter.CTkFrame):
    path = ''
    def __init__(self, master):
        super().__init__(master)

        self.entry_path = customtkinter.CTkEntry(master=master, width=240, height=32, placeholder_text="Выберите путь к папке")
        self.entry_path.pack(pady=12, padx=10)

    def set_path(self, path):
        self.path = path

class App(customtkinter.CTk):
    name = 'Калькулятор'
    def __init__(self):
        super().__init__()
        self.geometry("400x150")
        self.title(self.name)

        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(0, weight=1)

        self.checkbox_frame = PathSelector(self)
        # self.checkbox_frame.grid(row=0, column=0, padx=10, pady=(10, 0), sticky="nsw")

        self.button = customtkinter.CTkButton(self, text="my button", command=self.button_callbck)
        # self.button.grid(row=3, column=0, padx=10, pady=10, sticky="ew")


        self.wm_iconbitmap()
        icopath = ImageTk.PhotoImage(file=get_path("icon.png"))
        self.iconphoto(False, icopath)

    def quit_window(self, icon, item):
        icon.stop()
        self.destroy()

    def show_window(self, icon, item):
        icon.stop()
        self.after(0, self.deiconify)

    

    def button_callbck(self):
        print("button clicked")

app = App()
app.mainloop()