import os
with open("tst.txt") as f:
    deta = f.readlines()

#print(deta)
deta2 =sorted(set([word.strip().lower() for word in deta]))
print(deta2)