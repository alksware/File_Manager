import os
import time as tm


class File:

    def create_new_file(self):
        try:
            file_name = input("Please enter your file's name:")
            with open(file_name, "w") as file:
                tm.sleep(2)
                print(file_name, "Created")
        except:
            print("System: an unexpected error was encountered")

    def delete_file(self):
        try:
            file_name = input("Please choose delete file:")
            tm.sleep(2)
            os.remove(file_name)
            print(file_name, "Deleted")
        except:
            print("System: an unexpected error was encountered")

    def add_text(self):
        try:
            file_name = input("Please choose add file:")
            with open(file_name, "a") as file:
                text = input("Please write something:\n")
                file.write("{}\n".format(text))
                tm.sleep(2)
                print("This sentence added to {} :".format(file_name), text)
        except:
            print("System: an unexpected error was encountered")

    def read_file(self):
        try:
            file_name = input("Please choose read file:")
            tm.sleep(2)
            print("---Context in {}---".format(file_name))
            with open(file_name, "r") as file:
                context = file.read()
                print(context)
        except:
            print("System: an unexpected error was encountered")

    def read_first_line(self):
        try:
            file_name = input("Please choose read file:")
            tm.sleep(2)
            print("--- Title in {}---".format(file_name))
            with open(file_name, "r") as file:
                context = file.readline()
                print(context)
        except:
            print("System: an unexpected error was encountered")

fileManager = File()

while True:
    choose_progress = input("""
--------------------------------
Welcome to Alksware Text Manager 
Please enter a progress
1-Create a file
2-Delete a file
3-Add text in choose file
4-Read text in choose file
5-Read only title in choose file
Q-Quit
*** Programe reboot himself after create a file
--------------------------------
Chooses Progress : 
    """)
    if(choose_progress == "Q"):
        break
    elif(choose_progress == "1"):
        fileManager.create_new_file()
        print("Rebooting the program...")
        tm.sleep(2)
        break
    elif(choose_progress == "2"):
        fileManager.delete_file()
    elif(choose_progress == "3"):
        fileManager.add_text()
    elif(choose_progress == "4"):
        fileManager.read_file()
    elif(choose_progress == "5"):
        fileManager.read_first_line()
    else:
        print("Please enter a valid a chooses")
        continue

