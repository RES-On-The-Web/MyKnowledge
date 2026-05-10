# --------------------------------------------------


    # 01_signals_and_slots

# from PySide6.QtWidgets import QApplication, QWidget, QLCDNumber, QSlider, QVBoxLayout
# import sys

# class Window(QWidget):
#     def __init__(self):
#         super().__init__()
#         self.__self_recognizer()

#         self.resize(300,200)
#         self.setWindowTitle("simple window")

#         self.setLayout(self.layoutV)

#     def self_recognizer(self):

#         self.more_widget()
#         self.main_layout()
#     __self_recognizer = self_recognizer

#     def more_widget(self):

#         self.lcd_number = QLCDNumber()
#         self.slider = QSlider()
#         self.slider.setMinimum(0)
#         self.slider.setMaximum(100)
#         self.slider.valueChanged.connect(self.lcd_number.display)

#     def main_layout(self):

#         self.layoutV = QVBoxLayout()
#         self.layoutV.addWidget(self.lcd_number)
#         self.layoutV.addWidget(self.slider)

# def main():
#     app = QApplication(sys.argv)
#     window = Window()

#     window.show()
#     sys.exit(app.exec())

# if __name__ == "__main__":
#     main()


# --------------------------------------------------


    # 02_event_handler_key_press

# from PySide6.QtWidgets import QApplication, QWidget, QLabel
# from PySide6.QtCore import Qt
# import sys

# class Window(QWidget):
#     def __init__(self):
#         super().__init__()
#         self.__self_recognizer()

#         self.resize(300,200)
#         self.setWindowTitle("simple window")


#     def self_recognizer(self):
#         self.main_windgets()
#     __self_recognizer = self_recognizer
    
#     def main_windgets(self):
#         self.label = QLabel("  this is a example : press a key", self)
    
#     def keyPressEvent(self, event):
#         self.label.setText(f"{event.text()}")

#         if event.key() == Qt.Key_Escape:
#             self.close()


# def main():
#     app = QApplication(sys.argv)
#     window = Window()

#     window.show()
#     sys.exit(app.exec())

# if __name__ == "__main__":
#     main()


# --------------------------------------------------


    # 03_event_sender

# from PySide6.QtWidgets import QApplication, QWidget, QPushButton, QMainWindow, QHBoxLayout, QVBoxLayout
# import sys

# class Widget(QWidget):
#     def __init__(self, parent):
#         super().__init__()
#         self.__self_recognizer()
#         self.parent = parent

#     def self_recognizer(self):
#         self.buttons()
#         self.horizontal_layout()
#         self.vertical_layout()
#     __self_recognizer = self_recognizer

#     def buttons(self):
#         self.button1 = QPushButton("button1")
#         self.button2 = QPushButton("button2")
#         self.button1.clicked.connect(self.on_click)
#         self.button2.clicked.connect(self.on_click)

#     def horizontal_layout(self):
#         self.layoutH = QHBoxLayout()
#         self.layoutH.addWidget(self.button1)
#         self.layoutH.addWidget(self.button2)

#     def vertical_layout(self):
#         layoutV = QVBoxLayout(self)
#         layoutV.addStretch(1)
#         layoutV.addLayout(self.layoutH)

#     def on_click(self):
#         self.parent.status_bar.showMessage(self.sender().text())


# class Window(QMainWindow):
#     def __init__(self):
#         super().__init__()

#         self.resize(300, 200)
#         self.setWindowTitle("simple window")

#         self.status_bar = self.statusBar()

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


    # 04_emitting_signals

# from PySide6.QtWidgets import QApplication, QMainWindow, QLabel, QWidget
# from PySide6.QtCore import QObject, Signal
# import sys

# class Widget(QWidget):
#     def __init__(self):
#         super().__init__()
#         self.__self_recognizer()

#     def self_recognizer(self):
#         self.more_widget()
#     __self_recognizer = self_recognizer

#     def more_widget(self):
#         label = QLabel("click here to close the window", self)
#         label.setGeometry(70, 0, 300, 200)


# class Communicate(QObject):
#     closeTheWindow = Signal()

# class Window(QMainWindow):
#     def __init__(self):
#         super().__init__()

#         self.resize(300, 200)
#         self.setWindowTitle("simple window")

#         self.jump_the_flow = Communicate()
#         self.jump_the_flow.closeTheWindow.connect(self.close)

#         widget_class = Widget()
#         self.setCentralWidget(widget_class)

#     def mousePressEvent(self, event):
#         self.jump_the_flow.closeTheWindow.emit()


# def main():
#     app = QApplication(sys.argv)
#     window = Window()

#     window.show()
#     sys.exit(app.exec())

# if __name__ == "__main__":
#     main()