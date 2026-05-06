    # 6. Modules
#
# def tabee(x:int):
#     print(x)
# t = tabee
# t(12312)


    # 6.1. More on Modules
#
# # developing module
#
# import main
# import importlib
# importlib.reload(main)
# main.printx(43252345)
#
# # plugings
#
# import importlib
# main = importlib.import_module("main")
# main.printx(23423)


    # 6.1.1. Executing modules as scripts¶
#
# def printx(x):
#     print(x)
# if __name__ == "__main__":
#     import sys
#     printx(int(sys.argv[1]))


    # 6.1.2. The Module Search Path
    # 6.1.3. “Compiled” Python files
    # 6.2. Standard Modules
# import sys
# print(sys.path)
# # sys.path.append('/somthing/somthing/somthing')


    # 6.3. The dir() Function
#
# # import fibo
# # print(dir(fibo))
# # : ['__name__', 'fib', 'fib2']
# import sys
# print(dir(sys))
# # just it shows functions
# 
# #
#
# dir()
# # it shows names/var/module/func/... in current file
#
# #
# 
# dir(builtins)
# # it shows standard modules in python


    # 6.4. Packages
#
# sound/                          Top-level package
#       __init__.py               Initialize the sound package
#       formats/                  Subpackage for file format conversions
#               __init__.py
#               wavread.py
#               wavwrite.py
#               aiffread.py
#               aiffwrite.py
#               auread.py
#               auwrite.py
#               ...
#       effects/                  Subpackage for sound effects
#               __init__.py
#               echo.py
#               surround.py
#               reverse.py
#               ...
#       filters/                  Subpackage for filters
#               __init__.py
#               equalizer.py
#               vocoder.py
#               karaoke.py
#                ...
# # from pkg.form import printa
# # printa.printaa(23940)
#
# #
#
# # you can't import method of a class in import-line (except static methods) or var = class.func


    # 6.4.1. Importing * From a Package
#
# # for faster experience, use 
# # >>> __all__ = ["module1","module2","module3"]
# # in __init__ file to 
# # >>> from pkg.subpkg import *
# # code work faster


    # 6.4.2. Intra-package References
#
# # absolute imports
# # from pkg.subpkg.module import class & __init__.py files
# # relative imports
# # need __init__.py files & python -m pkg.subpkg.executablefile & from ..anothersubpkg import file


    # 6.4.3. Packages in Multiple Directories
# __path__ ?!?