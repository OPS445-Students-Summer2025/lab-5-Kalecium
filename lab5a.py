#!/usr/bin/env python3
#Author ID: 150563211

def read_file_string(file_name):
    f = open(file_name, 'r')
    text = f.read()
    f.close()
    return text

def read_file_list(file_name):
    f = open(file_name, 'r')
    text = [] #empty list
    for line in f: #looping through line
        text.append(line.strip()) 
        #append them to file and remove trailings
    f.close()
    return text

if __name__ == '__main__':
    print(read_file_string('data.txt'))
    print(read_file_list('data.txt'))
    