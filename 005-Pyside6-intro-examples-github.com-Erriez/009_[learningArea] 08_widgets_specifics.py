# --------------------------------------------------


    # 01_set_focus

# from PySide6.QtWidgets import QApplication, QWidget, QLineEdit, QVBoxLayout, QMainWindow
# import sys

# class Window(QMainWindow):
#     def __init__(self):
#         super().__init__()

#         self.resize(300, 200)
#         self.setWindowTitle("simple window")

#         line_edit_1 = QLineEdit("")
#         line_edit_2 = QLineEdit("")

#         layoutV = QVBoxLayout()
#         layoutV.addWidget(line_edit_1)
#         layoutV.addWidget(line_edit_2)

#         widget = QWidget()
#         widget.setLayout(layoutV)

#         self.setCentralWidget(widget)

#         line_edit_2.setFocus()

# def main():
#     app = QApplication(sys.argv)
#     window = Window()

#     window.show()
#     sys.exit(app.exec())

# if __name__ == "__main__" :
#     main()