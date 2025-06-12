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

def append_file_string(file_name, string_of_lines):
    f = open(file_name, 'a')
    f.write(string_of_lines) #write to the bottom of file
    f.close()

def write_file_list(file_name, list_of_lines):
    f = open(file_name, 'w')
    for word in list_of_lines: #Looping through each list item
        f.write(word + '\n')
        #append the line with line spacing
    f.close()

def copy_file_add_line_numbers(file_name_read, file_name_write):
    line_no = 0 #line counter
    f1 = open(file_name_read, 'r')
    f2 = open(file_name_write, 'w')
    for line in f1: #looping through each lines in the read file
        line_no += 1
        f2.write(str(line_no) + ':' + line)
    f1.close() 
    f2.close()

if __name__ == '__main__':
    file1 = 'seneca1.txt'
    file2 = 'seneca2.txt'
    file3 = 'seneca3.txt'
    string1 = 'First Line\nSecond Line\nThird Line\n'
    list1 = ['Line 1', 'Line 2', 'Line 3']
    append_file_string(file1, string1)
    print(read_file_string(file1))
    write_file_list(file2, list1)
    print(read_file_string(file2))
    copy_file_add_line_numbers(file2, file3)
    print(read_file_string(file3))