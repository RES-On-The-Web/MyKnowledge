    # 7. Input and Output
    # 7.1. Fancier Output Formatting
# 
# c=4353
# print(f"{c} mobile")
# 
# #
# 
# a = 234234
# b = 2342/234234
# print("{:.2%}".format(b))
#
# #
#
# str() = human writing
# repr() = compiler writing


    # 7.1.1. Formatted String Literals¶
#
# import math
# print(f"{math.pi:.3f}")
# 
# #
# 
# table={"hamed":23423,"mamad":23423,"hasan":324532}
# for name,phone in table.items():
#     print(f"{name:10} ==> {phone:10}")
# 
# #
# 
# name = "hamed"
# print(f" -> {name!s}") #= str()
# print(f" -> {name!r}") #= repr()
# 
# #
# 
# name = "hamed"
# print(f"{name=}")


    # 7.1.2. The String format() Method
#
# SKIP


    # 7.1.3. Manual String Formatting
# 
# for x in range(10):
#     print(str(x).rjust(3),str(x).rjust(3),str(x).rjust(3))


    # 7.1.4. Old string formatting
    # 7.2. Reading and Writing Files
#
# f = open("workflow","w","encoding="utf-8) #= open("workflow") default mode=r
# # name - mode (r,w,a, b) - encoding type
# 
# #
#
# with open("workflow") as f:
#     content = f.read()
# print(f.closed)


    # 7.2.1. Methods of File Objects
#
# with open("vs.txt") as f:
#     content = f.read()
# print(content)
# 
# # 
# 
# with open("vs.txt") as fl :
#     contentl = fl.readline()
# print(contentl)
# 
# #
# 
# with open("vs.txt") as fls :
#     for l in fls :
#         print(l, end="")
# 
# #
# 
# with open("vs.txt") as fls2 :
#     contentls2 = list(fls2)
# print(contentls2)
# 
# #
# 
# with open("vs.txt") as fr :
#     fr.write("write this mf")
