import easygui as eg  #import the gui to run the quiz  


eg.msgbox("Welcome to my quiz on the story on Peter Pan!") #A welcome and introduction to your website

score = 0 #Setting the score to 0 to start with


# QUESTION 1 with images

answers = ["Brown","Black","Green","Red","Blue"] 


choice = eg.buttonbox("How many pigs was in the story?","Quiz!",answers,"peter.gif") #Add the gif image to your question

if choice == "Green":
    eg.msgbox("Excellent choice well done!","Quiz!")
    score = score + 1
else:
    eg.msgbox("No, It his clothes was Green","Quiz!")


# QUESTION 2 with images

answers = ["Cinderella","Rapunzel","TinkerBell"] 


choice = eg.buttonbox("Who is Peter Pan’s little friend?","Quiz!",answers,"tinker.gif") #Add the gif image to your question

if choice == "TinkerBell":
    eg.msgbox("Excellent choice well done!","Quiz!")
    score = score + 1
else:
    eg.msgbox("No, TinkerBell is Peter Pan's little friend!","Quiz!")

    

