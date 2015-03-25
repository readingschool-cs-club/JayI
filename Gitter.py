from Bot import Bot

import requests
import json
import re

class GitterBot(Bot):
    def __init__(self, token):
        super().__init__()
        self.token = token
        self.headers = {
            "Authorization": "Bearer %s" % self.token,
        }

        self.userId = self.get_userId()
        self.connect(self.get_rooms()[0])

    def get_rooms(self):
        r = requests.get("https://api.gitter.im/v1/rooms", headers=self.headers)
        return [room["id"] for room in r.json()]

    def get_userId(self):
        r = requests.get("https://api.gitter.im/v1/user", headers=self.headers)
        return r.json()[0]["id"]

    def connect(self, room):
        r = requests.get("https://stream.gitter.im/v1/rooms/%s/chatMessages" % room,
                headers=self.headers, stream=True)

        for line in r.iter_lines(chunk_size=1):
            line = line.decode("utf-8")
            if line.strip():
                self.load(json.loads(line), room)

    def load(self, data, room):
        mention = None
        for user in data["mentions"]:
            if "userId" in user and user["userId"] == self.userId:
                mention = user["screenName"]
                break

        if not mention:
            return

        mention = "@" + mention
        trigger = re.sub(r"\s*%s\s*" % re.escape(mention), " ", data["text"]).strip()

        self.write(data["fromUser"], trigger, room)

    def write(self, user, trigger, room):
        response = self.respond(user["id"], trigger)
        if response:
            self.send("@" + user["username"] + " " + response, room)

    def send(self, text, room):
        requests.post("https://api.gitter.im/v1/rooms/%s/chatMessages" % room,
            headers=self.headers, data={"text":text})
