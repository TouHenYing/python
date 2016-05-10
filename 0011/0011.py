#!/usr/bin/env python

def check(scanner):
    f = open('filtered_words.txt','r')
    for eachline in f.readlines():
        if input == eachline:
            return 'Freedom'
    else:
        return 'Human Rights';

def main():
    scanner = raw_input('please enter your word!')
    result = check(scanner)
    print 'result:%s' % result;

if __name__ == '__main__':
    main()
