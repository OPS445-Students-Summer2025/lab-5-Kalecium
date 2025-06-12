#!/usr/bin/env python3
# Author ID: 150563211

def add(number1, number2):
    #Add two numbers together, return the result, if error return string 'error: could not add numbers'
    try:
        int(number1)
        int(number2)
        result = int(number1) + int(number2)
    except (ValueError):
        result = 'error: could not add numbers'
    
    return result

def read_file(filename):
    # Read a file, return a list of all lines, if error return string 'error: could not read file'
    try:
        f = open(filename, 'r')
        text = []
        for line in f:
            text.append(line)
        f.close()
    except(FileNotFoundError):
        text = 'error: could not read file'
    return text

if __name__ == '__main__':
    print(add(10,5))                        # works
    print(add('10',5))                      # works
    print(add('abc',5))                     # exception
    print(read_file('seneca2.txt'))         # works
    print(read_file('file10000.txt'))       # exception