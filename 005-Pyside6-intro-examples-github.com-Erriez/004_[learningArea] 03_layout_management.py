# --------------------------------------------------


    # 01_absolute_positioning

# from PySide6.QtWidgets import QApplication, QWidget, QLabel
# import sys

# class Window(QWidget):
#     def __init__(self):
#         super().__init__()

#         self.resize(1920,1040)
#         self.setWindowTitle("simple window")
        

#         label1 = QLabel("this is",self)
#         label1.move(100,50)

#         label2 = QLabel("my",self)
#         label2.move(130,60)

#         label3 = QLabel("windows", self)
#         label3.move(150,70)


# def main():
#     app = QApplication(sys.argv)
#     window = Window()

#     window.show()
#     sys.exit(app.exec())


# if __name__ == "__main__":
#     main()


# --------------------------------------------------


    # 02_box_layout

# from PySide6.QtWidgets import QApplication, QWidget, QPushButton, QHBoxLayout, QVBoxLayout
# import sys

# class Window(QWidget):
#     def __init__(self):
#         super().__init__()

#         self.resize(1920,1010)
#         self.setWindowTitle("simple window")

#         button_ok = QPushButton("OK")
#         button_cancel = QPushButton("CANCEL")

#         layoutH = QHBoxLayout()
#         layoutH.addStretch(1)
#         layoutH.addWidget(button_ok)
#         layoutH.addWidget(button_cancel)

#         layoutV = QVBoxLayout()
#         layoutV.addStretch(1)
#         layoutV.addLayout(layoutH)

#         self.setLayout(layoutV)


# def main():
#     app = QApplication()
#     window = Window()

#     window.show()
#     sys.exit(app.exec())


# if __name__ == "__main__":
#     main()


# --------------------------------------------------


    # 03_grid_layout

# from PySide6.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QGridLayout
# import sys

# class Window(QWidget):
#     def __init__(self):
#         super().__init__()

#         self.setWindowTitle("simple window")

#         grid = QGridLayout()

#         button_names = [['Cls', 'Bck', '', 'Close'],
#                         ['7', '8', '9', '/'],
#                         ['4', '5', '6', '*'],
#                         ['1', '2', '3', '-'],
#                         ['0', '.', '=', '+']]

#         for row,_ in enumerate(button_names):
#             for column,name in enumerate(button_names[row]):
#                 if not name:
#                     grid.addWidget(QLabel(name), row, column)
#                 else:
#                     grid.addWidget(QPushButton(name), row, column)
        
#         self.setLayout(grid)


# def main():
#     app = QApplication(sys.argv)
#     window = Window()

#     window.show()
#     sys.exit(app.exec())

# if __name__ == "__main__":
#     main()


# --------------------------------------------------


    # 04_grid_layout_span

# from PySide6.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QGridLayout, QSizePolicy
# import sys

# class Window(QWidget):
#     def __init__(self):
#         super().__init__()

#         self.resize(300,200)
#         self.setWindowTitle("simple window")

#         title = QLabel("Title")
#         email = QLabel("Email")
#         moreInfo = QLabel("More Info")

#         title_edit = QLineEdit()
#         email_edit = QLineEdit()
#         moreInfo_edit = QLineEdit()
#         moreInfo_edit.setSizePolicy(QSizePolicy.Expanding,QSizePolicy.Preferred)

#         grid = QGridLayout()
#         grid.setSpacing(5)

#         grid.addWidget(title, 1, 0)
#         grid.addWidget(email, 2, 0)
#         grid.addWidget(moreInfo, 3, 0)

#         grid.addWidget(title_edit, 1, 1)
#         grid.addWidget(email_edit, 2, 1)
#         grid.addWidget(moreInfo_edit, 3, 1, 5, 1)

#         self.setLayout(grid)

# def main():
#     app = QApplication(sys.argv)
#     window = Window()

#     window.show()
#     sys.exit(app.exec())

# if __name__ == "__main__":
#     main()


# ------------------------------------------------


    # 05_resizable_window

# from PySide6.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QDialogButtonBox, QHBoxLayout, QVBoxLayout, QMessageBox
# from PySide6.QtCore import Qt
# import sys

# class Window(QWidget):
#     def __init__(self):
#         super().__init__()
#         self.__self_recognizer()


#         self.resize(300,200)
#         self.setWindowTitle("simple window")

#         self.setLayout(self.layoutV)


#     def self_recognizer(self):
#         self.horizontal_layout_1()
#         self.horizontal_layout_2()
#         self.vertical_layout()
#     __self_recognizer = self_recognizer

