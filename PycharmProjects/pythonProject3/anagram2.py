import os
with open("tst.txt") as f:
    deta = f.readlines()

#print(deta)
deta2 =sorted(set([word.strip().lower() for word in deta]))
print(deta2)

def signiture(word):
    return ''.join(sorted(word))


dictionary =dict()

for word in deta2:
    sign = signiture(word)
    if sign not in dictionary:
        dictionary[sign] = word

    else:
        dictionary[sign].append(word)

print(dictionary)