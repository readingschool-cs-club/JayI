#!/usr/bin/env python3
#
# JayI main executable.
#

from datetime import datetime
from sys import exit
import os

import string, re

# the core
class JayI:

    def __init__(self):
        self.filename = "responses.txt"
        self.map = {}
        self.learning = None
        try:
            open(self.filename, "r+").close()
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
       
        # squeeze spacing, make it lowercase and strip out punctuation and excess spacing
        trigger = re.sub(r"\s\s+", " ", trigger).lower().translate(dict.fromkeys(map(ord, string.punctuation))).strip()

        if trigger in self.map:
            return self.map[trigger]

        if trigger == "bye":
            print("Bye, see you soon!")
            exit()
        elif trigger == "delete all":
            file.close()
            self.reset()
            return
        elif trigger == "where were you born":
            self.learning = trigger
            return "I'm not sure. Can you tell me?"
        elif trigger == "how old are you":
            birthday = self.birthday()
            day = "day" if birthday == 1 else "days"
            return "I am %d %s old" % (birthday, day)
        else:
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
