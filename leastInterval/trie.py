class TrieNode:
    def __init__(self):
        # Initialize a TrieNode with children and a flag for end of word
        self.children = {}
        self.is_end_of_word = False


class Trie:
    def __init__(self):
        # Initialize the Trie with a root node
        self.root = TrieNode()

    def insert(self, word):
        # Insert a word into the Trie
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.is_end_of_word = True  # Mark the end of the word

    def search(self, word):
        # Search for a word in the Trie
        node = self.root
        for char in word:
            if char not in node.children:
                return False
            node = node.children[char]
        return node.is_end_of_word  # Return True if it's the end of a word

    def startsWith(self, prefix):
        # Check if any word in the Trie starts with the given prefix
        node = self.root
        for char in prefix:
            if char not in node.children:
                return False
            node = node.children[char]
        return True
