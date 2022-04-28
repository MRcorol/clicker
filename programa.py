import sys
from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QLabel
from PyQt5.QtWidgets import QPushButton
from PyQt5.QtWidgets import QWidget


app = QApplication(sys.argv)

# Настройка окна и его размеров.
window = QWidget()
window.setWindowTitle('PyQt5 App')
window.setGeometry(100, 100, 1000, 500)
window.setStyleSheet('background: black')


number_of_clicks = 1
score_of_clicks = 1
level_of_clicks = 0
def showHi():
    global score_of_clicks
    global number_of_clicks # НУЖНО!
    global level_of_clicks
    number_of_clicks = number_of_clicks + 5
    label_number_of_clicks.setText('Clicks: ' + str(number_of_clicks))
    level_of_clicks = level_of_clicks + 1
    label_level_of_clicks.setText('Level: ' + str(level_of_clicks))
    score_of_clicks = score_of_clicks + 20
    label_score_of_clicks.setText('Score: ' + str(score_of_clicks))


def showHi2():
    global score_of_clicks
    if score_of_clicks > 300:
        global number_of_clicks # НУЖНО!
        global level_of_clicks
        number_of_clicks = number_of_clicks + 300
        label_number_of_clicks.setText('Clicks: ' + str(number_of_clicks))
        level_of_clicks = level_of_clicks + 100
        label_level_of_clicks.setText('Level: ' + str(level_of_clicks))
        score_of_clicks = score_of_clicks + 300
        label_score_of_clicks.setText('Score: ' + str(score_of_clicks))



def showHi3():
    global score_of_clicks
    if score_of_clicks > 100000:
        global number_of_clicks # НУЖНО!
        global level_of_clicks
        number_of_clicks = number_of_clicks + 100000
        label_number_of_clicks.setText('Clicks: ' + str(number_of_clicks))
        level_of_clicks = level_of_clicks + 10000
        label_level_of_clicks.setText('Level: ' + str(level_of_clicks))
        score_of_clicks = score_of_clicks + 100000
        label_score_of_clicks.setText('Score: ' + str(score_of_clicks))

def showHi4():
    global score_of_clicks
    global level_of_clicks
    if level_of_clicks > 3333333:
        global number_of_clicks # НУЖНО!
        number_of_clicks = number_of_clicks + 50000000
        label_number_of_clicks.setText('Clicks: ' + str(number_of_clicks))
        level_of_clicks = level_of_clicks + 400000000
        label_level_of_clicks.setText('Level: ' + str(level_of_clicks))
        score_of_clicks = score_of_clicks + 10000000000000000000
        label_score_of_clicks.setText('Score: ' + str(score_of_clicks))

def showHi5():
    global score_of_clicks
    if score_of_clicks > 100000000:
        global number_of_clicks # НУЖНО!
        global level_of_clicks
        number_of_clicks = number_of_clicks + 500000000
        label_number_of_clicks.setText('Clicks: ' + str(number_of_clicks))
        level_of_clicks = level_of_clicks + 200000000
        label_level_of_clicks.setText('Level: ' + str(level_of_clicks))
        score_of_clicks = score_of_clicks + 10000000
        label_score_of_clicks.setText('Score: ' + str(score_of_clicks))  


def showHi6():
    global score_of_clicks
    global number_of_clicks
    global level_of_clicks
    number_of_clicks = 0
    label_number_of_clicks.setText('Clicks: ' + str(number_of_clicks))
    level_of_clicks = level_of_clicks * 0
    label_level_of_clicks.setText('Level: ' + str(level_of_clicks))
    score_of_clicks = 0
    label_score_of_clicks.setText('Score: ' + str(score_of_clicks))



label_number_of_clicks = QLabel('you can start if you click first button ', parent=window)
label_number_of_clicks.setStyleSheet("background-color : #0B3912; color: white")
label_number_of_clicks.move(0, 0)
label_number_of_clicks.resize(2000, 20)

label_score_of_clicks = QLabel('you can start if you click first button ', parent=window)
label_score_of_clicks.setStyleSheet("background-color : #72F086; color: white")
label_score_of_clicks.resize(2000, 20)
label_score_of_clicks.move(0, 25)

label_level_of_clicks = QLabel('you can start if you click first button ', parent=window)
label_level_of_clicks.setStyleSheet("background-color : #FF9311; color: white")
label_level_of_clicks.resize(2000, 20)
label_level_of_clicks.move(0 , 50)

# Добавление кнопки
pybutton = QPushButton(window)
pybutton.setText("5 clicks")
pybutton.resize(100,32)
pybutton.move(50, 100)
pybutton.setStyleSheet("background-color :#00FFF7; color: white")
pybutton.clicked.connect(showHi)


pybutton2 = QPushButton(window)
pybutton2.setText("300 clicks")
pybutton2.resize(100,32)
pybutton2.move(50, 150)
pybutton2.setStyleSheet("background-color : #80FF00; color: white")
pybutton2.clicked.connect(showHi2)


pybutton3 = QPushButton(window)
pybutton3.setText("100,000 clicks")
pybutton3.resize(100,32)
pybutton3.move(50, 200)
pybutton3.setStyleSheet("background-color : yellow; color; white")
pybutton3.clicked.connect(showHi3)

pybutton4 = QPushButton(window)
pybutton4.setText("????")
pybutton4.resize(100,32)
pybutton4.move(50, 250)
pybutton4.setStyleSheet("background-color : 00FFAA ; color; white")
pybutton4.clicked.connect(showHi4)

pybutton5 = QPushButton(window)
pybutton5.setText("ultar ????")
pybutton5.resize(100,32)
pybutton5.move(50, 300)
pybutton5.setStyleSheet("background-color : #FF00E0 ; color; white")
pybutton5.clicked.connect(showHi5)

pybutton6 = QPushButton(window)
pybutton6.setText("ribitgh (x0)")
pybutton6.resize(100,32)
pybutton6.move(50, 350)
pybutton6.setStyleSheet("background-color : #BFBFBF ; color; white")
pybutton6.clicked.connect(showHi6)

window.show()
sys.exit(app.exec_())
