sp_l =[
    [1, 2, 3],
    ["a", "b", "c"],
    ["+", "-", "*"]
]
#which section then which item of that section
#[0][2]
sp_l.append([9, 8, 7])

list_length = len(sp_l)

for x in range(0,list_length):
    print(sp_l[x][0])
    #print(sp_l[1][x])
    #print(sp_l[2][x])
#print(sp_l[x][3])

