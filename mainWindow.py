from src import *
from cellGrid import *

class Main_Window(QMainWindow):
    def __init__(self):
        super().__init__()
        
    def initUI(self):
        # Initialize window and basic layout
        self.setWindowTitle('Game of Life')
        self.setFixedSize(WIN_WIDTH, WIN_HEIGHT)
        self.generalLayout = QVBoxLayout()
        centralWidget = QWidget(self)
        centralWidget.setLayout(self.generalLayout)
        self.setCentralWidget(centralWidget)


