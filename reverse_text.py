"""Functions for reversing text files"""

import string 
import sys

def reverse_text(input_file_name, output_file_name, newlines=True):
    """Takes text input file and creates a new file with all the text flipped, NOT including punctuation. 
    For example, "Hi, I'm John" -> "John I'm Hi,"

    Args:
        input_file_name (str): Name of input file
        output_file_name (str): Name of output file.  
        newlines (bool, optional): Whether or not you want the output file to have new lines. Defaults to True.
    """
    output_file = open(output_file_name, "w")
    
    data = []
    char_count = 0

    # get info from input file
    with open(input_file_name, "r") as input_file:
        for line in input_file:     
            for word in line.split():
                data.append(word + " ") 
                    
                if newlines:
                    char_count += len(word)
                    # newlines every 100 char
                    if char_count > 100:
                        data.append("\n") 
                        char_count = 0
    
    # reverse the array
    reversed_data = data[::-1]
    
    # write the reversed list to the output file
    output_file.writelines(reversed_data)
    output_file.close()

def reverse_text_with_punctuation(input_file_name, output_file_name, newlines=True):
    """Takes text input file and creates a new file with all the text flipped, including punctuation.
    For example, "Hi, I'm John" -> "John I'm ,Hi"

    Args:
        input_file_name (str): Name of input file
        output_file_name (str): Name of output file. 
        newlines (bool, optional): Whether or not you want the output file to have new lines. Defaults to True.
    """
    output_file = open(output_file_name, "w")
    
    data = []
    char_count = 0

    # get info from input file
    with open(input_file_name, "r") as input_file:
        for line in input_file:     
            for word in line.split():
                if word[-1] in string.punctuation:
                    # if the word has punctuation attached to the end, seperate them and add the word first
                    data.append(word[:-1] + " ")
                    data.append(word[-1])
                else:           
                    data.append(word + " ")
                    
                if newlines:
                    char_count += len(word)
                    # newlines every 100 char
                    if char_count > 100:
                        data.append("\n") 
                        char_count = 0
    
    # reverse the array
    reversed_data = data[::-1]
    
    # write the reversed list to the output file
    output_file.writelines(reversed_data)
    output_file.close()
    
def main():
    if len(sys.argv) > 1: # use command line args
        print("Usage: python3 reverse_text.py [name of text file in current directory to be reversed]")
        input_file_name = sys.argv[1]
        name = input_file_name.split(".")[0]
        
        reverse_output_name = name + "_reversed.txt"
        reversed_wpunc_output_name = name + "_reversed_wpunc.txt"
        
        reverse_text(input_file_name, reverse_output_name)
        reverse_text_with_punctuation(input_file_name, reversed_wpunc_output_name)
        print("Files Generated: " + reverse_output_name + ", " + reversed_wpunc_output_name)
    else: # change these file names manually to run without command line args
        reverse_text("data/input.txt", "data/output.txt")
        reverse_text_with_punctuation("data/input.txt", "data/punc_output.txt")

if __name__ == "__main__":
    main()