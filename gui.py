from play import TicTacToe
from PyQt5.QtWidgets import QMainWindow, QPushButton, QGridLayout, QWidget, QLabel, QVBoxLayout
from PyQt5 import QtGui, QtCore


class RestartWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.label = QLabel('')
        self.restart_button = QPushButton('Restart')

        layout = QVBoxLayout()

        layout.addWidget(self.label)
        layout.addWidget(self.restart_button)
        self.setLayout(layout)

        self.restart_button.clicked.connect(self.close)

    def if_win(self, text):
        self.label.setText(text)


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('TicTacToe')
        self.setFixedSize(300,300)

        self.tic_tac_toe = TicTacToe()

        self.widget = QWidget()
        self.restart_window = RestartWindow()

        layout = QGridLayout()

        self.button_list = []
        for i in range(3):
            button_row = []
            for j in range(3):
                button = QPushButton()
                button.clicked.connect(self.on_clicked)
                button.setFixedSize(90,90)
                button_row.append(button)
                layout.addWidget(button, i, j)
            self.button_list.append(button_row)

        self.widget.setLayout(layout)
        self.setCentralWidget(self.widget)

        self.restart_window.restart_button.clicked.connect(self.clear)

    def clear(self):
        for i in range(3):
            for j in range(3):
                self.button_list[i][j].setIcon(QtGui.QIcon())
                self.tic_tac_toe.field[i][j] = 0

    def win_text(self, num) -> str:
        str1 = 'Tic win'
        str2 = 'Tac win'
        str3 = 'Draw'
        if num == 1: return str1
        elif num == 2: return str2
        elif num == 3: return str3
        else: return ''

    def on_clicked(self):
        x = self.widget.layout().indexOf(self.sender()) // 3
        y = self.widget.layout().indexOf(self.sender()) % 3
        self.tic_tac_toe.set_coords(x, y)
        self.tic_tac_toe.do_motion()
        text = self.win_text(self.tic_tac_toe.check_win())
        if self.tic_tac_toe.field[x][y] == 1:
            self.button_list[x][y].setIcon(QtGui.QIcon('pictures/tic.jpg'))
            self.button_list[x][y].setIconSize(QtCore.QSize(90, 90))
        elif self.tic_tac_toe.field[x][y] == 2:
             self.button_list[x][y].setIcon(QtGui.QIcon('pictures/tac.jpg'))
             self.button_list[x][y].setIconSize(QtCore.QSize(90, 90))
        if text != '':
            self.restart_window.if_win(text)
            self.restart_window.show()