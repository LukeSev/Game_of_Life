from src import *
class Cell(QPushButton):
    def __init__(self, row, col, grid_width, grid_height, edge_size):
        super().__init__()
        self.button     =   QPushButton()
        self.button.setFixedHeight(edge_size)
        self.button.setFixedWidth(edge_size)
        self.button.setStyleSheet("background-color:{}".format(COLOR_BASE))
        self.button.clicked.connect(self.toggle_cell)
        self.status     =   STATUS_DEAD
        self.neighbors  =   self.get_neighbors(row, col, grid_width, grid_height)

    def get_neighbors(self, row, col, grid_width, grid_height):
        # Gets the (row,col) locations of all cell's neighbors
        # Useful for easily checking number of active cells during game
        neighbors = []

        # Check if cell at edge of grid
        if(row == 0):
            first_row = row
        else:
            first_row = row-1
        if(row == grid_height-1):
            last_row = row
        else:
            last_row = row+1

        if(col == 0):
            first_col = col
        else:
            first_col = col-1
        if(col == grid_width-1):
            last_col = col
        else:
            last_col = col+1

        # Now add the row/col pairs for each valid neighbor
        for row in range(first_row, last_row+1):
            for col in range(first_col, last_col+1):
                neighbors.append((row, col))
        return neighbors
    
    def update_cell(self, status):
        if(status == STATUS_ALIVE):
            self.button.setStyleSheet("background-color:{}".format(COLOR_ALIVE))
        elif(status == STATUS_DEAD):
            self.button.setStyleSheet("background-color:{}".format(COLOR_DEAD))
        else:
            return
        self.status = status
    
    def toggle_cell(self):
        if(self.status == STATUS_ALIVE):
            self.update_cell(STATUS_DEAD)
        elif(self.status == STATUS_DEAD):
            self.update_cell(STATUS_ALIVE)

class cellGrid():
    def __init__(self, grid_width, grid_height, cell_cols, cell_rows, cell_size):
        self.width      =   grid_width      # width in pixels
        self.height     =   grid_height     # height in pixels
        self.cell_size  =   cell_size       # Size of each dimension of cell (cells are square)
        self.cols       =   cell_cols       # Number of columns of cells
        self.rows       =   cell_rows       # Number of rows of cells
        self.cells      =   []              # The cells themselves
        self.create_grid()          
    
    def create_grid(self):
        # Creates a grid of cells, adding them to cell list as grid is generated
        # Returns grid as widget
        self.grid = QGridLayout()
        for row in range(self.rows):
            for col in range(self.cols):
                new_cell = Cell(row, col, self.width, self.height, self.cell_size)
                self.grid.addWidget(new_cell.button, row, col)
                self.cells.append(new_cell)


    
