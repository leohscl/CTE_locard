lines = open("./test", 'r').readlines()
lines
list_words = [w.split(' ') for w in lines]
words = []
for l in list_words:
    for w in l:
        words.append(w)
words

