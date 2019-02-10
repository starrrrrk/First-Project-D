import sys,random
from PyQt5.QtWidgets import QMainWindow, QFrame, QDesktopWidget, QApplication
from PyQt5.QtCore import Qt, QBasicTimer, pyqtSignal
from PyQt5.QtGui import QPainter, QColor, QPen
from PyQt5.QtCore import QSize, QBasicTimer

class SnakeWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()
    def initUI(self):
        self.board = Board(self)
        board = self.board
        self.setCentralWidget(board)
        self.statusbar = self.statusBar()
        self.board.ScoreSignal[str].connect(self.statusbar.showMessage)
        board.start()
        self.resize(board.BoardWidth*board.scale, board.BoardHeight*board.scale)
        self.center()
        self.setWindowTitle('Змейка')
        self.show()
    def center(self):
        screen = QDesktopWidget().screenGeometry()
        size = self.geometry()
        self.move((screen.width() - size.width()) / 2,
                  (screen.height() - size.height()) / 2)
    def keyPressEvent(self, e):
        key = e.key()

        if key == Qt.Key_P:
            self.board.pause()
        elif key == Qt.Key_Right:
            self.board.direct = 0
        elif key == Qt.Key_Left:
            self.board.direct = 1
        elif key == Qt.Key_Up:
            self.board.direct = 2
        elif key == Qt.Key_Down:
            self.board.direct = 3
class Board(QFrame):
    ScoreSignal = pyqtSignal(str)
    BoardWidth = 21
    BoardHeight = 21
    speed = 500
    score = 0
    scale = 30
    snake_cords = [
        [1,0],
        [0,0],
        [-1,0]
    ]
    direct = 0
    num = 20
    apples_cords = [[random.randint(0,20),random.randint(0,20)] for i in range(num)]
    def __init__(self, parent):
        super().__init__(parent)
        self.initBoard()
    def initBoard(self):
        self.timer = QBasicTimer()
        self.timerOn = False
    def timerEvent(self, event):
        self.snake_step()
    def snake_step(self):
        scords = self.snake_cords
        acords = self.apples_cords
        for i in range(len(scords)-1,0,-1):
            scords[i][0] = scords[i - 1][0]
            scords[i][1] = scords[i - 1][1]
        if self.direct == 0:
            scords[0][0] += 1
        elif self.direct == 1:
            scords[0][0] -= 1
        elif self.direct == 2:
            scords[0][1] -= 1
        else:
            scords[0][1] += 1
        if scords[0] in scords[1:]:
            scords.pop(len(scords)-1)
        for i in acords:
            if scords[0] == i:
                acords.pop(acords.index(i))
                scords.append([scords[-1][0], scords[-1][1]])
                self.apple_update()
                self.score += 1
                break
        if scords[0][0] == 21:
            scords[0][0] = 0
        elif scords[0][0] == -1:
            scords[0][0] = 20
        if scords[0][1] == 21:
            scords[0][1] = 0
        elif scords[0][1] == -1:
            scords[0][1] = 20
        self.ScoreSignal.emit(str(self.score))
        self.speed_update()
        self.game_over()
        self.update()
    def apple_update(self):
        if len(self.apples_cords) < self.num:
            cord = [random.randint(0,20),random.randint(0,20)]
            while cord in self.apples_cords or cord in self.snake_cords:
                cord = [random.randint(0, 20), random.randint(0, 20)]
            self.apples_cords.append(cord)
    def start(self):
        self.timer.start(Board.speed, self)
        self.timerOn = True
    def pause(self):
        if self.timerOn:
            self.timer.stop()
        else:
            self.timer.start(Board.speed, self)
        self.timerOn = not self.timerOn
    def paintEvent(self, QP):
        QP = QPainter()
        QP.begin(self)
        self.drawSnake(QP)
        self.drawApples(QP)
        self.drawBoard(QP)
        QP.end()
    def drawSnake(self, QP):
        QP.setBrush(QColor(1000, 0, 200))
        for i in self.snake_cords:
            QP.drawRect(i[0]*self.scale,i[1]*self.scale, self.scale, self.scale)
    def drawApples(self, QP):
        QP.setBrush(QColor(50, 100, 50))
        for i in self.apples_cords:
            QP.drawRect(i[0] * self.scale, i[1] * self.scale, self.scale, self.scale)
    def drawBoard(self, QP):
        pen = QPen(QColor(0, 0, 0), 2, Qt.SolidLine)
        QP.drawLine(0, 0, 0, 630)
        QP.drawLine(630, 0, 630, 630)
        QP.drawLine(0, 0, 630, 0)
        QP.drawLine(0, 630, 630, 630)
    def speed_update(self):
        Board.speed = 1500//len(self.snake_cords)
        self.start()
    def game_over(self):
        if len(self.snake_cords) == 2:
            self.timer.stop()
            self.timerOn = False
            self.ScoreSignal.emit('Ты проиграл '+str(self.score)+' очков')
app = QApplication(sys.argv)
sw = SnakeWindow()
sys.exit(app.exec_())
