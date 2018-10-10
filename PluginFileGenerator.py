#!/usr/bin/python

import sys

def main(argv):
    splitArgs = [x.strip() for x in argv[0].split(',')]

    with open('plugin.txt', 'w') as the_file:
        for line in splitArgs:
            the_file.write(line + '\n')
    
if __name__ == "__main__":
   main(sys.argv[1:])
