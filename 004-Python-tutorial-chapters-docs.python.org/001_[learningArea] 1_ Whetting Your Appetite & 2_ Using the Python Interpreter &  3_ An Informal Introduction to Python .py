# 1.Whetting Your Appetite 








# 2.Using the Python Interpreter


    # 2.1.Invoking the Interpreter
    ##Terminal: python -c "print('hello_world')"
    ##Terminal: python -m module(scripts.py)
    ##Terminal: python -i script.py
    

    # 2.1.1.Argument Passing
# import sys
# print(len(sys.argv))
# print(sys.argv)


    # 2.1.2.Interactive Mode


    # 2.2.The Interpreter and Its Environment


    # 2.2.1.Source Code Encoding
# # -*- coding: UTF-8 -*-
# or
# (a shebang) #!/user/bin/env python3
# # -*- coding: cp1252 -*-








# 3.An Informal Introduction to Python
# spam = 1 # this is a command
# text = "# but this is not command because it's inside quotes"


    # 3.1. Using Python as a Calculator


    # 3.1.1.Numbers
# print(2+1,1-1,2*10,2**10,2/2,2//2,2%2)
# print(2j+1)
#     #>>> 2+10
#     #12
#     #>>>_+1
#     #13


    #  3.1.2.Text
    # # # text is unchangable (word[0]=b , ERROR)
    # # 'string' == "string"
    # # "it's" == 'it\'s'
    #
    # # >>>print('it\'s \na monkey')
    # # it's 
    # # a monkey
    # # >>>print(r"C:\this\name")
    # # C:\this\name
    #
    # # print("""\
    # # ksan;lfskdnfsad
    # # aksdn;lfksnd;lfsad\
    # # """)
    # # # \ = removing new line
    #
    # # >>>"un"+"locked"
    # unlocked
    # # >>>"un"*3
    # ununun
    # # >>>"un" "locked"
    # unlocked
    # # >>>text = ("un"
    # # >>>         "locked")
    # # >>>text
    # unlocked
    # # >>>text "un"
    # ERROR
#  +---+---+---+---+---+---+
#  | P | y | t | h | o | n |
#  +---+---+---+---+---+---+
#  0   1   2   3   4   5   6
# -6  -5  -4  -3  -2  -1
    # # >>>word = python
    # # >>>word[0]
    # w
    # # >>>word[-1:] (=word[-1:2381])
    # # >>len(word)
    # 6


    # 3.1.3.Lists
    # # # text is changable
    # # # list[0] , list[0:] , list.append[10] are available
    #
    # # >>> list = ["one", "two"]
    # # >>> list_link = list
    # # >>> list_link[-1] = "ten"
    # # # id(list) === id(list_link)
    # # # list === list_link
    #
    # # >>> list_copy = list[:]
    # # >>> list_copy[-1] = "ten"
    # # >>> list_copy != list
    
    
    # 3.2. First Steps Towards Programming
    # # # 0 and [] === False
    # # # a, b = b, a+b
# print(234,12342)
#     # # # , = one space

