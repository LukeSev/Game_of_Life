# For PyQt6 imports/constants
from PyQt6.QtWidgets import (
    QApplication,
    QLabel,
    QMessageBox,
    QWidget,
    QMainWindow, 
    QGridLayout, 
    QHBoxLayout,
    QVBoxLayout,
    QFormLayout,
    QLineEdit,
    QVBoxLayout,
    QPushButton,
    QComboBox,
    QFrame,
    QSizePolicy,
    QDialog,
    QDialogButtonBox,
    QSpacerItem
)
from PyQt6 import (
    QtGui, 
    QtWidgets
)
from PyQt6.QtCore import (
    Qt,
    QUrl,
    QTimer
)
from PyQt6.QtGui import (
    QPixmap,
    QPalette, 
    QFont
)
from PyQt6.QtMultimedia import (
    QSoundEffect,
    QMediaPlayer,
    QAudioOutput
)

# Alignment flags
LEFT    =   Qt.AlignmentFlag.AlignLeft
CENTER  =   Qt.AlignmentFlag.AlignCenter
RIGHT   =   Qt.AlignmentFlag.AlignRight

# Colors
LT_GREEN    =   '#2cf562'
LT_GREY     =   '#d7dbd8'
LT_RED      =   '#ff5640'

COLOR_ALIVE =   LT_GREEN
COLOR_DEAD  =   LT_RED
COLOR_BASE  =   LT_GREY