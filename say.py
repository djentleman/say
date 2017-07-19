import os

def say(word):
    os.popen('say ' + str(word))
