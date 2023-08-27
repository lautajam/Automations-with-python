"""This script creates files with the name, number and extension that the user wants."""

# Ask the user for the name, number and extension of the files. Also ask for the path where you want to create the files.
name_file = input(print("Enter the name of the file: "))

number_file = input(print("Enter the number of the file: "))

extension = input(print("Enter the extension of the files: "))

path = input(print("Enter the path where you want to create the files: "))

# Create the files with the name, number and extension that the user wants.
for i in range(1, int(number_file) + 1):
    file = open(path + "/" + name_file + str(i) + extension, "w")
    file.close()

