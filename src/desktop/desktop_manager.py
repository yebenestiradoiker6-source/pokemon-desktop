from PySide6.QtCore import Qt
from PySide6.QtWidgets import QApplication, QWidget


class DesktopOverlay(QWidget):
    def __init__(self, pokemon):
        super().__init__()
        self.pokemon = pokemon
        self.animation_player = None

        screen = QApplication.primaryScreen()
        geom = screen.availableGeometry()
        self.setGeometry(geom)

        self.setWindowFlags(
            Qt.FramelessWindowHint
            | Qt.WindowStaysOnTopHint
            | Qt.Tool
            | Qt.WindowDoesNotAcceptFocus
        )
        self.setAttribute(Qt.WA_TranslucentBackground, True)
        self.setAttribute(Qt.WA_ShowWithoutActivating, True)
        self.setAttribute(Qt.WA_TransparentForMouseEvents, True)

    def set_animation_player(self, animation_player):
        self.animation_player = animation_player

    def set_click_through(self, enabled: bool):
        self.setAttribute(Qt.WA_TransparentForMouseEvents, enabled)

    def paintEvent(self, event):
        if self.animation_player is None:
            return

        frame = self.animation_player.current_frame()
        if frame is None:
            return

        x = int(self.pokemon.x)
        y = int(self.pokemon.y)
        self.render(frame, x, y)

    def render(self, pixmap, x: int, y: int):
        from PySide6.QtGui import QPainter
        painter = QPainter(self)
        painter.setRenderHint(QPainter.Antialiasing, False)
        painter.drawPixmap(x, y, pixmap)
        painter.end()
