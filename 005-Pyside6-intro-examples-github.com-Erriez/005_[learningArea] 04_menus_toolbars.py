# --------------------------------------------------


    #  01_statusbar

# from PySide6.QtWidgets import QApplication, QMainWindow
# import sys

# class Window(QMainWindow):
#     def __init__(self):
#         super().__init__()

#         self.resize(250, 150)
#         self.setWindowTitle("simple window")

#         self.statusBar().showMessage("hello this is me")


# def main():
#     app = QApplication(sys.argv)
#     window = Window()

#     window.show()
#     sys.exit(app.exec())

# if __name__ == "__main__":
#     main()


# --------------------------------------------------


    # 02_menubar

# from PySide6.QtWidgets import QApplication, QMainWindow
# from PySide6.QtGui import QAction, QIcon
# import sys
# from pathlib import Path
# import os

# class Window(QMainWindow):
#     def __init__(self):
#         super().__init__()
#         self.__self_recognizer()

#         self.resize(300,200)
#         self.setWindowTitle("simple Window")


#     def self_recognizer(self):
#         self.menu_status()
#     __self_recognizer = self_recognizer

#     def menu_status(self):

#         menuBar = self.menuBar()
#         menu_file = menuBar.addMenu("&File")

#         path = Path(__file__).resolve().parent
#         exit_action = QAction(QIcon(os.path.join(path, "./000_[miscellaneousArea]/icon.jpeg")),"&Exit",self)

#         exit_action.triggered.connect(self.close)
#         self.statusBar()

#         exit_action.setStatusTip("exit action")
#         exit_action.setShortcut("Ctrl+O")
        
#         menu_file.addAction(exit_action)


# def main():
#     app = QApplication()
#     window = Window()

#     window.show()
#     sys.exit(app.exec())

# if __name__ == "__main__":
#     main()


# --------------------------------------------------


    # 03_toolbar

# from PySide6.QtWidgets import QApplication, QMainWindow
# from PySide6.QtGui import QAction, QIcon
# import os
# from pathlib import Path
# import sys

# class Window(QMainWindow):
#     def __init__(self):
#         super().__init__()
#         self.__self_recognizer()

#         self.resize(300, 200)
#         self.setWindowTitle("simple window")


#     def self_recognizer(self):
#         self.toolBar()
#     __self_recognizer = self_recognizer

#     def toolBar(self):

#         toolBar = self.addToolBar("Exit")

#         path = Path(__file__).resolve().parent
#         exit_action = QAction(QIcon(os.path.join(path, "./000_[miscellaneousArea]/icon.jpeg")), "ExitToolTip", self)

#         exit_action.setShortcut("Ctrl+I")
#         exit_action.setStatusTip("exit action on toolbar")

#         exit_action.triggered.connect(self.close)
#         self.statusBar()

#         toolBar.addAction(exit_action)



# def main():
#     app = QApplication(sys.argv)
#     window = Window()

#     window.show()
#     sys.exit(app.exec())

# if __name__ == "__main__":
#     main()


# --------------------------------------------------


    # 04_menubar_toolbar_statusbar

# from PySide6.QtWidgets import QApplication, QMainWindow, QTextEdit
# from PySide6.QtGui import QAction, QIcon
# import os
# import sys
# from pathlib import Path

# class Window(QMainWindow):
#     def __init__(self):
#         super().__init__()
#         self.__self_recognizer()

#         self.resize(300, 200)
#         self.setWindowTitle("simple window")

#     def self_recognizer(self):
#         self.menu_bar()
#         self.tool_bar()
#         self.body_widgets()
#     __self_recognizer = self_recognizer

#     def menu_bar(self):

#         menuBar = self.menuBar()
#         menu_file = menuBar.addMenu("&File")

#         path = Path(__file__).resolve().parent
#         exit_action = QAction(QIcon(os.path.join(path, "./000_[miscellaneousArea]/icon.jpeg")), "&Exit", self)

#         exit_action.setStatusTip("exit action on menu")
#         exit_action.setShortcut("Ctrl+O")

#         exit_action.triggered.connect(self.close)
#         self.statusBar()

#         menu_file.addAction(exit_action)

#     def tool_bar(self):

#         toolBar = self.addToolBar("Exit")

#         path = Path(__file__).resolve().parent
#         exit_action = QAction(QIcon(os.path.join(path, "./000_[miscellaneousArea]/icon.jpeg")), "&Exit", self)

#         exit_action.setStatusTip("exit action on menu")
#         exit_action.setShortcut("Ctrl+I")

#         exit_action.triggered.connect(self.close)
#         self.statusBar()

#         toolBar.addAction(exit_action)

#     def body_widgets(self):

#         text_edit = QTextEdit("this is a example")
#         self.setCentralWidget(text_edit)

# def main():
#     app = QApplication(sys.argv)
#     window = Window()

#     window.show()
#     sys.exit(app.exec())

# if __name__ == "__main__":
#     main()