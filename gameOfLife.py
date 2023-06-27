from mainWindow import *

def main():
    app = QApplication([])
    window = Main_Window() 
    sys.exit(app.exec())

if __name__ == "__main__":
    main()