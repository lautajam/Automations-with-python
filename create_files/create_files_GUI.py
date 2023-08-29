# Create a simple gui with tkinter to create files with the name, number and extension that the user wants.

from tkinter import *

# Create the window

window = Tk()

window.title("Create files")

window.geometry("600x210")

# Create the labels

label_title = Label(window, text = "Create files")

label_title.grid(column = 0, row = 0)

label_name = Label(window, text = "Enter the name of the file: ")

label_name.grid(column = 0, row = 1)

label_number = Label(window, text = "Enter the number of the file: ")

label_number.grid(column = 0, row = 2)

label_extension = Label(window, text = "Enter the extension of the files: ")

label_extension.grid(column = 0, row = 3)

label_path = Label(window, text = "Enter the path where you want to create the files: ")

label_path.grid(column = 0, row = 4)

# Create the entries

entry_name = Entry(window, width = 20)

entry_name.grid(column = 1, row = 1)

entry_number = Entry(window, width = 20)

entry_number.grid(column = 1, row = 2)

entry_extension = Entry(window, width = 20)

entry_extension.grid(column = 1, row = 3)

entry_path = Entry(window, width = 20)

entry_path.grid(column = 1, row = 4)

# Function which get the data from the entries
def get_data():
        
        name_file = entry_name.get()
    
        number_file = entry_number.get()
    
        extension = entry_extension.get()
    
        path = entry_path.get()
        
        return name_file, number_file, extension, path

# Function which create the files
def create_files():
    
    name_file, number_file, extension, path = get_data()
    
    for i in range(1, int(number_file) + 1):
        file = open(path + "/" + name_file + str(i) + extension, "w")
        file.close()
    
    print("Files created successfully")
   
            
# Create the button

button = Button(window, text = "Create files", command = create_files)

button.grid(column = 0, row = 5)


# MAIN

window.mainloop()