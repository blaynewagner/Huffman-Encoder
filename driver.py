# Usage: python3 driver.py <inFilename> <outFilename>
# include '.txt' extension on filenames


import huffman
import sys


def main():
    if len(sys.argv) < 3:
        print("\nUsage: python3 driver.py <inFilename> <outFilename>\n"
              "Include \'.txt\' extension on filenames.\n")
        quit()

    in_file = sys.argv[1]
    out_file = sys.argv[2]

    huffman.huffman_encode(in_file, out_file)

    input_bit_count = huffman.char_count(in_file)*8
    output_bit_count = huffman.char_count(out_file)

    print('\nFile encoded. The original file contained ' + str(input_bit_count)  + ' bits, while '
            'the encoded file contains ' + str(output_bit_count) + ' bits. The original file was '
            'reduced to ' + str(round(float(output_bit_count/input_bit_count)*100, 1)) + ' % of '
            'it\'s original size.\n')


if __name__ == "__main__":
    main()
