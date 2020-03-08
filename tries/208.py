# 208. Implement Trie (Prefix Tree)

class Trie(object):

    def __init__(self):
        self.trie = dict()
        self.end = '*'

    def insert(self, word):
        tempTrie = self.trie
        for letter in word:
            if letter in tempTrie:
                tempTrie = tempTrie[letter]
            else:
                tempTrie = tempTrie.setdefault(letter, {})
        tempTrie[self.end] = self.end

    def search(self, word):
        tempTrie = self.trie
        for letter in word:
            if letter in tempTrie:
                tempTrie = tempTrie[letter]
            else:
                return False
        return self.end in tempTrie

    def startsWith(self, prefix):
        tempTrie = self.trie
        for letter in prefix:
            if letter in tempTrie:
                tempTrie = tempTrie[letter]
            else:
                return False
        return True


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
