filedata = open("code.txt", "w+")
for x in range(0,11):
    
    filedata.write(str(x)+"\n")
filedata.close()

filedata = open("code.txt", "a+")
filedata.write("Finish")
filedata.close()
