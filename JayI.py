from datetime import *

print("""


   _________________
  |\________________\.
  \|________________|   __________          ___     ___
        | |   |        |\_________\        |\__\   |\__\.
    ____| |   |        | | _____  |        | | |   | | |
   |\ ____|   |        | | |   |  |___     | | |   | | |
   | |        |        | | |___|  |___\    | | |___| | |
    \|________|         \|____________|     \|_______| |
                                                   | | |
                                                   | | |
                                           ________| | |
                                          | \________| |
                                           \|__________|

       Created and developed by readingschool-cs-club
                Bringing Computers to Life
""")

class JayI:

    # the constructor
    def __init__(self):
        self.filename = "responses.txt"
        self.map = {}

        try:
            file1 = open(self.filename, "r")
            file1.close()
        except:
            file1 = open(self.filename, "w+")
            file1.write("Hello:Hi\n")
            file1.write("Hi:Hello\n")
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
            if trigger.lower() == "bye":
                print("Bye, see you soon !")
                break
            elif trigger.lower() == "delete all":
                file.close()
                file_stuff = open(self.filename, "w")
                file_stuff.write("")
                file_stuff.close()
            elif trigger.lower() == "how old are you ?":
                if JayI().birthday() == 1:
                    print("I am " + str(JayI().birthday()) + " day old")
                else:
                    print("I am " + str(JayI().birthday()) + " days old")
            else:
                try:
                    print(self.map[trigger])
                except:
                    inp = input("Sorry, that is not in my database. Suggest me a good response: ")
                    if inp == "No":
                        print("Alright, then")
                    else:
                        self.map[trigger] = inp
                        file.write(trigger + ":" + inp + "\n")
        file.close()



Jay = JayI()

Jay.read_file()
Jay.respond()
# I wonder what line I'm on...
