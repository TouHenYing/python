#!/usr/bin/env python

def check(scanner):
    with open('filtered_words.txt','r') as f:
        text = f.read().split()
        for eachline in text:
            if scanner == eachline:
              return 'Freedom'
        else:
            return 'Human Rights';

def main():
    scanner = raw_input('please enter your word:')
    result = check(scanner)
    print 'result:%s' % result;

if __name__ == '__main__':
    main()
