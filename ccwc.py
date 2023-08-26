import argparse

def count_bytes(filename):
    #function to count the number of bytes in a text
    with open(filename, 'rb') as file:
        content = file.read()
        byte_count = len(content)
        return byte_count
    

def main():

    parser = argparse.ArgumentParser(description='simplified unix wc version')
    parser.add_argument('-c', action='store_true', help='Count bytes')
    parser.add_argument('filename', help='Name of the file')
    args = parser.parse_args()
    
    #if -c flag is passed, 
    if args.c:
        bytes_count = count_bytes(args.filename)
        print (f"{bytes_count} {args.filename}")

if __name__ == '__main__':
    main()
