# --------------------------------------------------


    # 01_qtimer_singleshot

# from PySide6.QtWidgets import QApplication
# from PySide6.QtCore import QTimer
# import sys

# def main():
#     print("wait for closing the app")
    
#     # starting Object
#     app = QApplication([])

#     # simple delay (1000ms=1s) - static func (no need ReferenceObject)
#     QTimer.singleShot(5000, app.quit)

#     # app.exec = execute the app (like a function) 
#     # sys.exit = handling errors ( return to OS)
#     sys.exit(app.exec())


# if __name__ == "__main__":
#     main()


# --------------------------------------------------


    # 02_pyside_version

# from PySide6.QtCore import qVersion
# from packaging import version
# import sys
# pyside_minimum_version = "6.4.2"

# def main():
    
#     # str to version-object (comparing versions)
#     current_version = version.parse(str(qVersion()))
    
#     if current_version >= version.parse(str(pyside_minimum_version)):
#         print(f"GOOD -- {current_version=!s},{pyside_minimum_version=!s}")
#     else:
#         print(f"upgrade your pyside -- {current_version=!s},{pyside_minimum_version=!s}")
#         sys.exit(2)


# if __name__ == "__main__":
#     main()