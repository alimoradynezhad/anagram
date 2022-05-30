import os
with open("tst.txt") as f:
    deta = f.readlines()


deta2 =sorted(set([word.strip().lower() for word in deta]))


def signiture(word):
    return ''.join(sorted(word))


dictionary =dict()
lst =[]
for word in deta2:
    sign = signiture(word)

    if sign not in dictionary:
        dictionary[sign] = word




    else:
        dictionary[sign].append(word)


dictionary2 = dict()                            #create new dictionary
for word2 in dictionary:                        #loop in dictionary up   Has organized data

    counter= 0                                  #create counter
    for word3 in dictionary:                    #loop in dictionary up   Has organized data
        if len(word2) == len(word3):            #Check the length of the characters together
            counter = counter + 1
            dictionary2[len(word2)] = counter   # ست دیکشنری 2 با key = طول کلمه حلقه اول
                                                #         و value = شمارنده
print(dictionary2)

