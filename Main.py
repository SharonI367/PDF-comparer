import hashlib
from difflib import SequenceMatcher

def first(file1, file2):
    f1=hashlib.sha1()
    f2=hashlib.sha1()

    with open(file1,"rb") as file:
        chunk = 0
        while chunk != b'':
            chunk = file.read(1024)
            f1.update(chunk)

    with open(file2,"rb") as file:
        chunk = 0
        while chunk != b'':
            chunk = file.read(1024)
            f2.update(chunk)

        return f1.hexdigest(), f2.hexdigest()

def word_count(file):
    count = 0
    with open(file,"r") as f:
        l = f.read()
        m = l.split()
        for i in m:
            count += 1
            if count< 0:
                break
        return f"{file} word count:{count}"


msg1, msg2 = first("Sample_file1","Sample_file2")

if msg1!= msg2:
    print("Non-identical")
    print(word_count("Sample_file1"))
    print(word_count("Sample_file2"))

else:
    print("identical")







