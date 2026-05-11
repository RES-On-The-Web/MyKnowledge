# --------------------------------------------------


    # 01_input_dialog

# from PySide6.QtWidgets import QApplication, QMainWindow, QWidget, QInputDialog, QPushButton, QLineEdit, QHBoxLayout
# import sys

# class Widget(QWidget):
#     def __init__(self, parent):
#         super().__init__()
#         self.__self_recognizer()


#     def self_recognizer(self):
#         self.some_widgets()
#         self.main_layout()
#     __self_recognizer = self_recognizer

#     def some_widgets(self):
#         self.button = QPushButton("press this")
#         self.button.clicked.connect(self.dialog_box)

#         self.line_edit = QLineEdit()

#     def main_layout(self):
#         layoutH = QHBoxLayout(self)
#         layoutH.addWidget(self.button)
#         layoutH.addWidget(self.line_edit)

#     def dialog_box(self):
        
#         text, ok = QInputDialog.getText(self, "I&O dialog", "enter your name")

#         if ok:
#             self.line_edit.setText(text)


# class Window(QMainWindow):
#     def __init__(self):
#         super().__init__()

#         self.resize(300, 200)
#         self.setWindowTitle("simple window")

#         widget_class = Widget(parent = self)
#         self.setCentralWidget(widget_class)


# def main():
#     app = QApplication(sys.argv)
#     window = Window()

#     window.show()
#     sys.exit(app.exec())

# if __name__ == "__main__":
#     main()


# --------------------------------------------------


    # 02_color_dialog

# from PySide6.QtWidgets import QApplication, QWidget, QFrame, QColorDialog, QPushButton, QHBoxLayout
# import sys

# class Window(QWidget):
#     def __init__(self):
#         super().__init__()
#         self.__self_recognizer()

#         self.resize(300, 200)
#         self.setWindowTitle("simple window")


#     def self_recognizer(self):
#         self.more_widget()
#         self.main_layout()
#     __self_recognizer = self_recognizer


#     def more_widget(self):
#         default_color = "black"
#         self.button = QPushButton("press me")
#         self.button.clicked.connect(self.button_pressed)
#         self.frame = QFrame()
#         self.frame.setStyleSheet("QWidget { background-color : %s}" % default_color)
#         self.frame.setGeometry(50, 50, 100, 100)

#     def main_layout(self):
#         layoutH = QHBoxLayout(self)
#         layoutH.addWidget(self.button)
#         layoutH.addWidget(self.frame)

#     def button_pressed(self):
#         color = QColorDialog.getColor()

#         if color.isValid:
#             self.frame.setStyleSheet("QWidget { background-color : %s}" % color.name())


# def main():
#     app = QApplication(sys.argv)
#     window = Window()

#     window.show()
#     sys.exit(app.exec())

# if __name__ == "__main__":
#     main()


# --------------------------------------------------


    # 03_font_dialog

# from PySide6.QtWidgets import QApplication, QLabel, QFontDialog,  QPushButton, QWidget
# from PySide6.QtGui import QFont
# import sys

# class Window(QWidget):
#     def __init__(self):
#         super().__init__()

#         self.resize(300, 200)
#         self.setWindowTitle("simple window")

#         self.label = QLabel("this is a exmaple",self)
#         self.label.move(100, 100)
#         button = QPushButton("press this",self)
#         button.clicked.connect(self.font_window)

#     def font_window(self):
#         font, ok = QFontDialog.getFont()
#         if ok:
#             self.label.setFont(str(font))


# def main():
#     app = QApplication(sys.argv)
#     window = Window()

#     window.show()
#     sys.exit(app.exec())

# if __name__ == "__main__":
#     main()


# --------------------------------------------------


    # 04_file_dialog

# from PySide6.QtWidgets import QApplication, QFileDialog, QMainWindow, QLabel
# from PySide6.QtGui import QAction, QIcon
# import sys
# import os
# from pathlib import Path

# class Window(QMainWindow):
#     def __init__(self):
#         super().__init__()

