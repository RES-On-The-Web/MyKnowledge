# --------------------------------------------------


    # 01_simple_example

# from PySide6.QtWidgets import QApplication,QWidget
# import sys

# def main():

#     app = QApplication()

#     window = QWidget()
#     window.resize(1920,1080)
#     window.setWindowTitle("simple window")
    
#     window.show()
#     sys.exit(app.exec())


# if __name__ == "__main__":
#     main()


# --------------------------------------------------


    # 02_window_icon

# from PySide6.QtWidgets import QApplication, QWidget
# from PySide6.QtGui import QIcon
# import sys
# import os
# from pathlib import Path

# class Window(QWidget):
#     def __init__(self):
#         super().__init__()

#         self.resize(1920,1080)
#         self.setWindowTitle("simpleWindow")

#         path = Path(__file__).resolve().parent
#         self.setWindowIcon(QIcon(os.path.join(path, "./000_[miscellaneousArea]/icon.jpeg")))

#         self.show()

# def main():
#     app = QApplication(sys.argv)
#     window = Window()

#     sys.exit(app.exec())

# if __name__ == "__main__":
#     main()


# --------------------------------------------------


    # 03_tooltip

# from PySide6.QtWidgets import QApplication, QWidget, QToolTip, QPushButton, QHBoxLayout
# from PySide6.QtGui import QIcon, QFont
# from pathlib import Path
# import sys
# import os

# class Window(QWidget):
#     def __init__(self):
#         super().__init__()

#         self.resize(1920,1080)
#         self.setWindowTitle("simple window")



#         QToolTip.setFont(QFont("SansSerif", 10))
#         self.setToolTip('this is a <b>QWidget</b> widget')

#         button = QPushButton("click on this", self)
#         button.setFixedWidth(150)
#         button.resize(button.sizeHint())
#         button.setToolTip("this is a <b>QPushButton</b> widget")

#         layout = QHBoxLayout(self)
#         layout.addWidget(button)


# def main():
#     app = QApplication(sys.argv)
#     window = Window()

#     window.show()
#     sys.exit(app.exec())

# if __name__ == "__main__":
#     main()


# --------------------------------------------------


    # 04_closing_a_window

# from PySide6.QtWidgets import QApplication, QWidget, QPushButton, QHBoxLayout
# import sys

# class Window(QWidget):
#     def __init__(self):
#         super().__init__()

#         self.resize(1920,1080)
#         self.setWindowTitle("simple window")


#         button = QPushButton("quit", self)
#         button.setFixedWidth(150)
#         button.clicked.connect(QApplication.quit)
        
#         layout = QHBoxLayout(self)
#         layout.addWidget(button)


# def main():
#     app = QApplication(sys.argv)
#     window = Window()

#     window.show()
#     sys.exit(app.exec())


# if __name__ == "__main__":
#     main()


# --------------------------------------------------


    # 05_window_center

# from PySide6.QtWidgets import QApplication, QWidget
# from PySide6.QtGui import QScreen
# import sys

# class Window(QWidget):
#     def __init__(self):
#         super().__init__()

#         self.resize(1920,1040)
#         self.setWindowTitle("simple window")
#         self.window_center()


#     def window_center(self):
#         screen = QApplication.primaryScreen()
#         center_point = screen.availableGeometry().center()

#         window_screen = self.frameGeometry()
#         window_screen.moveCenter(center_point)
#         self.move(window_screen.topLeft())
        
        

# def main():
#     app = QApplication(sys.argv)
#     window = Window()

#     window.show()
#     sys.exit(app.exec())


# if __name__ == "__main__":
#     main()


# --------------------------------------------------


    # 06_window_button

# from PySide6.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QVBoxLayout
# from PySide6.QtCore import Qt
# import sys
# import random

# class Window(QWidget):
#     def __init__(self):
#         super().__init__()

#         self.resize(1920,1080)
#         self.setWindowTitle("simple window")


#         button = QPushButton("click on this", self)
#         button.setFixedWidth(150)
#         button.clicked.connect(self.changeTheText)

#         self.label = QLabel("i want to say somthing ... ")
#         self.label.setAlignment(Qt.AlignBottom | Qt.AlignHCenter)

#         layer = QVBoxLayout(self)
#         layer.addWidget(self.label)
#         layer.addWidget(button, alignment=Qt.AlignTop | Qt.AlignHCenter)
        

#     def changeTheText(self):
#         textList= [
#             ";)",
#             "FU",
#             "ILU",
#             "NOUOUOUO"
#         ]

#         self.label.setText(random.choice(textList))



# def main():
#     app = QApplication()
#     window = Window()

#     window.show()
#     sys.exit(app.exec())

# if __name__ == "__main__":
#     main()


# --------------------------------------------------


    # 07_window_hide_min_max

# from PySide6.QtWidgets import QApplication, QWidget
# from PySide6.QtCore import Qt
# import sys

# class Window(QWidget):
#     def __init__(self):
#         super().__init__()

#         self.resize(300,200)
#         self.setWindowTitle("simple window")
        
#         self.setWindowFlag(Qt.CustomizeWindowHint, True)
#         self.setWindowFlag(Qt.WindowMinMaxButtonsHint, False)


# def main():
#     app = QApplication()
#     window = Window()

#     window.show()
#     sys.exit(app.exec())

# if __name__ == "__main__":
#     main()