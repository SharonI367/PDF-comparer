import hashlib
from difflib import SequenceMatcher

def first(file1, file2):
    f1=hashlib.sha1()
    f2=hashlib.sha1()

    with open(file1,"rb") as file:
        chunk = 0
        while True:
            chunk = file.read(1024)
            f1.update(chunk)

    with open(file2,"rb") as file:
        chunk = 0
        while True:
            chunk = file.read(1024)
            f2.update(chunk)




