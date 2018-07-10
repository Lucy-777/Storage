import sys

#alphabet
alphabet = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
# creates the function codeMessage and gets the parameters cypher_shift, file_data and alphabet
def codeMessage(cypher_shift, file_data, alphabet):
    #what decoded_message would look like at start
    decoded_message = ""
    #repeats the loop for every look in file
    for line in file_data:
        # length of line in the file
        length_of_code = len(line)
        # creates a for loop to start at position 0 and goes through each character
        for x in range(0, length_of_code):
            #ignores , . ! \n and " " or space
            if line[x] == "," or line[x] == "." or line[x] == "!" or line[x] == "\n" or line[x] == " ":
                #tells it to go straight into decode_letter and not do anything to it
                decode_letter = line[x]
            #if its not one of those character itll run in else
            else:
                #changes the character to upper case and finds where the character is in the alphabet list
                letter_position = alphabet.index(line[x].upper())
                #creates a temperory varible of cypher_shift called cypher_shift_temp so we dont change cypher_shift
                cypher_shift_temp = cypher_shift

                
                #out of bounds fix
                #finds the letter in the alphabet list and then adds the cypher shift to it
                #it takes away the answer from 25
                #if the answer is 0 or greater than 0 then we know the shift will drop of the end of the list 
                if (25-(letter_position+cypher_shift)) < 0:
                    #take away 25 from the new position of the end of the list
                    #this will tell us the position in the list of the shifted character(any position dropped of the list will be put at the start
                    cypher_shift_temp = (letter_position+cypher_shift) - 25
                    #sets letter_position to -1
                    letter_position = -1
              
                #will get the character at the new position from the alphabet list and place it in decode_letter
                decode_letter = alphabet[letter_position+cypher_shift_temp]
            #adds this letter onto the decoded message
            decoded_message = decoded_message + decode_letter
            
        #adds decoded_message to "/r" which basically makes a new line        
        decoded_message = decoded_message + "\r"
    # returns the final message
    return decoded_message






while True:
    while True:
        print("")
        print("")
        print("****************************************")
        print("*")
        print("* Welcome to my encryption program.")
        print("*")
        print("****************************************")
        print("")
        #asks for file name with extension
        file_name =input("file name? include extension ")
      

        try:
            #opens file_data, now its dynamic(your own file name)
            file_data = open(file_name,"r")

        except:
             print("File does not exist, please check file name and extension are correct ")
             break


        #asks for cypher shift
        try:
            cypher_shift =int(input("what cypher shift would you like -9 to 9 "))
        except:
            print("Not a number, try again")
            break

        
        if cypher_shift < -9 or cypher_shift > 9:
            print("Cypher shift out of bounds")
            break
        #asks if you want to encode or decode
        en_type = input("encode or decode? ")
        en_type = en_type.lower()
        if en_type == "encode" or en_type == "decode":
            print()
        else:
            print("Not entered correctly.")
            break






        #if you want to encode then it just times the cypher_shift by -1 so it inverts the direction of the shift    
        if en_type == "encode":
            cypher_shift = cypher_shift*-1




        #tells decoded_message to run codeMessage and to send cypher_shift file_data and alphabet as parameters 
        decoded_message = codeMessage((cypher_shift), file_data, alphabet)
        #prints decoded_message
        print(decoded_message)
        ##
        #closes file_data
        file_data.close()
        #cypher_data.close()
    end = input("Do you want to end program?")
    if end == "yes":
        sys.exit()
    


