import unittest
from huffman import *


class HuffTest(unittest.TestCase):
    # tests function: count_occurrences
    def test_count_occ_abc(self):
        expected = {}
        expected['a'] = 1
        expected['b'] = 1
        expected['c'] = 1
        file = open('test1.txt', 'r')
        result = count_occurrences(file)
        self.assertEqual(expected, result)

    # tests function: count_occurrences
    def test_count_occ_new_line(self):
        expected = {}
        expected['1'] = 5
        expected['\n'] = 4
        file = open('test2.txt', 'r')
        result = count_occurrences(file)
        self.assertEqual(expected, result)

    # tests function: count_occurances
    def test_count_occ_space(self):
        expected = {}
        for char in 'what\'s up?':
            expected[char] = 1
        file = open('test3.txt', 'r')
        result = count_occurrences(file)
        self.assertEqual(expected, result)

    # tests function: tree_from_dict
    def test_tfd_three_entries(self):
        input = {}
        input['a'] = 1
        input['b'] = 6
        input['c'] = 2
        expected = Node(9, Leaf('b', 6), Node(3, Leaf('c', 2), Leaf('a', 1)))
        result = tree_from_dict(input)
        self.assertEqual(expected, result)

    # tests function: tree_from_dict
    def test_tfd_same_freq(self):
        input = {}
        input['a'] = 1
        input['b'] = 1
        input['c'] = 1
        expected = Node(3, Node(2, Leaf('b', 1), Leaf('a', 1)), Leaf('c', 1))
        result = tree_from_dict(input)
        self.assertEqual(expected, result)

    # tests function: tree_to_dict
    def test_tfd_5_entries(self):
        input = {}
        input[' '] = 5
        input['\n'] = 2
        input['a'] = 1
        input['1'] = 4
        input['?'] = 3
        expected = Node(15, Node(9, Leaf(' ', 5), Leaf('1', 4)),
                            Node(6,
                                 Node(3, Leaf('\n', 2), Leaf('a', 1)),
                                 Leaf('?', 3)))
        result = tree_from_dict(input)
        self.assertEqual(expected, result)

    # tests function: hufftree_lt
    def test_comparator_two_leafs(self):
        leaf1 = Leaf('a', 2)
        leaf2 = Leaf('b', 1)
        self.assertEqual(hufftree_lt(leaf1, leaf2), 1)

    # tests function: hufftree_lt
    def test_comparator_one_leaf_one_node(self):
        leaf = Leaf('abc', 3)
        node = Node(3, None, None)
        self.assertEqual(hufftree_lt(leaf, node), 0)

    # tests function: hufftree_lt
    def test_comparator_two_nodes(self):
        node1 = Node(3, None, None)
        node2 = Node(2, None, None)
        self.assertEqual(hufftree_lt(node2, node1), -1)

    # tests functions: codes_from_tree and encoding
    def test_codes_and_string_test4(self):
        # open the file
        file = open('test4.txt', 'r')

        # make the characters and frequencies manually
        test_dict = {}
        test_dict['a'] = 2
        test_dict['b'] = 3
        test_dict['c'] = 1
        test_dict['d'] = 4

        # make the tree
        test_tree = tree_from_dict(test_dict)

        # get the codes
        result = codes_from_tree(test_tree)

        # make the expected codes
        expected = {}
        expected['a'] = '000'
        expected['b'] = '01'
        expected['c'] = '001'
        expected['d'] = '1'

        # ensure codes are correct
        self.assertEqual(expected, result)

        # generate the final string
        result_string = encoding(file, expected)

        # make the expected final string
        expected_string = '0000100110000110111'

        # ensure strings are correct
        self.assertEqual(result_string, expected_string)

    # test function: codes_from_tree and encoding
    def test_codes_2_chars(self):
        test_dict = {}
        test_dict['a'] = 2
        test_dict['b'] = 3
        test_tree = tree_from_dict(test_dict)
        result = codes_from_tree(test_tree)
        expected = {}
        expected['a'] = '1'
        expected['b'] = '0'
        self.assertEqual(expected, result)

    # tests: full program
    def test_full_test1(self):
        input = open('test1.txt', 'r')
        output = open('output1.txt', 'w')
        ascii_count = count_occurrences(input)
        hufftree = tree_from_dict(ascii_count)
        char_codes = codes_from_tree(hufftree)
        final_string = encoding(input, char_codes)
        output.write(final_string)
        input.close()
        output.close()


if __name__ == '__main__':
    unittest.main()
