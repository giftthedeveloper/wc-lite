#!/usr/bin/env python3
import argparse
import sys

def count_bytes(filename):
    #function to count the number of bytes in a text
    with open(filename, 'rb') as file:
        content = file.read()
        byte_count = len(content)
        return byte_count

def count_lines(filename):
    #function to count lines in a text file
    with open (filename, 'r') as file:
        no_of_lines = sum(1 for _ in file) 
        return no_of_lines
    
def count_words(filename):
    #function to count words by whitespace
    with open (filename, 'r') as file:
        content = file.read()
        words = content.split()
        no_of_words = len(words)
        return no_of_words

def count_characters(filename):
    #function to count characters using utf-8 encoding to handle multi byte characters
    with open (filename, 'r', encoding='utf-8') as file:
        content = file.read()
        char_count = len(content)
        return char_count

def read_input():
    return sys.stdin.read()


def main():
    #user help menu
    parser = argparse.ArgumentParser(description='simplified unix wc version by Gift Jeremiah')
    parser.add_argument('-c', action='store_true', help='Count bytes in a text file')
    parser.add_argument('-l', action='store_true', help='Count lines in a text file')
    parser.add_argument('-w', action='store_true', help='Count words in a file')
    parser.add_argument('-m', action='store_true', help='Count characters in a file')
    parser.add_argument('filename',nargs='?', help='Name of the file')

    args = parser.parse_args()

    if args.filename == '-':
        content = read_input()
        line_count = content.count('\n')
        word_count = len(content.split())
        char_count = len(content)
        byte_count = len(content.encode()) 
        print(f"{byte_count} bytes, {word_count} words, {char_count} characters, {line_count} lines")
    
    
    #if -c flag is passed, 
    if args.c:
        bytes_count = count_bytes(args.filename)
        kb_count = bytes_count/1024
        print (f"{args.filename} is {bytes_count} bytes and roughly {kb_count} kilobyte")

    #if the -l flag is passed
    elif args.l:
        line_count = count_lines(args.filename)
        print(f"{line_count} lines in {args.filename}")

    #if the =w flag is passed
    elif args.w:
        word_count = count_words(args.filename)
        print(f"There are {word_count} words in {args.filename}")

    #if the -m argument is passed
    elif args.m:
        character_count = count_characters(args.filename)
        print(f'{args.filename} has {character_count} characters')

    #setting the defualt behaivour to give every detail about the file
    else:  # Default behavior
        word_count = count_words(args.filename)
        character_count = count_characters(args.filename)
        lines_count = count_lines(args.filename)
        bytes_count = count_bytes(args.filename)
        print(f"{bytes_count} bytes, {word_count} words, {character_count} characters, {lines_count} lines")

    
if __name__ == '__main__':
    main()
