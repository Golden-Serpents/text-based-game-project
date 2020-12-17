import time
import random
import tkinter as tk

##interface is for user interaction only, interface will consist of the
##options the play can take numbered 1-4*. text indicating what each one does
##will be on screen in the text form. the game will be text based aided by the
##options available to them in the interface

##interface creation


class Application(tk.Frame):

    def __init__(self, master=None):
        
        super().__init__(master)
        self.master = master
        self.pack()
        self.create_widgets()
        
    def create_widgets(self):
        
        self.option = []
        self.title = []
    
        ##the shit i need to work outside of the function
        option1 = False
        option2 = False
        option3 = False
        option4 = False

        timer = 0
        
        x = 0
        
        self.title.append(tk.Label(self, width = 30, height = 1, fg = "black", text = "your options"))  ##just creating buttons and labels nothing important for now anyway
        self.title[x].grid(row = 0, column = 0)
        
        self.option.append(tk.Button(self, width = 10, height = 1, fg = "black", text = "1"))
        self.option[x].grid(row = 1, column = 0)

        x+=1

        self.option.append(tk.Button(self, width = 10, height = 1, fg = "black", text = "2"))
        self.option[x].grid(row = 2, column = 0)

        x+=1

        self.option.append(tk.Button(self, width = 10, height = 1, fg = "black", text = "3"))
        self.option[x].grid(row = 3, column = 0)

        x+=1
        
        self.option.append(tk.Button(self, width = 10, height = 1, fg = "black", text = "4"))
        self.option[x].grid(row = 4, column = 0)

        self.spacer = tk.Label(self, width = 10, height = 1)
        self.spacer["text"] = "\n"
        self.spacer.grid(row = 29, column = 0)

        self.quit = tk.Button(self, width = 10, height = 1, fg = "red")
        self.quit["text"] = "QUIT"
        self.quit["command"] = self.master.destroy
        self.quit.grid(row = 30, column = 0)

        print("you wake up in a small apartment. you've lived here for as long as you can remember. the passage of time has been meaningless and inevident. your birthday may have passed at any point \nthere is", \
              " a letter that has been slid under your door.\n1. pick up the letter")
        
        self.option[x]["state"] = tk.DISABLED
        
        x-=1

        self.option[x]["state"] = tk.DISABLED

        x-=1

        self.option[x]["state"] = tk.DISABLED

        x-=1

        self.option[x]["command"] = (lambda : option1 , True) ###need to do this with commands so that they don't automatically trigger
        
        global task 

        def task():

            self.option[x]["state"] = tk.NORMAL
            self.option[x]["command"] = lambda : option2 , True
            print("2. leave the apartment")

x = 1

root = tk.Tk()

app = Application(master=root)

app.master.title("options screen")
app.master.geometry("300x185")
root.after(1, task)
app.mainloop()

##this ain't good
##to add the options they need to be added in create_widgets() and have .update(command = option[]) whatever like that probably a bunch of nested if statements. this is going to be awful
