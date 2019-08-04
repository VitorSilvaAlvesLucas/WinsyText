#-------------------------------------------------------#
# https://www.github.com/VitorSilvaAlvesLucas/CalcPy-v1.0
#-------------------------------------------------------#
try:
    from tkinter import X, Y, BOTTOM, RIGHT, LEFT, Y, HORIZONTAL
    from tkinter.scrolledtext import ScrolledText
    from tkinter import messagebox
    from tkinter import filedialog
    from tkinter.font import Font
    from tkinter import *
    import pyautogui
    import io
    import os
except Exception as error:
    messagebox.showerror("Warning","{}".format(error))

class Root():
    def __init__(self,main_tab):
        ### Find current directory ###
        self.directory = os.getcwd()
        ###### Window properties ######
        self.main_tab = main_tab
        self.main_tab.protocol("WM_DELETE_WINDOW",self.exit_all_windows)
        self.main_tab.state("zoomed")
        self.main_tab["bg"] = "#1C1C1C"
        self.main_tab.title("WinsyText")
        self.main_tab.minsize(600, 300)
        ######## Define icon #########
        self.main_tab.iconbitmap("{}\icon_winsytext.ico".format(self.directory))
        ########### Frame #############
        self.frame = Frame(self.main_tab)
        self.frame.pack(fill=BOTH,expand=1)
        ##### Start Scrolled Text #####
        self.scrolled_text()
        ####### Start Menu Bar ########
        self.options_menu()
        ######## Info Status ##########
        self.info_status_var = Label(self.main_tab,text="WinsyText-v1.0 | GitHub: https://github/VitorSilvaAlvesLucas/WinsyText-v1.0",
        bg="#1C1C1C",fg="#00BFFF",font=("Arial",10))
        self.info_status()
        try:
            open_preferences = io.open("preferences.txt","r")
            self.read_preferences = open_preferences.read().strip()
            if "Dark Mode" in self.read_preferences:
	            self.dark_mode()
            elif "Light Mode" in self.read_preferences:
	            self.light_mode()
            elif "Gray Mode" in self.read_preferences:
                self.gray_mode()
            else:
                null_var = "null"
        except Exception as error:
            messagebox.showerror("Warning","{}".format(error))
    def info_status(self):
        self.info_status_var.pack()
    def options_menu(self):
        object_menu = Menu()
        ###### Menu declaration  ######
        file_menu_bar = Menu(object_menu,background="white",foreground="black")
        edit_menu_bar = Menu(object_menu,background="white",foreground="black")
        view_menu_bar = Menu(object_menu,background="white",foreground="black")
        preferences_menu_bar = Menu(object_menu,background="white",foreground="black")
        theme_menu_bar = Menu(object_menu,background="white",foreground="black")
        help_menu_bar = Menu(object_menu,background="white",foreground="black")
        tools_menu_bar = Menu(object_menu,background="white",foreground="black")
        ########## Menu bars ##########
        object_menu.add_cascade(label="File",menu=file_menu_bar)
        object_menu.add_cascade(label="Edit",menu=edit_menu_bar)
        object_menu.add_cascade(label="View",menu=view_menu_bar)
        object_menu.add_cascade(label="Preferences",command=self.preferences_menu_bar)
        object_menu.add_cascade(label="Theme",menu=theme_menu_bar)
        object_menu.add_cascade(label="Tools",command=self.tools)
        object_menu.add_cascade(label="Help",command=self.help)
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
        view_menu_bar.add_command(label="FullScreen",command=self.fullscreen)
        view_menu_bar.add_command(label="Disable FullScreen",command=self.disable_fullscreen)
        theme_menu_bar.add_command(label="Dark Mode",command=self.dark_mode)
        theme_menu_bar.add_command(label="Light Mode",command=self.light_mode)
        theme_menu_bar.add_command(label="Gray Mode",command=self.gray_mode)
        self.main_tab.configure(menu=object_menu)
    def scrolled_text(self):
        ######## Define the widgets ##########
        self.scrolled_text_var = ScrolledText(self.frame,width=1,height=1,wrap=NONE,bg="#1C1C1C",fg="white",font=("Arial", 11))
        horizontal_scrollbar = Scrollbar(self.frame,orient=HORIZONTAL)
        ######### Start the widgets ##########
        self.scrolled_text_var.pack(fill=BOTH,expand=1)
        horizontal_scrollbar.pack(fill=BOTH)
        ###### Configure the widgets #########
        horizontal_scrollbar.config(command=self.scrolled_text_var.xview)
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
    def preferences_menu_bar(self):
        try:
            ##### Window properties ######
            self.object_preferences = Tk()
            self.object_preferences["bg"] = "#F2F2F2"
            self.object_preferences.geometry("200x90+50+50")
            self.object_preferences.title("Preferences")
            self.object_preferences.resizable(False,False)
            ######## Define icon #########
            self.object_preferences.iconbitmap("{}\icon_winsytext.ico".format(self.directory))
            ########## Widgets ###########
            label_font_type = Label(self.object_preferences,text="Type font:",font=("Calibri"))
            label_font_size = Label(self.object_preferences,text="Font size:",font=("Calibri"))
            #### Statement of available resources ####
            fonts_disp = ["Calibri","Cambria","Courier","Impact","Georgia","ComicSansMS","Constantia","Fixedsys","Arial"]
            self.fonts_var = StringVar(self.object_preferences)
            self.fonts_var.set("Calibri")
            self.fonts_var.trace("w",self.change_font)
            size_disp = [8,9,10,11,12,14,16,18,20,22,24,28,36,42,68]
            self.size_var = IntVar(self.object_preferences)
            self.size_var.set(12)
            self.size_var.trace("w",self.change_size)
            ####### OptionMenu #########
            to_choose_fonts = OptionMenu(self.object_preferences,self.fonts_var,*fonts_disp)
            to_choose_size = OptionMenu(self.object_preferences,self.size_var,*size_disp)
            ####### Start Widgets ########
            label_font_type.grid(row=0,column=0,padx=0,pady=10)
            label_font_size.grid(row=1,column=0,padx=0,pady=10)
            to_choose_fonts.grid(row=0,column=1,padx=5,pady=5)
            to_choose_size.grid(row=1,column=1,padx=5,pady=5)
        except Exception as error:
            messagebox.showerror("Warning","{}".format(error))
    def change_font(self,*args):
        try:
            self.scrolled_text_var["font"] = self.fonts_var.get()
        except Exception as error:
            messagebox.showerror("Warning","{}".format(error))
    def change_size(self,*args):
        font_object = Font(size=self.size_var.get(),family=self.fonts_var.get())
        self.scrolled_text_var.config(font=font_object)
    def help(self):
        try:
            os.system("start https://github.com/VitorSilvaAlvesLucas/CoderNEText-v1.0")
        except Exception as error:
            messagebox.showerror("Warning","{}".format(error))
    def tools(self):
        try:
            ##### Window properties ######
            self.object_tools = Tk()
            self.object_tools["bg"] = "#F2F2F2"
            self.object_tools.geometry("+70+50")
            self.object_tools.title("Tools")
            self.object_tools.iconbitmap("{}\icon_winsytext.ico".format(self.directory))
            self.object_tools.resizable(False,False)
            #####   Widgets count   #####
            label_count = Label(self.object_tools,text="How many times this word appeared:",font="Calibri")
            self.entry_count = Entry(self.object_tools,width=30,font="Calibri")
            self.label_show_count = Label(self.object_tools,text="",font="Calibri")
            button_count = Button(self.object_tools,text="Count:",command=self.button_count,font="Calibri")
            ####### Start Widgets ########
            label_count.grid(row=0,column=0,padx=5,pady=5)
            self.entry_count.grid(row=1,column=0,padx=5,pady=5)
            self.label_show_count.grid(row=2,column=0,padx=40,pady=5)
            button_count.grid(row=2,column=0,padx=8,pady=5,stick=W)
        except Exception as error:
            messagebox.showerror("Warning","{}".format(error))
    def button_count(self):
        get_entry = self.entry_count.get()
        get_words = self.scrolled_text_var.get(0.0,END)
        count_words = get_words.count(get_entry)
        self.label_show_count["text"] = count_words
    def fullscreen(self):
        try:
            self.main_tab.resizable(False,False)
            self.main_tab.state("zoomed")
        except Exception as error:
            messagebox.showerror("Warning","{}".format(error))
    def disable_fullscreen(self):
        try:
            self.main_tab.resizable(True,True)
            self.main_tab.state("normal")
        except Exception as error:
            messagebox.showerror("Warning","{}".format(error))
    def dark_mode(self):
        os.system("echo Dark Mode > preferences.txt")
        self.scrolled_text_var["bg"] = "black"
        self.scrolled_text_var["fg"] = "white"
    def light_mode(self):
        os.system("echo Light Mode > preferences.txt")
        self.scrolled_text_var["bg"] = "white"
        self.scrolled_text_var["fg"] = "black"
    def gray_mode(self):
        os.system("echo Gray Mode > preferences.txt")
        self.scrolled_text_var["bg"] = "#1C1C1C"
        self.scrolled_text_var["fg"] = "white"
    def exit_all_windows(self):
        self.main_tab.destroy()
        try:
            self.object_preferences.destroy()
        except Exception as error:
            null_var = "null"
        try:
            self.object_tools.destroy()
        except Exception as error:
            null_var = "null"

object_tk = Tk()
Root(object_tk)
object_tk.mainloop()
