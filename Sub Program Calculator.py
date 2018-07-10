#Define Calculation(Sub-Program) send 3 parameters

def Calculation(number_1,number_2,cal_type):
    #Check if cal_type is equal to plus
    if cal_type=="+":
        total=number_1+number_2
    #Check if cal_type is equal to minus
    elif cal_type=="-":
        total=number_1-number_2
    #Check if cal_type is equal to times
    elif cal_type=="*":
        total=number_1*number_2
    #Check if cal_type is equal to divide
    elif cal_type=="/":
        total=number_1/number_2

    #Rounds total to 2DP and places it back into total
    total=round(total,2)
    #Returns total to main program
    return total
#Askes what number 1 is and puts it in num_1 (Float accepts decimal)
num_1=float(input("What is number 1?"))
#Askes what number 2 is and puts it in num_2
num_2=float(input("What is number 2?"))
#Askes what calculation unit to use
cal_type=input("What is the calculation type- +,-,*,/")
#Runs sub-program and passes it the 3 parameters
total=Calculation(num_1,num_2,cal_type)
#prints total
print(total)
