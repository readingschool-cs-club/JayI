#!/usr/bin/env python3
#
# JayI main executable.
#

from datetime import datetime
from sys import exit
import os

import string, re
import csv

LIKE = "like "
KEYS = ["trigger", "answer"]

# the core
class JayI:
    def __init__(self, filename="responses.csv"):
        self.filename = filename
        self.learning = None
        self.map = {}
        try:
            open(self.filename, "r+").close()
            self.read_file()
        except (IOError, FileNotFoundError):
            self.reset()

    def reset(self):
        if os.path.exists(self.filename):
            os.remove(self.filename)
        self.init_file()
        self.learn("Hello", "Hi")
        self.learn("Hi", "Hello")
        self.read_file()

    def learn(self, key, value):
        key = self.flatten(key)
        self.map[key] = self.parse(value)
        self.write_file(key, value)

    def init_file(self):
        with open(self.filename, "w+") as file:
            writer = csv.DictWriter(file, fieldnames=KEYS)
            writer.writeheader()

    def write_file(self, key, value):
        with open(self.filename, "a+") as file:
            writer = csv.DictWriter(file, fieldnames=KEYS)
            writer.writerow({ KEYS[0]: key, KEYS[1]: value })

    def parse(self, value):
        flattened = self.flatten(value)
        if flattened.startswith(LIKE):
            return self.link(flattened[len(LIKE):])
        return value.strip()

    def read_file(self):
        self.map = {}
        with open(self.filename, "r") as file:
            reader = csv.DictReader(file)
            for row in reader:
                key = row[KEYS[0]]
                value = row[KEYS[1]]
                self.map[key] = self.parse(value)

    @staticmethod
    def flatten(trigger):
        # squeeze spacing, make it lowercase and strip out punctuation and excess spacing
        trigger = re.sub(r"\s", " ", trigger)
        return re.sub(r"\s\s+", " ", trigger).lower().translate(dict.fromkeys(map(ord, string.punctuation))).strip()

    def link(self, trigger):
        trigger = self.flatten(trigger)
        def linker():
            return self.respond(trigger)
        return linker

    @staticmethod
    # find out my birthday
    def birthday():
        birthday = datetime.fromtimestamp(1423785600)  # 13/02/2015
        age = (datetime.utcnow() - birthday).days
        return age

    # the whole loop!
    def respond(self, trigger):
        learning = self.learning
        self.learning = None

        if not trigger.strip():
            return

        if learning:
            self.learn(learning, trigger)
            return
      
        trigger = self.flatten(trigger)

        if trigger in self.map:
            learnt = self.map[trigger]
            try:
                return learnt()
            except TypeError:
                return learnt

        if trigger == "bye":
            print("Bye, see you soon!")
            exit()
        elif trigger == "delete all":
            self.reset()
            return
        elif trigger == "where were you born":
            self.learning = trigger
            return "I'm not sure. Can you tell me?"
        elif trigger in ["how old are you", "when were you born"]:
            birthday = self.birthday()
            day = "day" if birthday == 1 else "days"
            return "I am %d %s old" % (birthday, day)
        else:
            self.learning = trigger
            return "Sorry, that is not in my database. Suggest me a good response: "

if __name__ == "__main__":
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
        r = Jay.respond(input("> "))
        r and print(r)

