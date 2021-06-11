import os
a = int(input(" 'a'000 0000  choose the number 'a' (enter 0 to create all 8 digit combinations) : "))
b = 0
c = 0
d = 0
e = 0
f = 0
g = 0
h = 0

x = 0

dr = os.getcwd()+"/pass.txt"

file = open(dr, "w")
while x != "99999999":
    x = str(a) + str(b) + str(c) + str(d) + str(e) + str(f) + str(g) + str(h)
    file.write(x+"\n")
    h += 1
    if h == 10:
        h = 0
        g += 1
    if g == 10:
        g = 0
        f += 1
    if f == 10:
        f = 0
        e += 1
    if e == 10:
        e = 0
        d += 1
    if d == 10:
        d = 0
        c += 1
    if c == 10:
        c = 0
        b += 1
    if b == 10:
        print(x)
        b = 0
        a += 1
