# 4. More Control Flow Tools
#
# x=0
# while x<10 :
#     print(x)
#     x += 1


    # 4.1. if Statements
#
# try:
#     x = int(input("please inter a number: "))
# except ValueError:
#     print("it's not number")
# if x<0 :
#     print("negative changed to zero")
#     x=0
#     print(0)
# elif x==0:
#     print("zero")
# elif x==1:
#     print("one")
# elif x>0:
#     print("more")


    # 4.2. for Statements
#
# words = ["cat","catfish","horse"]
# for word in words:
#     print(f"{word}, len={len(word)}")
#
# # #
#
# users = {"hamed":"active", "mamad":"inactive", "hasan":"active"}
# for user,status in users.copy().items():
#     if status=="inactive":
#         del users[user]
# print(users)
#
# # #
#
# users = {"hamed":"active", "mamad":"inactive", "hasan":"active"}
# active_users = {}
# for user,status in users.items():
#     if status=="active":
#         active_users[user] = status
# print(active_users)


    # 4.3. The range() Function
#
# for i in range(4):
#     print(i)
# # : 0
# # : 1
# # : 2
# # : 3
#
# # #
#
# print(list(range(3,10)))
# # : [3,4,5,6,7,8,9]
# print(list(range(3,10,2)))
# # : [3,5,7,9]
# print(list(range(-3,-10,-2)))
# # : [-3,-5,-7,-9]
#
# # #
#
# names = ["hamed","mamad","hasan"]
# for i in range(len(names)):
#     print(f"{i} : {names[i]}")
# # better to use enumerate()
#
# # #
#
# # some function work with iterative object
# sum(range(4)) # 1+2+3
# # : 6


    # 4.4. break and continue Statements
#
# # break & continue in the innermost circle
# # for & while
#
# for i in range(0,10):
#     if i==2:
#         break
#     print(i)
#
# # #
#
# for i in range(0,3):
#     if i==1:
#         continue
#     print(i)
# # continue = next circle


    # 4.5. else Clauses on Loops
#
# # 'break' (also reture) and 'else' are interdependent
# # if 'while/for x==T' never execute 'else' but if 'while/for x==F' just ones execute 'else'
# # 'else' with 'for/while' is simular to 'else' with 'try'
#
# n=0
# while n<3:
#     if int(n%2==2):
#         print('break')
#         break
#     n+=1
# else:
#     print("there's no two")
#
# # #
# 
# for i in range(3):
#     if int(i%2==3):
#         print('break')
#         break
#     i+=1
# else:
#     print("there's no two")


    # 4.6. pass Statements