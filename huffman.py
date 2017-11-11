from collections import defaultdict


# from: https://wiki.python.org/moin/HowTo/Sorting/
def cmp_to_key(mycmp):
    'Convert a cmp= function into a key= function'
    class K(object):
        def __init__(self, obj, *args):
            self.obj = obj
        def __lt__(self, other):
            return mycmp(self.obj, other.obj) < 0
        def __gt__(self, other):
            return mycmp(self.obj, other.obj) > 0
        def __eq__(self, other):
            return mycmp(self.obj, other.obj) == 0
        def __le__(self, other):
            return mycmp(self.obj, other.obj) <= 0
        def __ge__(self, other):
            return mycmp(self.obj, other.obj) >= 0
        def __ne__(self, other):
            return mycmp(self.obj, other.obj) != 0
    return K


# a HuffTree is one of:
# - a Leaf()
# - a Node()
# - None
class Leaf:
    def __init__(self, char, freq):
        self.char = char # a char
        self.freq = freq # a number

    def __eq__(self, other):
        return (type(other) == Leaf
		    and self.char == other.char
		    and self.freq == other.freq)

    def __repr__(self):
        return "Leaf({!r}, {!r})".format(self.char, self.freq)

    def __lt__(self, other):
        return self.freq < other.freq


class Node:
    def __init__(self, freq, left, right):
        self.freq = freq # a number
        self.left = left # a HuffTree
        self.right = right # a HuffTree

    def __eq__(self, other):
        return (type(other) == Node
			and self.freq == other.freq
			and self.left == other.left
			and self.right == other.right)

    def __repr__(self):
        return "Node({!r}, {!r}, {!r})".format(self.freq,
						self.left, self.right)


# a FileName is a string representing the name of a file in your directory


# FileName, Filename -> HuffTree
# writes the Huffman encoding of the input filename to the output filename
# NOTE: include the .txt file extension when calling
def huffman_encode(input, output):
    try:
        input_file = open(input, 'r')
    except:
        print('\nError opening file.\n')
        quit()

    # get the frequency of each character
    # ascii_count - Dictionary
    # key - char in the text file
    # value - number of times it occurs
    ascii_count = count_occurrences(input_file)

    # create the huffman tree
    # htree - Huffman Tree created from ascii_count
    htree = tree_from_dict(ascii_count)

    # get the codes for each character
    # codes - Dictionary
    # key - char in the text file
    # value - it's encoding inside htree
    codes = codes_from_tree(htree)

    # create the final string
    # output_string - string containing the full encoding
    output_string = encoding(input_file, codes)

    # write the string to the resultant file
    output_file = open(output, 'w')
    output_file.write(output_string)

    # close the files
    input_file.close()
    output_file.close()


# File, Dictionary -> String
# returns the encoding given each character key and the text file
def encoding(file, codes):
    # reset the file's line position
    file.seek(0)

    # encode the string
    result = ''
    for line in file:
        for char in line:
            result += codes[char]
    return result


# File -> Dictionary
# returns a dict with the # of times each ASCII character occurs in given file
def count_occurrences(file):
    result = defaultdict(int)
    for line in file:
        for char in line:
            result[char] += 1
    return result


# Dictionary -> HuffTree
# returns a HuffTree from the given dictionary
def tree_from_dict(dic):
    # turn the dictionary into a list
    result = []
    for char, freq in dic.items():
        result.append(Leaf(char, freq))

    # sort the list, make a node out of the smallest 2 values
    while len(result) > 1:
        result = sorted(result, key=cmp_to_key(hufftree_lt))
        node1 = result.pop(0)
        node2 = result.pop(0)
        result.append(Node(node1.freq + node2.freq, node2, node1))
    return result[0]


# HuffTree -> Number
# compares the two given HuffTrees
def hufftree_lt(tree1, tree2):
    if tree1 is None or tree2 is None:
        print('Error comparing HuffTrees. One or more tree is None.')
        quit()
    return tree1.freq - tree2.freq


# HuffTree -> Dictionary
# returns the traversal codes for a given HuffTree
def codes_from_tree(tree, result={}, str=''):
    if type(tree) is Leaf or tree is None:
        result[tree.char] = str
    else:
        codes_from_tree(tree.left, result, str + '0')
        codes_from_tree(tree.right, result, str + '1')
    return result


# FileName -> Number
# returns the number of characters in the given file
def char_count(filename):
    file = open(filename, 'r')
    tot = 0
    for line in file:
        for char in line:
            tot += 1
    file.close()
    return tot
