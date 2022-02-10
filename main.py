import fileinput
import pickle

from Chain import Chain

chain = Chain()
counter = 0
for word in fileinput.input('data/words.txt'):
    word = word.strip()
    chain.add_word(word)
    counter += 1
    if counter % 1000 == 0:
        print(counter)

print(chain.depth())
chain.normalize()

pickle.dump(chain, open('chain.pickle', 'wb'))

print(chain)
