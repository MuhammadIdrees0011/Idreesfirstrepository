# Printing B pattern in stars shape
# for row in range(0, 7):
#     for col in range(0, 6):
#         if ((col == 0 or col == 4) and (row!= 0)) \
#             or ((row == 1 or row == 4 or row ==  6) and (col >0 and col <5)):
#                 print("*",end ="")
#         else:
#             print(end=" ")
#     print()








for row in range(0, 6):
    for col in range(0, 4):
        if (row == 0 ) or (col == 1 and row != 0) \
            or (row == 5 and col ==  0):
            print("*", end = "")
            
        
        else:
            print(end=" ")
    print()






















# for rows in range(0,7):
#     for colums in range(0,6):
#         if ((colums == 0 or colums == 4) and (rows != 0)) \
#             or ((rows == 1 or rows == 4 or rows == 6) and (colums >0 and  colums < 5)):
#                 print("*", end = "")
#         else:
#             print(end=" ")
#     print()