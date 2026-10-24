from pathlib import Path

from PySide6.QtCore import QTimer
from PySide6.QtGui import QKeySequence, QShortcut
from PySide6.QtWidgets import QApplication

from src.animation.animation_player import AnimationPlayer
from src.animation.sprite_loader import SpriteLoader
from src.application.config import DEFAULT_NAME, DEFAULT_POKEMON, PROJECT_ROOT
from src.desktop.desktop_manager import DesktopOverlay
from src.movement.movement_controller import MovementController
from src.pokemon.pokemon import Pokemon
from src.ui.side_panel import SidePanel


class PokemonDesktopApp:
    def __init__(self, project_root: Path | None = None):
        self.project_root = project_root or PROJECT_ROOT
        self.app = QApplication([])

        self.pokemon = Pokemon(
            species=DEFAULT_POKEMON,
            name=DEFAULT_NAME,
            x=200,
            y=200,
            width=96,
            height=96,
            speed=120.0,
            direction=1,
            hunger=75,
            happiness=80,
            energy=70,
            health=100,
        )

        self.sprite_loader = SpriteLoader(self.project_root)
        idle_frames = self.sprite_loader.load_animation("pikachu", "idle")
        walk_frames = self.sprite_loader.load_animation("pikachu", "walk")

        self.animation = AnimationPlayer(idle_frames or walk_frames, fps=8, loop=True)
        self.overlay = DesktopOverlay(self.pokemon)
        self.overlay.set_animation_player(self.animation)
        self.overlay.show()

        self.side_panel = SidePanel(self.pokemon)
        self.side_panel.hide()

        self.movement = MovementController(self.pokemon, 1920, 1080)

        self.timer = QTimer()
        self.timer.timeout.connect(self.tick)
        self.timer.start(16)

        QShortcut(QKeySequence("Ctrl+Shift+P"), self.overlay, activated=self.toggle_panel)

    def tick(self):
        self.movement.update(0.016)
        self.animation.update()
        self.overlay.repaint()
        self.side_panel.refresh()

    def toggle_panel(self):
        self.side_panel.toggle()
        self.overlay.set_click_through(not self.side_panel.is_visible)

    def run(self):
        self.app.exec()

    def close(self):
        self.timer.stop()
