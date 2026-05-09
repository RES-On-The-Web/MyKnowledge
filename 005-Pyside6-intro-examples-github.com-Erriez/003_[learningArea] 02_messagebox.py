# --------------------------------------------------


    # 01_messagebox_question

# from PySide6.QtWidgets import QApplication, QWidget, QLabel, QMessageBox
# from PySide6.QtCore import Qt
# import sys

# class Window(QWidget):
#     def __init__(self):
#         super().__init__()

#         self.resize(1920,1040)
#         self.setWindowTitle("simple window")

#         label = QLabel("close this window to show the question", self)
#         label.move(500,500)
    
#     def closeEvent(self, event):

#         answer = QMessageBox.question(  self,
#                                         "Message",
#                                         "are you sure ?",
#                                         QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No,
#                                         QMessageBox.StandardButton.No
#                                         )
#         if answer == QMessageBox.StandardButton.Yes:
#             event.accept()
#         else:
#             event.ignore()



# def main():
#     app = QApplication(sys.argv)
#     window = Window()

#     window.show()
#     sys.exit(app.exec())

# if __name__ == "__main__":
#     main()


# --------------------------------------------------


    # 02_messagebox_resizable //FULL OF BUGS & IT'S NOT WORKING WELL