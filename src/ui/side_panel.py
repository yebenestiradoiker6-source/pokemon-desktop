from PySide6.QtCore import Qt
from PySide6.QtWidgets import QApplication, QLabel, QVBoxLayout, QWidget


class SidePanel(QWidget):
    def __init__(self, pokemon):
        super().__init__()
        self.pokemon = pokemon
        self.is_visible = False

        screen = QApplication.primaryScreen()
        self.screen_width = screen.availableGeometry().width()
        self.screen_height = screen.availableGeometry().height()

        self.setWindowFlags(
            Qt.FramelessWindowHint
            | Qt.WindowStaysOnTopHint
            | Qt.Tool
            | Qt.WindowDoesNotAcceptFocus
        )
        self.setAttribute(Qt.WA_TranslucentBackground, True)
        self.resize(260, self.screen_height)
        self.move(self.screen_width - 260, 0)

        self.setStyleSheet("""
            QWidget {
                background: rgba(18, 18, 22, 180);
                border: 1px solid rgba(255,255,255,40);
                border-radius: 12px;
            }
            QLabel {
                color: white;
                background: transparent;
            }
        """)

        self.layout = QVBoxLayout(self)
        self.layout.setContentsMargins(16, 16, 16, 16)
        self.layout.setSpacing(10)

        self.title = QLabel("Pokémon Desktop")
        self.title.setStyleSheet("font-weight: bold; font-size: 18px;")
        self.layout.addWidget(self.title)

        self.info = QLabel()
        self.info.setWordWrap(True)
        self.layout.addWidget(self.info)

        self.refresh()

    def refresh(self):
        self.info.setText(
            f"{self.pokemon.name}\n"
            f"Estado: {self.pokemon.state}\n"
            f"Salud: {int(self.pokemon.health)}\n"
            f"Hambre: {int(self.pokemon.hunger)}\n"
            f"Felicidad: {int(self.pokemon.happiness)}\n"
            f"Energía: {int(self.pokemon.energy)}"
        )

    def toggle(self):
        self.is_visible = not self.is_visible
        if self.is_visible:
            self.show()
            self.move(self.screen_width - 260, 0)
        else:
            self.hide()
