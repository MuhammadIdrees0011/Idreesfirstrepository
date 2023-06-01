# printing stars in A shape:
#0,0, 0,1,0,2, 0,3,0,4
 
for row in range(0,7):
    for col in range(0,5):
        if (col == 0 or col == 4)  or ((row == 0 or row == 3)\
            and (col>0 and col <4)):
            print("*", end="")
        else:
            print(end=" ")
    print()



























# for row in range(0,6):
#     for col in range(0,5):
#         if ((col == 0 or col == 4) and (row!=0)) or ((row == 0 or row == 3) and (col>0 and col <4)):
#             print("*",end="")
#         else:
#             print(end=" ")
#     print()