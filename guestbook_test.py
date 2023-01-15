import json
import os

def test_add():
    os.system("python guestbook.py new First")
    with open("guestbook.txt", "r") as f:
        guestbook = json.load(f)
    assert guestbook[0] == "First"
    os.remove("guestbook.txt")

def test_list():
    os.system("python guestbook.py new First")
    os.system("python guestbook.py new Second")
    os.system("python guestbook.py list > output.txt")
    with open("output.txt", "r") as f:
        output = f.read()
    assert "First" in output
    assert "Second" in output
    os.remove("guestbook.txt")
    os.remove("output.txt")

def test_edit():
    os.system("guestbook.py new First")
    os.system("guestbook.py edit 0 Edited")
    with open("guestbook.txt", "r") as f:
        guestbook = json.load(f)
    assert guestbook[0] == "Edited"
    os.remove("guestbook.txt")

def test_delete():
    os.system("guestbook.py new First")
    os.system("guestbook.py new Second")
    os.system("guestbook.py delete 0")
    with open("guestbook.txt", "r") as f:
        guestbook = json.load(f)
    assert guestbook[0] == "Second"
    os.remove("guestbook.txt")
