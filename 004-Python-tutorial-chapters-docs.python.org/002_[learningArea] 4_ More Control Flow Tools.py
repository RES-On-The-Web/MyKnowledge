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
#
# # means nothing
#
# class myEmptyClass:
#     pass
# 
# #
# 
# def initlog(*args):
#     pass
# 
# #
# 
# def initlog(*args):
#     ...


    # 4.7. match Statements
#
# # _ = 'else'
#
# status=1
# match status:
#     case 2:
#         print(1)
#     case 2:
#         print(2)
#     case 4 | 3:
#         print("4 | 3")
#     case _:
#         print("=elsey")


    # 4.8. Defining Functions
# a=4
# def tabee():
#     "this is a docstring (document of my code)"
#     a=3
#     print(a)


    # 4.9. More on Defining Functions
    # 4.9.1. Default Argument Values
#
# def plusTabee(a,b=1,c=1):
#     print(a+b+c)
# plusTabee(a=1,b=2)
# 
# #
# 
# i=2
# def f(vari=i):
#     print(vari)
# i=3
# f()
# # : 2
#
# #
#
# def g(a, L=[]):
#     L.append(a)
#     print(L)
# g(1)
# g(2)
# g(3)
# # : [1]
# # : [1,2]
# # : [1,2,3]
#
# #
#
# def gg(a, L=None):
#     if L==None:
#         L=[]
#     L.append(a)
#     print(L)
# gg(1)
# gg(2)
# gg(3)
# # : [1]
# # : [2]
# # : [3]


    # 4.9.2. Keyword Arguments
#
# # with the same arrangment in arguments & keyword. 
# # * = args without key , ** = args with key
# 
# def somthing(a,*arguments, **keyword):
#     print(a)
#     print("-"*40)
#     for arg in arguments:
#         print(arg)
#     print("-"*20)
#     for kw in keyword:
#         print(keyword[kw])
#     print("-"*10)
#     print(arguments)
#     print(keyword)
# somthing("git","-c","asdlfsd","asdfasdf",aa=30,bb=40)


    # 4.9.3. Special parameters
#
# def p_pk_k(Jposition,/,pANDk,*,Jkeyword):
#     print(Jposition,pANDk,Jkeyword)
# p_pk_k("p",pANDk="pk",Jkeyword="dsaf")


    # 4.9.3.1. Positional-or-Keyword Arguments
    # 4.9.3.2. Positional-Only Parameter
    # 4.9.3.3. Keyword-Only Arguments
    # 4.9.3.4. Function Examples
#
# def rand1(*,arg):
#     print(arg)
# rand1(arg=2394)
#
# #
#
# def rand2(arg,/):
#     print(arg)
# rand2(8345)
#
# #
#
# def rand3(arg):
#     print(arg)
# rand3(arg=435345)
# rand3(435345)


    # 4.9.3.5. Recap
    # 4.9.4. Arbitrary Argument Lists
    # 4.9.5. Unpacking Argument Lists
#
# args = [2,5]
# l=[]
# for num in range(*args):
#     l.append(num)
# print(l)
# print(*args)
# 
# # # 
# 
# def dictstar(var1,var2="dsafsdf",var3="afddafs"):
#     print(var1,var2,var3)
# dictL={"var1":"adsfdsf","var2":"asdas","var3":"asdfsdf"}
# dictstar(**dictL)


    # 4.9.6. Lambda Expressions
#
# # small function == lambda x,n: x+n
# # small class ==
# def smallClass(n):
#     return lambda x:x+n 
# ob = smallClass(100)
# print(ob)
# print(ob(1))


    # 4.9.7. Documentation Strings
#
# # start with captal and end with dot
# # secend line should be empty (=summary)
# # other lines ... (there's no pattern)
#
# def my_function():
#     """Do nothing, but document it.

#     No, really, it doesn't do anything:

#         >>> my_function()
#         >>>
#     """


    # 4.9.8. Function Annotations
#
# # (NO ERROR)
#
# def annotations(name : str = "hamed",phoneNumber : int = "09000000") -> list:
#     return [name,phoneNumber]
# print(annotations())


    # 4.10. Intermezzo: Coding Style