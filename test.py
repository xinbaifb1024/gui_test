import tkinter as tk
from tkinter import messagebox
from tkinter import StringVar 
import subprocess
import os

class Demo:
    def __init__(self):
        self.window = tk.Tk()
        self.labels = []
        self.buttons = []
        self.commands = []
        self.load_command()
        self.pos = 0
        self.dir = os. getcwd()
        self.v = StringVar()
    
    def call_command(self, pos):
        self.pos = pos % len(self.commands)
        cmd = "cpy.cpp"
        subprocess.call(self.dir+"/a.out " + self.commands[self.pos], shell=True)
        self.v.set(self.commands[self.pos])
    
    def load_command(self):
        with open("commands.config", "r") as f:
            lines = f.readlines()
            for line in lines:
                self.commands.append(line.strip())
    
    def add_label(self):
        label = tk.Label(
            textvariable=self.v,
            fg="white",
            bg="black",
            width=50,
            height=20
        )

        label.pack()
        self.labels.append(label)

    def button_left_func(self):
        self.pos = max(0, self.pos - 1)
        self.call_command(self.pos)

    def button_right_func(self):
        self.pos = min(len(self.commands)-1, self.pos + 1)
        self.call_command(self.pos)
        #messagebox.showinfo("Message","button_right " + str(pos))

    def add_right_button(self, text):
        button = tk.Button(
            text=text,
            width=25,
            height=5,
            bg="white",
            fg="black",
            command=self.button_right_func
        )
        button.pack(side=tk.RIGHT)
        self.buttons.append(button)


    def add_left_button(self, text):
        button = tk.Button(
            text=text,
            width=25,
            height=5,
            bg="white",
            fg="black",
            command=self.button_left_func
        )
        button.pack(side=tk.LEFT)
        self.buttons.append(button)

if __name__ == '__main__':
    demo = Demo()
    demo.add_label()
    demo.add_left_button("Previus")
    demo.add_right_button("Next")
    demo.window.mainloop()


