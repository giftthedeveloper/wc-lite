import argparse

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

def main():

    parser = argparse.ArgumentParser(description='simplified unix wc version')
    parser.add_argument('-c', action='store_true', help='Count bytes in a text file')
    parser.add_argument('-l', action='store_true', help='Count lines in a text file')
    parser.add_argument('filename', help='Name of the file')
    args = parser.parse_args()
    
    #if -c flag is passed, 
    if args.c:
        bytes_count = count_bytes(args.filename)
        kb_count = bytes_count/1024
        print (f"{args.filename} is {bytes_count} bytes and roughly {kb_count} kilobyte")

    #if the -l flag is passed
    if args.l:
        line_count = count_lines(args.filename)
        print(f"{line_count} lines in {args.filename}")

if __name__ == '__main__':
    main()
