class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_word = False

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        current = self.root
        for letter in word:
            if letter not in current.children:
                current.children[letter] = TrieNode()
            current = current.children[letter]

        current.is_word = True

    def search(self, word):
        current = self.root
        for letter in word:
            if letter not in current.children:
                return False
            current = current.children[letter]

        return current.is_word

    def startsWith(self, prefix):
        current = self.root
        for letter in prefix:
            if letter not in current.children:
                return False
            current = current.children[letter]

        return True


def multiStringSearch(bigString, smallString):
    trie = Trie()
    res = []

    tokens = bigString.split(' ')
    for t in tokens:
        trie.insert(t)

    return [trie.startsWith(t) for t in smallString]

