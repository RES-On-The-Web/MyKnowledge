# --------------------------------------------------


    # 01_checkbox

# from PySide6.QtWidgets import QApplication, QWidget, QCheckBox
# from PySide6.QtCore import Qt
# import sys

# class Window(QWidget):
#     def __init__(self):
#         super().__init__()

#         self.resize(300, 200)
#         self.setWindowTitle("simple window")

#         check_box = QCheckBox("this is a check box", self)
#         check_box.toggle()
#         check_box.setTristate(True)
#         check_box.stateChanged.connect(self.check_box_state_change)

#     def check_box_state_change(self, state):
#         state = Qt.CheckState(state)
#         if state == Qt.CheckState.Unchecked:
#             self.setWindowTitle("UnChecked")
#         elif state == Qt.CheckState.PartiallyChecked:
#             self.setWindowTitle("PChecked")
#         elif state == Qt.CheckState.Checked:
#             self.setWindowTitle("Checked")

# def main():
#     app = QApplication(sys.argv)
#     window = Window()

#     window.show()
#     sys.exit(app.exec())

# if __name__ == "__main__":
#     main()


# --------------------------------------------------


    # 02_toggle_buttons

# from PySide6.QtWidgets import QApplication, QWidget, QPushButton, QFrame, QHBoxLayout, QVBoxLayout
# from PySide6.QtGui import QColor
# import sys

# class Window(QWidget):
#     def __init__(self):
#         super().__init__()

#         self.resize(300, 200)
#         self.setWindowTitle("simple window")

#         self.color = QColor(0, 0, 0)

#         button_red = QPushButton("Red")
#         button_red.setCheckable(True)
#         button_red.clicked.connect(self.set_state)

#         button_green = QPushButton("Green")
#         button_green.setCheckable(True)
#         button_green.clicked.connect(self.set_state)

#         button_blue = QPushButton("Blue")
#         button_blue.setCheckable(True)
#         button_blue.clicked.connect(self.set_state)

#         layoutH = QHBoxLayout()
#         layoutH.addWidget(button_red)
#         layoutH.addWidget(button_green)
#         layoutH.addWidget(button_blue)

#         self.frame = QFrame()
#         self.frame.setStyleSheet("QWidget { background-color : %s }" % self.color.name())

#         layoutV = QVBoxLayout(self)
#         layoutV.addLayout(layoutH)
#         layoutV.addWidget(self.frame)

#     def set_state(self, pressed):
#         button = self.sender()
        
#         if pressed:
#             value = 255
#         else:
#             value = 0
        
#         if button.text() == "Red":
#             self.color.setRed(value)
#         elif button.text() == "Green":
#             self.color.setGreen(value)
#         elif button.text() == "Blue":
#             self.color.setBlue(value)
#         else:
#             self.color = QColor(0, 0, 0)

#         self.frame.setStyleSheet("QFrame { background-color : %s }" % self.color.name())


# def main():
#     app = QApplication()
#     window = Window()

#     window.show()
#     sys.exit(app.exec())

# if __name__ == "__main__":
#     main()


# --------------------------------------------------


    # 03_slider

# from PySide6.QtWidgets import QApplication, QWidget, QSlider, QLabel, QHBoxLayout
# from PySide6.QtGui import QPixmap
# from PySide6.QtCore import Qt
# from pathlib import Path
# import sys
# import os

# class Window(QWidget):
#     def __init__(self):
#         super().__init__()

#         self.resize(300, 200)
#         self.setWindowTitle("Simple window")

#         slider = QSlider()
#         slider.setOrientation(Qt.Horizontal)
#         slider.valueChanged.connect(self.value_changed)

#         self.label = QLabel()
#         self.path = Path(__file__).resolve().parent
#         self.label.setPixmap(QPixmap(os.path.join(self.path, "./000_[miscellaneousArea]/mute.png")))

#         layoutH = QHBoxLayout(self)
#         layoutH.addWidget(slider)
#         layoutH.addWidget(self.label)

#     def value_changed(self, value):

#         if value <= 0:
#             self.label.setPixmap(QPixmap(os.path.join(self.path, "./000_[miscellaneousArea]/mute.png")))
#         elif value <= 30:
#             self.label.setPixmap(QPixmap(os.path.join(self.path, "./000_[miscellaneousArea]/min.png")))
#         elif value <= 80:
#             self.label.setPixmap(QPixmap(os.path.join(self.path, "./000_[miscellaneousArea]/med.png")))
#         else:
#             self.label.setPixmap(QPixmap(os.path.join(self.path, "./000_[miscellaneousArea]/max.png")))


# def main():
#     app = QApplication(sys.argv)
#     window = Window()

#     window.show()
#     sys.exit(app.exec())

# if __name__ == "__main__":
#     main()


# --------------------------------------------------


    # 04_progressbar

# from PySide6.QtWidgets import QApplication, QWidget, QPushButton, QGridLayout, QProgressBar
# from PySide6.QtCore import QBasicTimer
# import sys

# class Window(QWidget):
#     def __init__(self):
#         super().__init__()

#         self.resize(300, 200)
#         self.setWindowTitle("simple window")

