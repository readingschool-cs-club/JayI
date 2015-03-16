#!/usr/bin/env python3
#
# JayI main executable.
#

from datetime import datetime
from sys import exit
import os


#

class JayI:

    def __init__(self):
        self.filename = "responses.txt"
        self.map = {}
        self.learning = None
        try:
            file = open(self.filename, "r+")
            file.close()
        except (IOError, FileNotFoundError):
            self.reset()
        self.read_file()

    def reset(self):
        if os.path.exists(self.filename):
            os.remove(self.filename)
        file = open(self.filename, "w+")
        file.write("hello:Hi\n")
        file.write("hi:Hello\n")
        file.close()

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
        learning = self.learning
        self.learning = None

        if not trigger.strip():
            return

        if learning:
            self.map[learning] = trigger
            file.write(learning + ":" + trigger + "\n")
            return
#Trigger response to user......
        trigger = trigger.lower()
        if trigger == "bye":
            print("Bye, see you soon!")
            exit()
        elif trigger == "delete all":
            file.close()
            self.reset()
            return
        elif trigger == "how old are you?":
            birthday = self.birthday()
            day = "day" if birthday == 1 else "days"
            return "I am %d %s old" % (birthday, day)
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
    result = Jay.respond(input("> "))
    result is not None and print(result)
