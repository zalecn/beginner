class TrieNode():
    def __init__(self):
        self.count = 0   # 统计单词前缀出现的次数
        self.next = {}   # 指向各个子树
        self.exist = False  # 标记该结点处是否构成单词

    def insert(self, word):
        if len(word) == 0:
            return
        node = self
        for c in word:
            if c not in node.next:
                node.next[c] = TrieNode()
            node = node.next[c]
            node.count += 1
        node.exist = True

    def search(self, word):
        if len(word) == 0:
            return False

        node = self
        for c in word:
            if c not in node.next:
                return False
            node = node.next[c]
        return node.exist




if __name__ == "__main__":
    root = TrieNode()
    root.insert("insert")
    root.insert("root")
    root.insert("test")
    root.insert("create")
    root.insert("created")

    print("ro: ")
    print(root.search("ro"))
    print("roo: ")
    print(root.search("roo"))
    print("root: ")
    print(root.search("root"))
    print("")
    print(root.search(""))
    print("rot: ")
    print(root.search("rot"))
    print("insert")
    print(root.search("insert"))
