from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QHBoxLayout, QVBoxLayout, QLineEdit, QPushButton

def firstWindow():
    global numButton
    firstWin = QWidget()
    firstWin.setWindowTitle('Calc')
    firstWin.setFixedSize(150,100)

    title = QLabel('Enter Time in hours:')

    numButton = QLineEdit()

    enterButton = QPushButton('Enter')
    enterButton.clicked.connect(showResWin)

    v_line = QVBoxLayout()
    v_line.addWidget(title, alignment=Qt.AlignCenter)
    v_line.addWidget(numButton)
    v_line.addWidget(enterButton, alignment=Qt.AlignCenter)

    firstWin.setLayout(v_line)

    return firstWin

def showResWin():
    global resWin
    firstWin.hide()
    resWin = resultWindow()
    resWin.show()

def resultWindow():
    resWin = QWidget()
    resWin.setWindowTitle('Result')
    answer = QLabel()
    answer.setText(f'{numButton.text()} * 60')
    
    v_line = QVBoxLayout()
    v_line.addWidget(answer)

    resWin.setLayout(v_line)

    return resWin

app = QApplication([])

firstWin = firstWindow()
firstWin.show()

app.exec_()