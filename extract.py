#!/usr/bin/env python
"""
PHP heredoc gettext extractor
Copyright (C) 2012 Dafydd Crosby

This script pulls gettext translations out of PHP heredoc strings

USAGE:
extract.py [files]

TODO:
cleaner searching of gettext strings

Permission is hereby granted, free of charge, to any person obtaining a copy of
this software and associated documentation files (the "Software"), to deal in 
the Software without restriction, including without limitation the rights to 
use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies 
of the Software, and to permit persons to whom the Software is furnished to do 
so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all 
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR 
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, 
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE 
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER 
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, 
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE 
SOFTWARE.
"""

import sys

DEBUG = True
KEYWORD = "_"

def check_file(filepath):
    try:
        handle = open(filepath, "r")
    except IOError, err:
        print(err)
        return []

    inheredoc = False
    heredoc_word = ''
    ingettext = False
    heredoc_string = ''
    gettext_strings = []
    for line in handle:
        line = line.strip()
        if not inheredoc:
            index = line.find('<<<')
            if index < 0:
                # Didn't find anything, move along
                pass
            else:
                heredoc_word = line[index+3:]
                inheredoc = True
                if DEBUG:
                    print('found heredoc word: ' + heredoc_word)
        else:
            if line == heredoc_word or line == heredoc_word + ";":
                inheredoc = False
                if DEBUG:
                    print('exiting heredoc word: ' + heredoc_word)
                gettext_strings.join(search_heredoc_string(heredoc_string))
                heredoc_string = ""
            else:
                heredoc_string.join(line)

def search_heredoc_string(string):
    """
    Go through the heredoc string itself and search for
    gettext strings, returning an array
    """
    gettext_strings = []
    index = 0
    result = -1
    needle_beg = '{$' + KEYWORD + '('
    beg_offset = len(needle_beg) + 1
    needle_end = ')}'
    keepgoing = True
    while keepgoing == True:
        result = string.find(needle_beg, index)
        if result >= 0:
            slice_start = result + beg_offset
            index = result + 1
            result = string.find(needle_end, index)
            if result >= 0:
                # We subtract one from the slice_end to deal with the ending
                # quotation mark
                slice_end = result - 1
                gettext_strings.append(string[slice_start:slice_end])
        else:
            keepgoing = False  
         
    return gettext_strings
    
def output_messages_file(output_file, messages):
    pass

def main():
    php_files = sys.argv[1:]
    output_file = "messages.po"
    messages = []
    
    if DEBUG:
        print(php_files)

    for filepath in php_files:
        messages.append(check_file(filepath))

if __name__ == "__main__":
    main()
