
# practiceString = "Dynamite"
#
# for i in range(4):
#     i = i * 30
#     print(i)

'''Stackoverflow Example'''

# n = 4
# print("Pattern 1")
#
# for a1 in range (0 , n):
#     for a2 in range (a1):
#         print("*", end="")
#     print()
#
# for a1 in range (n,0,-1):
#     for a2 in range (a1):
#         print("*", end="")
#     print()

# --------------------------------
# Row1: 4 spaces, 1 star, 4 spaces
# Row2: 3 spaces, 3 stars, 3 spaces
# Row3: 2 spaces, 5 stars, 2 spaces
# Row4: 1 space, 7 stars, 1 space
# Row5: 0 spaces, 9 stars, 0 spaces
# Row6: 1 space, 7 stars, 1 space
# Row7: 2 spaces, 5 stars, 2 spaces
# Row8: 3 spaces, 3 stars, 3 spaces
# Row9: 4 spaces, 1 star, 4 spaces
# ---------------------------------
# n = 9
# print("Pattern 2")
#
# for a1 in range(1, (n+1)//2 + 1): #from row 1 to 5
#     for a2 in range((n+1)//2 - a1):
#         print(" ", end = "")
#     for a3 in range((a1*2)-1):
#         print("*", end = "")
#     print()
#
# for a1 in range((n+1)//2 + 1, n + 1): #from row 6 to 9
#     for a2 in range(a1 - (n+1)//2):
#         print(" ", end = "")
#     for a3 in range((n+1 - a1)*2 - 1):
#         print("*", end = "")
#     print()

'''Deconstructing the code'''

for a in range(1,(9+1)//2+1):
    for a2 in range ((9+1)//2-a):
        print("",end="")
print("Hello World")




