'''3. a) Write a program to print each line of a file in reverse order. '''



def file_Creation():                                        #Using the memory space allocated to the variable “ofile”,we are opening/creating the file
     ofile=open("Sample.txt","w+")                          #“Story.txt” in write+read mode (w+). This variable is now used in the next steps to access
     choice=True                                            #The boolean True is assigned to a variable “choice”.
     while True:                                            
            line=input("\n Enter a sentence")               #Then using the while loop, we write the desired lines into the file using the variable “line”.
            ofile.write(line)                               #The content in the variable “line” is written in the file using the command ofile .write(line).
            choice=input("Enter more?-Y/N")
            if choice=='N':break
     ofile.close()                                          #Then the file is closed using the command ofile.close().
     def Reverse_Content():
      ofile=open("Sample.txt","r")
      k=ofile.readlines()                                   #Then the variable “k” stores the list created using the readlines() command.
      t=reversed(k)                                         #The list stored in the variable “k” is then reversed and stored in the variable “t”.
      for i in t:
           print(i.rstrip())                                #Using a for loop, we can print each line using the ‘rstrip’ method from t.
                                                            #Hence the content is printed in the reverse order.
