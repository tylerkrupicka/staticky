import re as regex
import os
import datetime

class Pyng:

    def __init__(self):
        #set variables
        self.config = "config.txt"
        self.dict = {}

    def main(self):
        while(True):
            cmd = input("Enter Command (generate, new_post, quit): ")
            if cmd == "generate":
                self.generate()
            elif cmd == "new_post":
                self.new_post()
            elif cmd == "quit":
                break

    def generate(self):
        self.getConfig()

    def getConfig(self):
        for line in open(self.config):
            pair = line.split(": ")
            for i in range(0,len(pair)):
                pair[i] = pair[i].strip()
            self.dict[pair[0]] = pair[1]

    def new_post(self):
        print("new post")
        today = datetime.date.today()
        date = today.isoformat()
        path = "posts"
        title = input("Title: ")
        os.chdir(path)
        file=open(title+".txt", "a")
        file.write(title+"\n"+date)

if __name__ == '__main__':
    Pyng().main()

class Post:

    def __init__(self):
        self.title = ""
        self.link = ""
        self.date = ""
        self.content = ""
