"""Functions for reversing text files"""

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
                remove_front = False
                # break the first special character off, if it is present
                if not word[0].isalpha():
                    data.append(word[0])
                    remove_front = True
                
                # find how many special characters are at the end
                back_index = -1
                while abs(back_index) < len(word):
                    #print("Back index: " + str(back_index))
                    if not word[back_index].isalpha():
                        back_index -= 1
                    else:
                        break
                    
                # add the core part of the word (word minus front and end pieces) to the data
                if remove_front and back_index < -1:
                    data.append(word[1:back_index + 1])
                elif not remove_front and back_index < -1:
                    data.append(word[:back_index + 1])
                elif remove_front and back_index == -1:
                    data.append(word[1:])
                elif not remove_front and back_index == -1:
                    data.append(word)
                    
                # add the end peices to the data
                for i in range (back_index + 1, 0, 1):
                    data.append(word[i])
                
                data.append(" ")
                
                if newlines:
                    char_count += len(word)
                    # newlines every 100 char
                    if char_count > 100:
                        data.append("\n") 
                        char_count = 0

    output_file.writelines(data[::-1])
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