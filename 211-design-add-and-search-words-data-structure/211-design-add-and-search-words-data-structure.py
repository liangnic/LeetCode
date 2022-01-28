class WordNode:
    def __init__(self):
        self.words = {}
        self.isEnd = False

class WordDictionary:

    def __init__(self):
        self.root = WordNode()
        
    def addWord(self, word: str) -> None:
        node = self.root
        
        for w in word:
            if w in node.words:
                node = node.words[w]
            else:
                node.words[w] = WordNode()
                node = node.words[w]
        node.isEnd = True
        
    def search(self, word: str) -> bool:
        
        stack = [(self.root,word)]
        while stack:
            node, w = stack.pop()
            if not w:
                if node.isEnd:
                    return True
            elif w[0]=='.':
                for n in node.words.values():
                    stack.append((n,w[1:]))
            else:
                if w[0] in node.words:
                    n = node.words[w[0]]
                    stack.append((n,w[1:]))
        return False


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)