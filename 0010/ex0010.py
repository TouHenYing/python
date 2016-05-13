#!/usr/bin/env python
import string
import random

def generate(n = 1):
    code = []
    for x in range(n):
        code.append(random.choice(string.letters))

    return code

def main():
    try:
        number = int(raw_input('please enter your code length:'))
    except ValueError,e:
        print e
    else:
        result = generate(number)
        print 'result:',result

if __name__ == '__main__':
    main()
