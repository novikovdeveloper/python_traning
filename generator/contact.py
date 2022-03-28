from model.contact import Contact
import random
import string
import os.path
import json
import getopt
import sys

try:
    opts, args = getopt.getopt(sys.argv[1:], "n:f:", ["number of contacts", "file"])
except getopt.GetoptError as err:
    getopt.usage()
    sys.exit(2)

n = 5
f = "data/contacts.json"

for o, a in opts:
    if 0 == "-n":
        n = int(a)
    elif o == "-f":
        f = a




def random_string(prefix, maxlen):
    symbols = string.ascii_letters + string.digits
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])


testdata = [Contact(firstname="", middlename="", lastname="", nickname="", title="",
            company="", address="", home="", work="", mobile="",
            email="", email2="", email3="")] + [Contact(firstname=random_string("Alex", 5), middlename=random_string("Middle", 10), lastname=random_string("Bolduin", 5),
                                             nickname=random_string("vasua228", 10), title=random_string("no title", 5), company=random_string("roga i kopita", 10), address=
                             random_string("Moscow,Pushkina str. app 13", 20), home=random_string("123456",10), work=random_string("7891011",10), mobile=random_string("7891011",10),
            email=random_string("exam", 10), email2=random_string("exam2", 10), email3=random_string("exam2", 10))
    for i in range(n)
]

file = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", f)

with open(file, "w") as out:
    f.write(json.dumps(testdata, default=lambda x: x.__dict__, indent=2))