class Chain:
    def __init__(self):
        self.root = Node()

    def add_word(self, word: str):
        word = word.lower()
        self.root.update(word + ' ')

    def depth(self):
        return self.root.depth()

    def normalize(self):
        self.root.normalize()


class Node:
    def __init__(self):
        self.freq = {}
        self.next = {}

    def update(self, word: str):
        if len(word) < 1:
            return

        letter, ending = word[0], word[1:]
        self.freq[letter] = self.freq.get(letter, 0) + 1
        if letter not in self.next:
            self.next[letter] = Node()
        self.next[letter].update(ending)

    def normalize(self):
        count = sum(self.freq.values())
        for k in self.freq.keys():
            self.freq[k] = self.freq[k] / count
            self.next[k].normalize()

    def depth(self):
        mx = 0
        for k in self.next:
            d = self.next[k].depth() + 1
            if d > mx:
                mx = d
        return mx