#         self.resize(300, 200)
#         self.setWindowTitle("simple window")

#         path = Path(__file__).resolve().parent

#         open_action = QAction(QIcon(os.path.join(path, "./000_[miscellaneousArea]/icon.jpeg")),"&Open",self)
#         open_action.setStatusTip("open a file")
#         open_action.setShortcut("Ctrl+O")
#         open_action.triggered.connect(self.file_opener)

#         exit_action = QAction(QIcon(os.path.join(path, "./000_[miscellaneousArea]/icon.jpeg")), "&Exit", self)
#         exit_action.setStatusTip("close the program")
#         exit_action.setShortcut("Ctrl+L")
#         exit_action.triggered.connect(self.close)

#         menu = self.menuBar()
#         menu_file = menu.addMenu("&File")
#         menu_file.addAction(open_action)
#         menu_file.addSeparator()
#         menu_file.addAction(exit_action)

#         self.label = QLabel("a place")
#         self.setCentralWidget(self.label)


#     def file_opener(self):
#         path, _ = QFileDialog.getOpenFileName(self, "open file", "C:/")

#         if not path:
#             self.statusBar().showMessage("bro, don't cancel it")
#         elif not os.path.exists(path):
#             self.statusBar().showMessage("i cant file this path. try again")
#         else:
#             try:
#                 with open(path) as f:
#                     data = f.read()
#                     self.statusBar().showMessage("i found that !")
#                     self.label.setText(data)
#             except OSError as err:
#                 self.statusBar().showMessage(f"there's an error : {err}")


# def main():
#     app = QApplication(sys.argv)
#     window = Window()

#     window.show()
#     sys.exit(app.exec())

# if __name__ == "__main__":
#     main()


# --------------------------------------------------


    # 05_custom_dialog

# from PySide6.QtWidgets import QApplication, QWidget, QDialog, QPushButton, QMessageBox, QVBoxLayout, QDialogButtonBox
# import sys

# class Dialog(QDialog):
#     def __init__(self):
#         super().__init__()

#         self.setMinimumSize(200, 100)
#         self.setMaximumSize(201, 101)
#         self.setWindowTitle("this is a dialog box")

#         button_box = QDialogButtonBox()
#         button_box.setStandardButtons(QDialogButtonBox.StandardButton.Cancel | QDialogButtonBox.StandardButton.Ok)
#         button_box.accepted.connect(self.accept)
#         button_box.rejected.connect(self.reject)

#         layoutV = QVBoxLayout(self)
#         layoutV.addStretch(1)
#         layoutV.addWidget(button_box)


# class Window(QWidget):
#     def __init__(self):
#         super().__init__()

#         self.setMinimumSize(400, 300)
#         self.setWindowTitle("simple window")

#         button = QPushButton("dialog window", self)
#         button.clicked.connect(self.dialog_flow)

#     def dialog_flow(self):
#         dialog = Dialog()

#         if dialog.exec() == QDialog.Accepted:
#             QMessageBox.information(self, "this is a message box title", "yeeeeeeeeeeeeeeeeeeeee")

# def main():
#     app = QApplication(sys.argv)
#     window = Window()

#     window.show()
#     sys.exit(app.exec())

# if __name__ == "__main__":
#     main()


# --------------------------------------------------


    # 06_dialog_model_modeless

# from PySide6.QtWidgets import ( QApplication, QWidget, QPushButton, QHBoxLayout, QVBoxLayout, 
#                                 QDialog, QLineEdit, QSpinBox, QFormLayout, QLabel, QDialogButtonBox,
#                                 QMessageBox )
# from PySide6.QtCore import QObject, Signal                                
# import sys

# class Dialog(QDialog):
#     def __init__(self, parent, name, age):
#         super().__init__(parent)

#         self.setFixedWidth(300)
#         self.setFixedHeight(200)
#         self.setWindowTitle("modes")

#         self.line_edit = QLineEdit()
#         self.line_edit.setText(name)
#         self.spin_box = QSpinBox()
#         self.spin_box.setValue(age)

