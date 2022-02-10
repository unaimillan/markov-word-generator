import pickle
import random

chain = pickle.load(open('chain.pickle', 'rb'))
print('Chain loaded')

# items = sorted(chain.root.freq.items(), key=lambda x: x[1], reverse=True)
# for k, v in items:
#     print(k, v)
inp = ''

while inp == '':
    cur = chain.root
    while len(cur.next) != 0:
        freqs = sorted(cur.freq.items(), key=lambda x: x[1], reverse=True)
        prop = random.random()
        pos = 0
        while prop > freqs[pos][1]:
            prop -= freqs[pos][1]
            pos += 1
        letter = freqs[pos][0]
        print(letter, end='')
        cur = cur.next[letter]
    inp = input()
