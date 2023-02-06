scores = []

with open('scores.csv', 'r') as f:
    for line in f:
        l = line.split(';')
        s = int(l[1].strip('\n'))
        scores.append({'name':l[0], 'score':s})


print(scores)

with open('scores.csv', 'w') as f:
    for score in scores:
        f.write(f"{score['name']};{score['score']}")
        f.write('\n')


