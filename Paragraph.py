#Roosevelt Bannerman
#Paragraph Program

global NUM_COLUMNS
NUM_COLUMNS = 80

global inputFile
inputFile = open("input.txt","r")
global outputFile
outputFile = open("output.txt","w")


def nextWord():
    temp = ""
    word = ""
    endFile = False
    newPara = False
    
    while(temp != " "):
        temp = inputFile.read(1)
        if not temp:
            endFile = True
            return word,newPara,endFile
        elif(temp == "\n"):
            newPara = True
            return word,newPara,endFile
        elif(temp == " "):
            return word,newPara,endFile
        else:
            word += temp

    return word,newPara,endFile
    
def runProgram():
    endFile = False
    word = ""
    line = ""
    carry = ""
    while(not endFile):
        line = carry
        carry = ""
        word,newPara,endFile = nextWord()
        if(len(line) + len(word) < NUM_COLUMNS and newPara == False):
            line += (word + " ")
            carry = line
        elif(len(line) + len(word) < NUM_COLUMNS and newPara == True):
            line = line[:-1]
            outputFile.write(line + "\n\n")
            carry = ""
        elif(len(line) + len(word) >= NUM_COLUMNS and newPara == False):
            line = line[:-1]
            difference = NUM_COLUMNS - len(line)
            counter = 0
            while(difference > 0):
                if(line[counter] == " "):
                    temp1 = line[:counter]
                    temp2 = line[counter:]
                    line = temp1 + " " + temp2
                    difference -= 1
                    counter +=1
                elif(counter == len(line)-1):
                    counter = 0
                counter += 1
            outputFile.write(line + "\n")
            carry = word + " "
        elif(len(line) + len(word) >= NUM_COLUMNS and newPara == True):
            line = line[:-1]
            difference = NUM_COLUMNS - len(line)
            while(difference > 0):
                if(line[counter] == " "):
                    temp1 = line[:counter]
                    temp2 = line[counter:]
                    line = temp1 + " " + temp2
                    difference -= 1
                    counter +=1
                elif(counter == len(line)-1):
                    counter = 0
                counter += 1
            outputFile.write(line + "\n")
            outputFile.write(word+"\n\n")
            carry = ""

            print("\n\tPress enter to save the results.")
            input()
            
runProgram()
inputFile.close()
outputFile.close()
