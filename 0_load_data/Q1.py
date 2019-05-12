content = open("hw0_data/words.txt").read()
array = content.split()
d = dict()
l = list()

for i in array:
    if i not in l:
        l.append(i)
    if i not in d:
        d[i] = 1
    else:
        d[i] += 1

for i in range(len(l)):
    print("%s %s %s"%(l[i], i, d[l[i]]))

with open("Q1.txt", "w") as q1_text:
    for i in range(len(l)):
        if i == len(l) - 1:
            q1_text.write("%s %s %s"%(l[i], i, d[l[i]]))
        else:
            q1_text.write("%s %s %s"%(l[i], i, d[l[i]]) + "\n")