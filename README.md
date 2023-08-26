# wc Lite - Unix `wc` Command Simplified

WC Lite is a simplified version of the Unix `wc` command. It provides basic functionality to count lines, words, characters, and bytes in a text file or from standard input. This project is intended as a coding challenge and a way to practice command-line argument parsing in Python.


## Table of Contents

- [Getting Started](#getting-started)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)
- [Usage](#usage)
- [Options](#options)
- [Examples](#examples)


## Getting Started

### Prerequisites

To run this script, you'll need:

- Python 3.x

### Installation

1. Clone this repository:

   git clone https://github.com/giftthedeveloper/wc-lite.git
   cd wc-lite

2. Make the script executable:

```chmod +x gwc.py ```

3. Create a symbolic link for convenience (optional):

```ln -s gwc.py gwc```

### Usage

To use WC Lite, open a terminal and navigate to the directory where the script is located. You can run the script with various options to count lines, words, characters, and bytes in a text file. You can also provide text input via standard input.

### Options

    -c: Count bytes in a text file.
    -l: Count lines in a text file.
    -w: Count words in a text file.
    -m: Count characters in a text file.
    -: Read text input from standard input.

### Examples

in my repo i already have a text.txt but you can provide a path to your text file.

Count bytes or kilobytes in a file:

```./gwc -c text.txt ```

Count lines in a file:

```./gwc -l filename.txt ```

Count words in a file:

```./gwc -w filename.txt ```

Count characters in a file:

```./gwc -m filename.txt ```

Read text input from standard input:

```./gwc - ```

This is a test input.
Press Enter when done or Ctrl D