#         self.timer = QBasicTimer()
#         self.step = 0

#         self.progress_bar = QProgressBar()

#         self.button = QPushButton("start")
#         self.button.clicked.connect(self.start_progress_bar)

#         grid = QGridLayout(self)
#         grid.addWidget(self.progress_bar, 0, 0)
#         grid.addWidget(self.button, 0, 1)


#     def timerEvent(self, time):
#         if self.step >= 100:
#             self.timer.stop()
#             self.step = 0
#             self.button.setText("Finished")
#         else:
#             self.step += 1
#             self.progress_bar.setValue(self.step)

#     def start_progress_bar(self):
#         if self.timer.isActive():
#             self.timer.stop()
#             self.button.setText("start")
#         else :
#             self.timer.start(100, self)
#             self.button.setText("stop")



# def main():
#     app = QApplication(sys.argv)
#     window = Window()

#     window.show()
#     sys.exit(app.exec())

# if __name__ == "__main__":
#     main()


# --------------------------------------------------

    # 05_calendar

# from PySide6.QtWidgets import ( QApplication, QWidget, 
#                                 QCalendarWidget, QLabel, QHBoxLayout)
# import sys

# class Window(QWidget):
#     def __init__(self):
#         super().__init__()

#         self.resize(300, 200)
#         self.setWindowTitle("simple window")

#         calendar = QCalendarWidget()
#         calendar.clicked.connect(self.calender_connection)
#         # calendar.setGridVisible(True)
#         calendar.setVerticalHeaderFormat(QCalendarWidget.ISOWeekNumbers)

#         self.label = QLabel("this is a example")

#         layoutH = QHBoxLayout(self)
#         layoutH.addWidget(calendar)
#         layoutH.addWidget(self.label)

#     def calender_connection(self, data):
#         self.label.setText(data.toString())


# def main():
#     app = QApplication(sys.argv)
#     window = Window()

#     window.show()
#     sys.exit(app.exec())

# if __name__ == "__main__":
#     main()


# --------------------------------------------------


    # 06_qpixmap

# from PySide6.QtWidgets import ( QApplication, QWidget,
#                                 QLabel)
# from PySide6.QtGui import QPixmap
# from pathlib import Path
# import sys
# import os

# class Window(QWidget):
#     def __init__(self):
#         super().__init__()

#         self.resize(300, 200)
#         self.setWindowTitle("simple window")

#         path = Path(__file__).resolve().parent
#         label = QLabel(self)
#         label.setPixmap(QPixmap(os.path.join(path, "./000_[miscellaneousArea]/redrock.png")))


# def main():
#     app = QApplication(sys.argv)
#     window = Window()

#     window.show()
#     sys.exit(app.exec()) 

# if __name__ == "__main__":
#     main()


# --------------------------------------------------


    # 07_lineedit

# from PySide6.QtWidgets import ( QApplication, QWidget,
#                                 QLabel, QLineEdit, QHBoxLayout, QVBoxLayout, QPushButton)
# import sys

# class Window(QWidget):
#     def __init__(self):
#         super().__init__()

#         self.resize(300, 200)
#         self.setWindowTitle("simple window")
        
#         self.label = QLabel("a place to put your text in it")

#         line_edit = QLineEdit()
#         line_edit.textChanged.connect(self.line_edit_connection)

#         layoutH = QHBoxLayout()
#         layoutH.addWidget(line_edit)
#         layoutH.addWidget(self.label)

#         layoutV = QVBoxLayout(self)
#         layoutV.addLayout(layoutH)


#     def line_edit_connection(self, text):
#         self.label.setText(text)


# def main():
#     app = QApplication(sys.argv)
#     window = Window()

#     window.show()
#     sys.exit(app.exec())

# if __name__ == "__main__":
#     main()


# --------------------------------------------------


    # 08_splitter --SKIP--

# --------------------------------------------------


    # 09_combobox

# from PySide6.QtWidgets import ( QApplication, QWidget,
#                                 QComboBox, QLabel, QVBoxLayout)
# import sys

# class Window(QWidget):
#     def __init__(self):
#         super().__init__()

#         self.resize(300, 200)
#         self.setWindowTitle("simple window")

#         self.comobox = QComboBox()
#         self.comobox.addItem("hamed")
#         self.comobox.addItem("mamad")
#         self.comobox.addItem("hasan")
#         self.comobox.activated.connect(self.comobox_connection)

#         self.label = QLabel("this is a place for combobox")
#         self.label.move(0, 100)

#         layoutV = QVBoxLayout(self)
#         layoutV.addWidget(self.comobox)
#         layoutV.addWidget(self.label)

#     def comobox_connection(self, index):
#         self.label.setText(self.comobox.itemText(index))
#         self.label.adjustSize()


# def main():
#     app = QApplication(sys.argv)
#     window = Window()

#     window.show()
#     sys.exit(app.exec())

# if __name__ == "__main__":
#     main()


# --------------------------------------------------


    # 10_standard_icons

# from PySide6.QtWidgets import ( QApplication, QWidget, QStyle,
#                                 QGridLayout, QPushButton)
# from PySide6.QtGui import Qt
# import sys

