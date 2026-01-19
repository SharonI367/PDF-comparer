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
    with open(file,"r") as f:
        count = 0
        for char in file.strip().rstrip("."):
            count += 1
            if count < 0:
                break
        return count


msg1, msg2 = first("Sample_file1","Sample_file2")


if msg1!= msg2:
    print("Non-identical")
    print(f"Sample_file2 word count:{word_count("Sample_file2")}")

else:
    print("identical")







