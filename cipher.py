def encryptCode(code,cipher):
    final_code = ""
    code_length = len(code)
    for x in range(0,code_length):
        character = int(code[x])
        #change the code
        character = character + cipher
        #add the encrypted digit to the final code
        final_code = final_code + str(character)
    return final_code

error_flag = True

while error_flag:
    error_flag = False
    code = input("Add your numeric code ")


    if len(code) >5 and len(code) <9:
        print("Code correct length")
    else:
        print("Code incorrect length")
        error_flag = True
    if code.isdigit():
        print("Is number")
    else:
        print("Not number")
        error_flag = True
    cipher = input("Key which is between -9 & 9 ")

    if int(cipher) <10 and int(cipher) >-10:
        print("Cipher between 10 and -10")
    else:
        print("Cipher not between 10 and -10")
        error_flag = True
        
    final_code = encryptCode(code,int(cipher))
    print(final_code)    