# class Window(QWidget):
#     def __init__(self):
#         super().__init__()

#         self.resize(300, 200)
#         self.setWindowTitle("simple window")

#         icons = [attr for attr in dir(QStyle.StandardPixmap) if attr.startswith("SP_")]
#         grid = QGridLayout(self)
#         NUM_COLUMN = 4

#         for icon_id,icon_name in enumerate(icons):

#             name_enum = getattr(QStyle, icon_name)
#             icon = self.style().standardIcon(name_enum)

#             button = QPushButton(icon_name)
#             button.setIcon(icon)

#             row = icon_id / NUM_COLUMN
#             column = icon_id % NUM_COLUMN
#             grid.addWidget(button, row, column)


# def main():
#     app = QApplication(sys.argv)
#     window = Window()

#     window.show()
#     sys.exit(app.exec())

# if __name__ == "__main__":
#     main()


# --------------------------------------------------


    # 11_dial

# from PySide6.QtWidgets import ( QApplication, QWidget,
#                                 QDial, QLabel, QVBoxLayout)
# import sys

# class Window(QWidget):
#     def __init__(self):
#         super().__init__()

#         self.resize(300, 200)
#         self.setWindowTitle("simple window")

#         DEFAULT_VALUE = 30

#         self.label = QLabel("a label")

#         self.dial = QDial()
#         self.dial.valueChanged.connect(self.dial_connection)
#         self.dial.setValue(DEFAULT_VALUE)
#         self.dial.setRange(0, 200)
#         self.dial.setNotchesVisible(True)

#         layoutV = QVBoxLayout(self)
#         layoutV.addWidget(self.dial)
#         layoutV.addWidget(self.label)


#     def dial_connection(self):
#         self.label.setText(f"{self.dial.value()}")

# def main():
#     app = QApplication(sys.argv)
#     window = Window()

#     window.show()
#     sys.exit(app.exec())

# if __name__ == "__main__":
#     main()


# --------------------------------------------------


    # 12_context_menu

# from PySide6.QtWidgets import QApplication, QWidget, QMenu, QMessageBox
# import sys

# class Window(QWidget):
#     def __init__(self):
#         super().__init__()

#         self.resize(300, 200)
#         self.setWindowTitle("simple window")

#         self.right_click_menu = QMenu(self)
#         right_click_menu__submenu_colors = QMenu("color")
#         right_click_menu__submenu_window = QMenu("window")


#         action__submenu_color = right_click_menu__submenu_colors.addAction("red")
#         action__submenu_color = right_click_menu__submenu_colors.addAction("blue")
#         action__submenu_color = right_click_menu__submenu_colors.addAction("green")
#         right_click_menu__submenu_colors.triggered.connect(self.action__submenu_color_connection)

#         action__submenu_window__normal = right_click_menu__submenu_window.addAction("normal")
#         action__submenu_window__normal.triggered.connect(self.action__submenu_window__normal_connection)
#         action__submenu_window__minimize = right_click_menu__submenu_window.addAction("minimize")
#         action__submenu_window__minimize.triggered.connect(self.action__submenu_window__minimize_connection)
#         action__submenu_window__maximize = right_click_menu__submenu_window.addAction("maximize")
#         action__submenu_window__maximize.triggered.connect(self.action__submenu_window__maximize_connection)

#         action_right_click_menu__message =  self.right_click_menu.addAction("show message")
#         action_right_click_menu__message.triggered.connect(self.action_right_click_menu__message_connection)

#         action_right_click_menu__checking = self.right_click_menu.addAction("checked item")
#         action_right_click_menu__checking.setCheckable(True)
#         action_right_click_menu__checking.triggered.connect(self.action_right_click_menu__checking_connection)

#         right_click_menu__sep1 = self.right_click_menu.addSeparator()
#         self.right_click_menu.addMenu(right_click_menu__submenu_colors)
#         self.right_click_menu.addMenu(right_click_menu__submenu_window)
#         right_click_menu__sep2 = self.right_click_menu.addSeparator()

#         action_right_click_menu__quit = self.right_click_menu.addAction("quit")
#         action_right_click_menu__quit.triggered.connect(self.close)
    
#     def action_right_click_menu__message_connection(self):
#         QMessageBox().information(self, "a messge", "hello world")

#     def action_right_click_menu__checking_connection(self, checked : bool):
#         QMessageBox().information(self, "message", f"checked : {checked}")
#     def contextMenuEvent(self, event):
#         self.right_click_menu.exec(event.globalPos())

#     def action__submenu_color_connection(self, action):
#         QMessageBox().information(self, "a message", f"{action.text()}")

#     def action__submenu_window__normal_connection(self):
#         self.showNormal()

#     def action__submenu_window__minimize_connection(self):
#         self.showMinimized()

#     def action__submenu_window__maximize_connection(self):
#         self.showMaximized()

# def main():
#     app = QApplication(sys.argv)
#     window = Window()

#     window.show()
#     sys.exit(app.exec())

# if __name__ == "__main__":
#     main()


# --------------------------------------------------


    # 13_tabs --SKIP--