#!/usr/bin/env python3
#
# JayI main executable.
#

from datetime import *

class JayI:
  
    def __init__(self):
        self.filename = "responses.txt"
        self.map = {}
        print("""
            _________________
           |\________________\                                      
           \|_______    _____|   __________          ___     ___
                 | |   |        |\_________\        |\__\   |\__\         
             ____| |   |        | | _____  |        | | |   | | |          
            |\ ____|   |        | | |   |  |___     | | |___| | |
            | |        |        | | |___|  |___\    | | |___| | |
             \|________|         \|____________|     \|_______| |
                                                            | | |  
                                                            | | |
                                                            | | |
                                                    ________| | |
                                                   | \_______\| |
                                                    \|__________|
         
                Created and developed by readingschool-cs-club
                         Bringing Computers to Life
         """)

        try:
            file1 = open(self.filename, "r")
            file1.close()
        except IOError:
            file1 = open(self.filename, "w+")
            file1.write("hello:hi\n")
            file1.write("hi:hello\n")
            file1.close()


    def read_file(self):
        for line in open(self.filename, "r"):
            parts = line.split(":", 1)
            self.map[parts[0]] = parts[1].rstrip("\n")

    
    # find out my birthday
    def birthday(self):
        birthday = datetime.strptime("2015-02-13", "%Y-%m-%d")
        age = (datetime.utcnow() - birthday).days
        return abs(age)

    # the whole loop!
    def respond(self):
        print("Hi there. You can talk to me.")
        file = open(self.filename, "a+")
        while True:
            trigger = input()
            trigger = trigger.lower()
            if trigger == "bye":
                print("Bye, see you soon !")
                break
            elif trigger == "delete all":
                file.close()
                file_stuff = open(self.filename, "w")
                file_stuff.write("")
                file_stuff.close()
            elif trigger== "how old are you?":
                if self.birthday() == 1:
                    print("I am " + str(self.birthday()) + " day old")
                else:
                    print("I am " + str(self.birthday()) + " days old")
            elif trigger == "where were you born?":
                print("In a computer with billions of transistors!")
            elif trigger.strip() == "":
                pass
            else:
                try:
                    print(self.map[trigger])
                except:
                    inp = input("Sorry, that is not in my database. Suggest me a good response: ")
                    if inp.lower() == "No":
                        pass
                    else:
                        self.map[trigger] = inp
                        file.write(trigger + ":" + inp + "\n")
        file.close()



Jay = JayI()

Jay.read_file()
Jay.respond()
