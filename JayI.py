#!/usr/bin/env python3
#
# JayI main executable.
#

from datetime import datetime
from sys import exit

class JayI:

    def __init__(self):
        self.filename = "responses.txt"
        self.map = {}
        self.learning = None
        try:
            file1 = open(self.filename, "r")
            file1.close()
        except IOError:
            file1 = open(self.filename, "w+")
            file1.write("hello:Hi\n")
            file1.write("hi:Hello\n")
            file1.close()
        self.read_file()


    def read_file(self):
        for line in open(self.filename, "r"):
            parts = line.split(":", 1)
            self.map[parts[0]] = parts[1].rstrip("\n")

    @staticmethod
    # find out my birthday
    def birthday():
        birthday = datetime.fromtimestamp(1423785600)  # 13/02/2015
        age = (datetime.utcnow() - birthday).days
        return age

    # the whole loop!
    def respond(self, trigger):
        file = open(self.filename, "a+")

        if self.learning:
            if trigger.lower().strip():
                self.map[self.learning] = trigger
                file.write(self.learning + ":" + trigger + "\n")
            self.learning = None
            return

        trigger = trigger.lower()
        if trigger == "bye":
            print("Bye, see you soon!")
            exit()
        elif trigger == "delete all":
            file.close()
            new_file = open(self.filename, "w")
            new_file.write("")
            new_file.close()
        elif trigger == "how old are you?":
            birthday = self.birthday()
            if birthday == 1:
                return "I am 1 day old"
            else:
                return "I am %d days old" % birthday
        elif trigger == "where were you born?":
            return "In a computer with billions of transistors!"
        else:
            try:
                return self.map[trigger]
            except:
                self.learning = trigger
                return "Sorry, that is not in my database. Suggest me a good response: "
        file.close()

print(r"""
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


Jay = JayI()
print("Hi there. You can talk to me.")
while True:
    print(Jay.respond(input("> ")) or "")
