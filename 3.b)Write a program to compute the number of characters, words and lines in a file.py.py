'''3.b) Write a program to compute the number of characters, words and lines in a file.'''


file = open("Sample.txt", "r")                          #Open source file in r (read) mode. 
number_of_lines = 0                                     #variable to store total line count.
number_of_words = 0                                     #variable to store total word count.
number_of_characters = 0                                #variable to store total character count.
for line in file:
    
 line = line.strip("\n")
 words = line.split()                                   #splitting the line to make a list ofall the words present in that line and storing.
 number_of_lines += 1                                   #incrementing value of num_lines with each iteration of loop
number_of_words += len(words)                           #incrementing value of num_words by the number of items in the list wordlist
number_of_characters += len(line)
file.close()
  
print("lines:", number_of_lines, "words:", number_of_words, "characters:", number_of_characters)    # printing total word count,line count,character count.
