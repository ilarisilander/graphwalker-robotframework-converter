from tkinter import *
import json
from tkinter import filedialog
import tkinter as tk
import subprocess

def set_test_case_input():
    case_name_value.set(entry.get())

# Open file explorer and get file path
def set_graphwalker_path():
    root = tk.Tk()
    root.withdraw()
    global gw_path
    gw_path = filedialog.askopenfilename()
    btn.configure(bg = 'green')

# Open file explorer and get file path
def set_test_file_path():
    root = tk.Tk()
    root.withdraw()
    global test_path
    test_path = filedialog.askopenfilename()
    btn2.configure(bg = 'green')

# Run GraphWalker json file in GraphWalker CLI and filter it to a dictionary
def create_test_case(gw, test, generator):
    cmd_line = 'java -jar ' + '"' + gw + '"' + ' offline -m ' + '"' + test + '" ' + generator
    output = subprocess.check_output(cmd_line, shell=True)
    test_case = str(output)
    test_case = test_case[3:-2]
    test_case = test_case.replace("\\r\\n", "")
    test_case = test_case.replace('"currentElementName":"', "")
    test_case = test_case.replace('"', "")
    test_case = test_case[:-4]
    test_case = test_case.split("}{")
    return test_case

# Create a robot file with Test Cases generated from the GraphWalker CLI test
def create_test_case_file(test_case_name, test_file):
    robot_file = open("test_case.robot", "w")
    robot_file.write("*** Test Cases ***\n")
    robot_file.write(test_case_name + "\n")
    robot_file.write("    " + "[Documentation]" + "\n")
    for string in test_file:
        robot_file.write("    " + string + "\n")
    robot_file.close()

# Create a keywords file and remove duplicates from the GraphWalker test file
def create_keywords_file(test_file):
    test_file = list(dict.fromkeys(test_file))
    keywords_file = open("keywords.robot", "w")
    keywords_file.write("*** Keywords ***\n")
    for string in test_file:
        keywords_file.write(string + "\n" + "\n")
    keywords_file.close()

def get_generator_from_json(path):
    with open(path) as file:
        json_file = json.load(file)
        for each in json_file['models']:
            return each['generator']


def go():
    generator = get_generator_from_json(test_path)
    btn5.configure(bg = '#984c56', text = 'Building')
    test_case_name = entry.get()
    test_case = create_test_case(gw_path, test_path, generator)
    create_test_case_file(test_case_name, test_case)
    create_keywords_file(test_case)
    btn5.configure(bg = 'green', text = 'Done')


def quit():
    sys.exit()

def print_names():
    print(gw_path)
    print(test_path)

window = tk.Tk()

# GraphWalker CLI path
btn = Button(window, text = "GraphWalker CLI", bg = '#789E9E',fg = '#EEF3DB', relief = FLAT, activebackground = '#EEF3D8', font = 'Roboto')
btn.place(x = 10, y = 100)
btn.configure(command=set_graphwalker_path)

# JSON model file path
btn2 = Button(window, text = "JSON model", bg = '#789E9E',fg = '#EEF3DB', relief = FLAT, activebackground = '#EEF3D8', font = 'Roboto')
btn2.place(x = 10, y = 150)
btn2.configure(command=set_test_file_path)

# Quit the application
btn3 = Button(window, text = "Quit", bg = '#984c56',fg = '#EEF3DB', relief = FLAT, activebackground = '#EEF3D8', font = 'Roboto')
btn3.place(x = 10, y = 200)
btn3.configure(command = quit)

# Set the name of the test case
btn4 = Button(window, text = "Ok", bg = '#789E9E',fg = '#EEF3DB', relief = FLAT, activebackground = '#EEF3D8', font = 'Roboto')
btn4.place(x = 250, y = 50)
btn4.configure(command = set_test_case_input)

# Activates the process of creating test and creating files
btn5 = Button(window, text = "Go", bg = '#789E9E',fg = '#EEF3DB', relief = FLAT, activebackground = '#EEF3D8', font = 'Roboto')
btn5.place(x = 500, y = 200)
btn5.configure(command = go, width = 10, height = 10)

# Labels and inputs
case_name_value = StringVar()
tk.Label(window, textvariable = case_name_value).place(x = 50, y = 10)
entry = Entry(window, width = 35)
entry.insert(0, "Type test case name here")
entry.place(x = 10, y = 50)

window.title("JSON to robot converter")
window.geometry("640x480")
window.configure(bg = '#4D6466')
window.mainloop()
