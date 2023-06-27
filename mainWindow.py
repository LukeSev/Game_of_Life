from src import *
from cellGrid import *

class Main_Window(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()
        
    def initUI(self):
        # Initialize window and basic layout
        self.setWindowTitle('Game of Life')
        self.setFixedSize(WIN_WIDTH, WIN_HEIGHT)
        self.generalLayout = QVBoxLayout()
        centralWidget = QWidget(self)
        centralWidget.setLayout(self.generalLayout)
        self.setCentralWidget(centralWidget)
        title = QLabel(self)
        title.setText("Welcome to the Game of Life")
        cGrid = cellGrid(WIN_WIDTH, WIN_WIDTH, CELLS_PER_SIDE, CELLS_PER_SIDE, int(WIN_WIDTH/(CELLS_PER_SIDE)))
        self.generalLayout.addWidget(title)
        self.generalLayout.addLayout(cGrid.grid)

        self.center()
        self.show()

    def center(self):
        qRect = self.frameGeometry()
        centerPoint = QtGui.QGuiApplication.primaryScreen().availableGeometry().center()
        qRect.moveCenter(centerPoint)
        self.move(qRect.topLeft())


