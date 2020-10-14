import random
import tkinter

top = tkinter.Tk()
button = tkinter.Button(top, text="Enter a noun", command=generate_madlib())
top.mainloop()

file = open('madlibs.txt', 'r')
madlibs_input = file.readlines()
madlib_line = random.choice(madlibs_input)


def generate_madlib():
    noun = input("Enter a noun")
    madlib_output = madlib_line.replace("blank", noun)
    print("output: " + madlib_output)
