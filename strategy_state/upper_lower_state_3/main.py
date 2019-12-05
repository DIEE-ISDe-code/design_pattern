from printer import Printer

p=Printer()


sequence=['a','a','b','c','d','e','f','x','a','d','b','c','d']
for c in sequence:
    p.writeChar(c)

# it prints
# a a b c D E F X b a d b c d