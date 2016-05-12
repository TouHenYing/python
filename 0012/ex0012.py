#!/usr/bin/env python

def check(scanner):
    with open('filtered_words.txt','r') as f:
        text = f.read().split()
        for eachline in text:
            if scanner.find(eachline) != -1:
                return scanner.replace(eachline,'*' * len(eachline))
        else:
            return scanner

def main():
    scanner = raw_input('please enter your word:')
    result = check(scanner)
    print 'result:',result

if __name__ == '__main__':
    main()

