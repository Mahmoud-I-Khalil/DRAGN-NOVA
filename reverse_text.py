"""
With this code, punctuation is not flipped. So if you had the sentence 
"I have a dog, his name is Buddy", it would be flipped to be 
"Buddy is name his dog, a have I"
""" 

# Open the file in write mode
f2 = open("output.txt", "w")
  
data = []

# Open the input file again and get 
# the content as list to a variable data
with open("input.txt", "r") as myfile:
    for line in myfile:
        # reading each word        
        for word in line.split():
            # add the words           
            data.append(word + " ") 
  
# reverse the array
data_2 = data[::-1]
  
# write the reversed list to the output file
f2.writelines(data_2)
  
f2.close()
