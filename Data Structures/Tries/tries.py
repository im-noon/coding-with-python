# prefix trees


ALPHABET_SIZE = 26

class Node(object):
    """
    The container contain the given value of the node
    """
    def __init__(self, character, value):
        # node are character in a trie
        self.character = character

        # dictionary like key(char)- value(value) pairs
        self.value = value

        # every node may have several child: this is why tries are not memory
        # efficient, every node has 26 child no matter they needed or not
        self.child = [None for _ in range(ALPHABET_SIZE)]

        # tracking the end if given word in the tree
        # leaf nodes are then end if given word in the three
        self.isleaf = False


class Trie(object):
    """
    The prefix trees implementation
    """

    def __init__(self):
        # the root node is an empty: here we use *
        self.root = Node('*', None)

    def ascii_index(self, char):
        """
        Helper function to transform character to ascii inde
        :param char: character
        :return: index
        """
        return  ord(char) - ord('a')

    def insert(self, word, value):
        """
        Inserting the word, the running time complexity take O(M) where M is
        the length of the word
        :param word: key pair
        :param value: value pair
        :return: None
        """

        # always start at the root
        current = self.root

        # consider all character in the word
        for char in word:

            # we are dealing with indexes: user ascii representation to get
            # the index and transform within the range [0, ALPHABET_SIZE]
            ascii_index = self.ascii_index(char)

            # there may be a child of the given letter
            if current.child[ascii_index]:
                current = current.child[ascii_index]
            else:
                # insert new node with the given char
                node = Node(char, value)
                current.child[ascii_index] = node
                current = node

        # after considered all the character of the word, then mark the leaf
        # node to represent the end of word
        current.isleaf = True

    def search(self, word):
        """
        Check weather given word is represent in the tree or not
        Running time complexity is O(M)
        :param word: given word
        :return: value pair if word exist otherwise None
        """

        #if the the is empty then terminate
        if not self.root.child:
            return None

        # always start from root
        current = self.root

        # consider all char in the word
        for char in word:

            # we are dealing with the indexes  : use ascii representation to
            # get index if and transform within the range [0, ALPHABET_SIZE]
            ascii_index = self.ascii_index(char)

            # the letter presented in the tree
            if current.child[ascii_index]:
                # keep going
                current = current.child[ascii_index]
            else:
                # word is not present in the tree
                return None

        # if we've consider all the character and the actual node is leaf,
        # that mean we found the given word
        if current.isleaf:
            return current.value

        # not found
        return None



    def sort(self):
        """
        Get all word in sorted order
        :return: sorted words
        """
        if self.root:
            return self.get_words_prefix('')


    def longest_common_prefix(self):
        """
        Finding the longest common prefix
        :return: the LCP string
        """

        # always start from the root
        current = self.root

        # the representation of longest common prefix string
        lpc = None


        while not current.isleaf:
            # compute the number of children and index of the node
            child_count, child_index = self.get_child_count(current)

            # if there are more than 1 child, we have to stop
            if child_count != 1:
                break

            # consider the next node if current node have single child
            current = current.child[child_index]

            # keep building the lpc string
            if not lpc:
                lpc += str(current.character)
            else:
                lpc = str(current.character)

        return lpc

    def get_child_count(self, node):
        """
        Helper function, compute the child count and index of the given node
        :param node: the node to compute
        :return: tuple of child number and index
        """
        child_count = 0
        child_index = 0

        # compute the number of child and store index
        for index, child in enumerate(node.child):
            if child:
                child_count += 1
                child_index = index

        return child_count, child_index

    def get_words_prefix(self, prefix):
        """
        Gather the words with the same prefix
        :param prefix: string in word
        :return: word list
        """

        # store the words in the list
        all_words = []

        # always start from the root
        current = self.root

        # consider all character in the prefix
        for char in prefix:
            # we are dealing with the indexes  : use ascii representation to
            # get index if and transform within the range [0, ALPHABET_SIZE]
            ascii_index = self.ascii_index(char)


            # if there no solution
            if not current.child[ascii_index]:
                return Node

            current = current.child[ascii_index]

        # collected all the words starting with the same prefix
        self.collect(current, prefix, all_words)

        return all_words

    def collect(self, node, prefix, all_words):
        """
        Collect all words with the common prefix
        :param node: start node
        :param prefix: prefix string
        :param all_words: word list store
        :return: None
        """
        if not node:
            return

        # if leaf nodes represent valid words
        if node.isleaf:
            all_words.append({prefix:node.value})

        # keep going and consider the next node
        for child in node.child:

            # if the child is None the consider the next child in the same level
            if not child:
                continue

            # keep going down
            char_in_child = child.character
            self.collect(child, prefix + char_in_child, all_words)



if __name__ == "__main__":
    trie = Trie()

    trie.insert('sea', 9)
    trie.insert('seashore', 8)
    trie.insert('apple', 7)
    trie.insert('banana', 6)
    trie.insert('amazing', 5)
    trie.insert('banana', 4)
    trie.insert('octopus', 3)
    trie.insert('nominee', 2)
    trie.insert('she', 1)
    trie.insert('adam', 2)
    trie.insert('kevin', 3)
    trie.insert('adamma', 4)
    trie.insert('shell', 5)
    trie.insert('seashore', 6)


    print(trie.sort())

    print(trie.longest_common_prefix())

    print(trie.search('computer'))

    print(trie.search('shell'))