try:
    from tkinter.scrolledtext import ScrolledText
    from tkinter import messagebox
    from tkinter import filedialog
    from tkinter import *
    from os import *
    import pyautogui
    import io
except Exception as error:
    messagebox.showerror("Warning","{}".format(error))

class Root():
    def __init__(self,main_tab):
        #### Propriedades da janela ###
        self.main_tab = main_tab
        self.main_tab.title("Cleaner")
        self.main_tab["bg"] = "gray"
        self.main_tab.state("zoomed")
        self.main_tab["bg"] = "#1B1B1B"
        self.main_tab.minsize(600, 300)
        ##### Start Scrolled Text #####
        self.scrolled_text()
        ####### Start Menu Bar ########
        self.options_menu()
    def options_menu(self):
        object_menu = Menu()
        ###### Menu declaration  ######
        file_menu_bar = Menu(object_menu,background="white",foreground="black")
        edit_menu_bar = Menu(object_menu,background="white",foreground="black")
        view_menu_bar = Menu(object_menu,background="white",foreground="black")
        preferences_menu_bar = Menu(object_menu,background="white",foreground="black")
        help_menu_bar = Menu(object_menu,background="white",foreground="black")
        ########## Menu bars ##########
        object_menu.add_cascade(label="File",menu=file_menu_bar)
        object_menu.add_cascade(label="Edit",menu=edit_menu_bar)
        object_menu.add_cascade(label="View",menu=view_menu_bar)
        object_menu.add_cascade(label="Preferences",menu=preferences_menu_bar)
        object_menu.add_cascade(label="Help",menu=help_menu_bar)
        ###### Menu bar options #######
        file_menu_bar.add_command(label="Save",command=self.save_as_file)
        file_menu_bar.add_command(label="Open",command=self.open_as_file)
        file_menu_bar.add_command(label="New",command=self.new_file)
        file_menu_bar.add_command(label="Exit",command=self.exit_the_program)
        edit_menu_bar.add_command(label="Select all",command=self.select_all)
        edit_menu_bar.add_command(label="Copy",command=self.copy)
        edit_menu_bar.add_command(label="Paste",command=self.paste)
        edit_menu_bar.add_command(label="Leave all caps",command=self.leave_all_caps)
        edit_menu_bar.add_command(label="Leave all lowercase",command=self.leave_all_lowercase)
        self.main_tab.configure(menu=object_menu)
    def scrolled_text(self):
        self.scrolled_text_var = ScrolledText(self.main_tab,width=1,height=1,bg="#131313",fg="white",font=("Arial", 11))
        self.scrolled_text_var.pack(fill=BOTH,expand=1)
    def save_as_file(self):
        try:
            self.main_tab.filename = filedialog.asksaveasfilename(initialdir="/",title="Select file",filetypes=(("txt files","*.txt"),("all files","*.*")))
            save_file = io.open(self.main_tab.filename+".txt","w")
            text = str(self.scrolled_text_var.get(1.0,END))
            save_file.write(text)
        except Exception as error:
            messagebox.showerror("Warning","{}".format(error))
    def open_as_file(self):
        try:
            self.main_tab.filename = filedialog.askopenfilename(initialdir="/",title="Select file",filetypes=(("txt files","*.txt"),("all files","*,*")))
            open_file_content = io.open(self.main_tab.filename,"+r")
            read_file_content = open_file_content.read()
            self.scrolled_text_var.delete(0.0,END)
            self.scrolled_text_var.insert(0.0,read_file_content)
        except Exception as error:
            messagebox.showerror("Warning","{}".format(error))
    def new_file(self):
        self.scrolled_text_var.delete(0.0,END)
    def exit_the_program(self):
        self.main_tab.quit()
    def select_all(self):
        try:
            pyautogui.hotkey("ctrl", "a")
        except Exception as error:
            messagebox.showerror("Warning","{}".format(error))
    def copy(self):
        try:
            pyautogui.hotkey("ctrl", "c")
        except Exception as error:
            messagebox.showerror("Warning","{}".format(error))
    def paste(self):
        try:
            pyautogui.hotkey("ctrl", "v")
        except Exception as error:
            messagebox.showerror("Warning","{}".format(error))
    def leave_all_caps(self):
        try:
            get_text_for_upper = self.scrolled_text_var.get(0.0,END)
            transform_text_for_upper = get_text_for_upper.upper()
            self.scrolled_text_var.delete(0.0,END)
            self.scrolled_text_var.insert(0.0,transform_text_for_upper)
        except Exception as error:
            messagebox.showerror("Warning","{}".format(error))
    def leave_all_lowercase(self):
        try:
            get_text_for_lower = self.scrolled_text_var.get(0.0,END)
            transform_text_for_lower = get_text_for_lower.lower()
            self.scrolled_text_var.delete(0.0,END)
            self.scrolled_text_var.insert(0.0,transform_text_for_lower)
        except Exception as error:
            messagebox.showerror("Warning","{}".format(error))

object_tk = Tk()
Root(object_tk)
object_tk.mainloop()