#         form = QFormLayout()
#         form.addRow(QLabel("enter your name : "), self.line_edit)
#         form.addRow(QLabel("enter your age : "), self.spin_box)
        
#         button_box = QDialogButtonBox()
#         button_box.setStandardButtons(QDialogButtonBox.StandardButton.Ok | QDialogButtonBox.StandardButton.Cancel)
#         button_box.accepted.connect(self.accept)
#         button_box.rejected.connect(self.reject)

#         layoutV = QVBoxLayout(self)
#         layoutV.addLayout(form)
#         layoutV.addStretch(1)
#         layoutV.addWidget(button_box)

#     def getName(self):
#         return self.line_edit.text()
    
#     def getAge(self):
#         return self.spin_box.value()




# class Window(QWidget):
#     def __init__(self):
#         super().__init__()
#         self.__self_recognizer()

#         self.opened_windows = 0

#         self.name = None
#         self.age = 0

#         self.setFixedWidth(300)
#         self.setFixedHeight(200)
#         self.setWindowTitle("simple window")

#     def self_recognizer(self):
#         self.main_window()
#     __self_recognizer = self_recognizer

#     def main_window(self):
#         model_button = QPushButton("model window")
#         modeless_button = QPushButton("modeless window")

#         model_button.clicked.connect(self.model_starter)
#         modeless_button.clicked.connect(self.modeless_starter)

#         layoutH = QHBoxLayout()
#         layoutH.addWidget(model_button)
#         layoutH.addWidget(modeless_button)

#         button_quit = QDialogButtonBox()
#         button_quit.addButton(QDialogButtonBox.StandardButton.Ok)
#         button_quit.button(QDialogButtonBox.StandardButton.Ok).setText("Quit")
#         button_quit.accepted.connect(QApplication.quit)

#         layoutV = QVBoxLayout(self)
#         layoutV.addStretch(1)
#         layoutV.addLayout(layoutH)
#         layoutV.addStretch(1)
#         layoutV.addWidget(button_quit)

#     def model_starter(self):
#         dialog = Dialog(parent = self,
#                         name = self.name,
#                         age = self.age)

#         if dialog.exec() == QDialog.Accepted:
            
#             self.name = dialog.getName()
#             self.age = dialog.getAge()
#             QMessageBox.information(self, "Hi", f"wellcome {self.name} your age is {self.age}")
            

#     def modeless_starter(self):
#         if self.opened_windows == 0:
#             self.dialog = Dialog(parent = self,
#                             name = self.name,
#                             age = self.age)
#             self.dialog.accepted.connect(self.modeless_accept)
#             self.dialog.rejected.connect(self.modeless_reject)

#             self.dialog.show()
#             self.opened_windows = 1

#     def modeless_accept(self):
#         self.name = self.dialog.getName()
#         self.age = self.dialog.getAge()
#         QMessageBox.information(self, "Hi", f"wellcome {self.name} your age is {self.age}")

#         self.opened_windows = 0

#     def modeless_reject(self):
#         self.opened_windows = 0

    


# def main():
#     app = QApplication(sys.argv)
#     window = Window()

#     window.show()
#     sys.exit(app.exec())

# if __name__ == "__main__":
#     main()


# --------------------------------------------------


    # 07_dialog_username_password  #--SKIP--

# from PySide6.QtWidgets import QApplication, QLineEdit, QWidget, QMessageBox
# import sys

# class Window(QWidget):
#     def __init__(self):
#         super().__init__()

#         self.resize(300, 200)
#         self.setWindowTitle("simple window")

#         line_edit = QLineEdit(self)
#         line_edit.setEchoMode(QLineEdit.Password)
#         # line_edit.setEchoMode(QLineEdit.Normal)

#         QMessageBox.warning(self,"dasfsdf","asdfdf")


# def main():
#     app = QApplication(sys.argv)
#     window = Window()

#     window.show()
#     sys.exit(app.exec())

# if __name__ == "__main__":
#     main()