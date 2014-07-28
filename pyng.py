import re as regex
import os
import datetime
"""
pyng is a static site generator
Created by: Tyler Krupicka and James Dolan
"""

class Post:

    def __init__(self):
        #variables for each post  
        self.title = ""
        self.link = ""
        self.date = ""
        self.content = ""

class Pyng:

    def __init__(self):
        #variables
        self.config = "config.txt"
        self.dict = {}
        self.posts = []

    def main(self):
        #ask the user what task to perform until quit
        while(True):
            cmd = input("Enter Command (generate, new_post, quit): ")
            if cmd == "generate":
                self.generate()
            elif cmd == "new_post":
                self.new_post()
            elif cmd == "quit":
                break

    def generate(self):
        #generate the site by moving pages and filling in text
        self.getConfig()
        self.loadPosts()
        self.replaceContent()

    def getConfig(self):
        #load all the config variables in to a dictionary
        for line in open(self.config):
            pair = line.split(": ")
            for i in range(0,len(pair)):
                pair[i] = pair[i].strip()
            self.dict[pair[0]] = pair[1]

    def replaceContent(self):
        s=open("index.html", 'r+', encoding="utf8")
        page = ''
        for a in s:
            page += a
        for key in self.dict:
            page = page.replace('[[' + key + ']]',self.dict[key])
        s.seek(0)
        s.truncate()
        s.write(page)
        s.close()

    def loadPosts(self):
        #make each post file a class and then store them in a list
        for filename in os.listdir("posts"):
            #dont add the git ignore
            if filename == ".gitignore":
                pass
            else:
                post = Post()
                p = ""
                for line in open("posts/" + filename):
                    p += line.strip()
                pl = p.split("---")
                head = pl[0].split("Date: ")

                #determine title and date
                post.title = head[0].replace("Title: ", '')
                post.date = head[1]
                post.content = pl[1]

                self.posts.append(post)

        #sort the list of posts by date
        self.posts.sort(key=lambda x: x.date, reverse=True)
                    
    def new_post(self):
        #create a new post file with the desired header information
        today = datetime.date.today()
        date = today.strftime('%B %d, %Y')
        title = input("Title: ")
        valid_chars = '-_.() abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'
        filename = ''.join(c for c in title if c in valid_chars)
        os.chdir("posts")
        file=open(filename+".txt", "a")
        file.write("Title: " + title + "\n" + "Date: " + date + "\n---\n")
        file.close()
        os.chdir("..")
        print("Post file created. Be careful editing the post header formatting.")

if __name__ == '__main__':
    Pyng().main()
