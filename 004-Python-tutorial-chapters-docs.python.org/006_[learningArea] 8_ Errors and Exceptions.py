    # 8. Errors and Exceptions
    # 8.1. Syntax Errors
    # 8.2. Exceptions
#
# 10/0 -> ZeroDivisionError : division by zero
# 4+ spam*3 -> NameError : name 'spam' not defined
# '2' + 2 -> TypeError : can only concatenate str (not "int") to str


    # 8.3. Handling Exceptions
#
# while True:
#     try:
#         m = int(input("enter you're number : "))
#     except ValueError:
#         print("enter numbers not letters, Sir")
#     except KeyboardInterrupt:
#         print("you can't stop the app")
# #
# while True:
#     try:
#         m = int(input("enter you're number : "))
#     except ValueError, KeyboardInterrupt:
#         print("it's wrong !!!!")
# #
#
# while True:
#     try:
#         m = int(input("enter you're number : "))
#         break
#     except Exception as inst:
#         print(inst)
#         print(type(inst))
#
# #
#
# # else = code without exceptions (safe zone)
#
# while True:
#     try:
#         m = int(input("enter you're number : "))
#         break
#     except Exception as inst:
#         print(inst)
#         print(type(inst))
#     else:
#         print("if previous code runs correctly , i'll run too")


    # 8.4. Raising Exceptions
#
# raise NameError ("this is for developers")
#
# #
#
# try:
#     raise ValueError("hello")
# except:
#     print("somthing")
#     raise


    # 8.5. Exception Chaining
#
# while True:
#     try:
#         m = int(input("enter you're number : "))
#         break
#     except ValueError:
#         raise NameError("sec error")


    # 8.6. User-defined Exceptions
    # 8.7. Defining Clean-up Actions
#
# # resource release
# always 'finally' runs


    # 8.8. Predefined Clean-up Actions
#
# # with = auto resource releaser


    # 8.9. Raising and Handling Multiple Unrelated Exceptions
#
# try:
#     raise ExceptionGroup("dsfds",[OSError("e1"), SystemError("e2")])
# except* OSError as e:
#     print("done")
# except* SystemError as e:
#     print("done2")


    # 8.10. Enriching Exceptions with Notes
#
# while True:
#     try:
#         m = int(input("enter you're number : "))
#         break
#     except Exception as e:
#         e.add_note("add some information (good for loops)")
#         raise
