import random
import time
import threading
import tkinter as tk

clock = 0
i=0
loop=True
option=0

def shell_text():       ##text prompts to appear here

    print("welcome")
    time.sleep(1)

    
def option_check():     ##checking through options regularly, any interval will work. the sleep interval is necessary as to ensure it isn't trying to complete the loop at max frequency
    
    global option
    global loop

    print(option)
    
    while loop == True:
        
        if option !=0:
            print(option)
            option = 0
            
        else:
            
            option=option
            

        time.sleep(0.1)



check_thread = threading.Thread(target = option_check, daemon = True)
check_thread.start()

text_thread = threading.Thread(target = shell_text, daemon = True)
text_thread.start()

class Application(tk.Frame):        ##standard interface

    def __init__(self, master=None):

        super().__init__(master)
        self.master = master
        self.pack()
        self.create_widgets()

    def create_widgets(self):

        def option_change(i):       ##changes options
            
            global option

            option = i

        def quit_ui():      ##closes threads and ui; ends program
            
            global loop
            loop = False
            root.destroy()

        self.header = tk.Label(self, width = 20, height = 1, text = "chose your option")
        self.header.grid(row = 0, column = 0)
        
        self.option1 = tk.Button(self, width = 10, height = 1, text = "1")
        self.option1["command"] = lambda i=1: option_change(i)
        self.option1.grid(row = 1, column = 0)
        
        self.option2 = tk.Button(self, width = 10, height = 1, text = "2")
        self.option2["command"] = lambda i=2: option_change(i)
        self.option2.grid(row = 2, column = 0)

        self.option3 = tk.Button(self, width = 10, height = 1, text = "3")
        self.option3["command"] = lambda i=3: option_change(i)
        self.option3.grid(row = 3, column = 0)

        self.option4 = tk.Button(self, width = 10, height = 1, text = "4")
        self.option4["command"] = lambda i=4: option_change(i)
        self.option4.grid(row = 4, column = 0)

        self.quit = tk.Button(self, width = 10, height = 1, text = "QUIT", fg = "red")
        self.quit["command"] = lambda i=i: quit_ui()
        self.quit.grid(row=999, column = 0)

root =tk.Tk()

app = Application(master=root)

app.master.title="options"
app.master.geometry("300x160")
app.mainloop()
