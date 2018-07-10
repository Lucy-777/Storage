print(
"""
|=======|
|Netflix|
|=======|
""")


askacc = input("Do you have a account? ")
askacc.lower

if askacc == "yes" or "y":
    print("Yes")
elif askacc == "no" or "n":
    print("No")
else:
    print("You didnt enter a correct answer, Please try again")
    
print(askacc)