#     def accepted(self):
#         QMessageBox.information(self, "a message", "accepted")
#     def rejected(self):
#         QMessageBox.information(self, "a message", "rejected")

#     def horizontal_layout_1(self):
#         self.layoutH1 = QHBoxLayout()
#         self.layoutH1.addWidget(QLabel("Name"))
#         self.layoutH1.addWidget(QLineEdit())

#     def horizontal_layout_2(self):
#         buttonBox = QDialogButtonBox()
#         buttonBox.setStandardButtons(QDialogButtonBox.StandardButton.Cancel | QDialogButtonBox.StandardButton.Ok)
#         buttonBox.accepted.connect(self.accepted)
#         buttonBox.rejected.connect(self.rejected)

#         self.layoutH2 = QHBoxLayout()
#         self.layoutH2.addWidget(buttonBox)
#         self.layoutH2.setAlignment(Qt.AlignRight)

#     def vertical_layout(self):
#         self.layoutV = QVBoxLayout()
#         self.layoutV.addLayout(self.layoutH1)
#         self.layoutV.addStretch(1)
#         self.layoutV.addLayout(self.layoutH2)



# def main():
#     app = QApplication(sys.argv)
#     window = Window()

#     window.show()
#     sys.exit(app.exec())

# if __name__ == "__main__":
#     main()


# ------------------------------------------------


    # 06_basic_layouts

# from PySide6.QtWidgets import   QApplication, QWidget, QHBoxLayout, QVBoxLayout, QGroupBox, QPushButton, QLabel, QLineEdit, QGridLayout, QTextEdit, QFormLayout, QComboBox, QSpinBox, QDialogButtonBox
# import sys

# class Window(QWidget):
#     def __init__(self):
#         super().__init__()
#         self.__self_recognizer()

#         self.setWindowTitle("simple window")
#         self.setLayout(self.main_layout)


#     def self_recognizer(self):
#         self.group_box_layer()
#         self.group_box_grid()
#         self.group_box_form()
#         self.other_elements()
#         self.main_layout()
#     __self_recognizer = self_recognizer


#     def group_box_layer(self):
#         self.groupBoxLayout = QGroupBox("horizontal layout")
#         layout = QHBoxLayout()

#         for i in range(4):
#             button = QPushButton(f"button {i}")
#             layout.addWidget(button)
        
#         self.groupBoxLayout.setLayout(layout)

#     def group_box_grid(self):
#         self.groupBoxGrid = QGroupBox("grid layout")
#         grid = QGridLayout()

#         for i in range(3):
#             label = QLabel(f"Line {i} : ")
#             lineEdit = QLineEdit()
#             grid.addWidget(label, i, 0)
#             grid.addWidget(lineEdit, i, 1)

#         textEdit = QTextEdit()
#         grid.addWidget(textEdit, 0, 2, 3, 2)

#         grid.setColumnStretch(1,10)
#         grid.setColumnStretch(2,20)
#         self.groupBoxGrid.setLayout(grid)

#     def group_box_form(self):
#         self.groupBoxForm = QGroupBox()
#         form = QFormLayout()

#         form.addRow(QLabel("Line Edit : "), QLineEdit("enter your text"))
#         comboBox = QComboBox()
#         comboBox.addItems(["hamed", "mamad", "hasan"])
#         form.addRow(QLabel("combo box : "), comboBox)
#         form.addRow(QLabel("spin box : "), QSpinBox())

#         self.groupBoxForm.setLayout(form)

#     def other_elements(self):
#         self.textEdit = QTextEdit()
#         self.textEdit.setPlainText("this is a example text")

#         self.buttonBox = QDialogButtonBox()
#         self.buttonBox.setStandardButtons(QDialogButtonBox.StandardButton.Cancel | QDialogButtonBox.StandardButton.Ok)
#         # buttonBox.accepted.connect()
#         # buttonbox.rejected.connect()


#     def main_layout(self):
#         self.main_layout = QVBoxLayout()
        
#         self.main_layout.addWidget(QLabel('file'))

#         self.main_layout.addWidget(self.groupBoxLayout)
#         self.main_layout.addWidget(self.groupBoxGrid)
#         self.main_layout.addWidget(self.groupBoxForm)

#         self.main_layout.addWidget(self.textEdit)
#         self.main_layout.addWidget(self.buttonBox)
        


# def main():
#     app = QApplication(sys.argv)
#     window = Window()

#     window.show()
#     sys.exit(app.exec())

# if __name__ == "__main__":
#     main()