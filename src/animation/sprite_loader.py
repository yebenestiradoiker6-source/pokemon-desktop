from pathlib import Path

from PySide6.QtCore import Qt
from PySide6.QtGui import QImage, QPainter, QPixmap


class SpriteLoader:
    def __init__(self, project_root: Path):
        self.project_root = project_root

    def load_animation(self, species_name: str, animation_name: str):
        folder = self.project_root / "assets" / "pokemon" / species_name / animation_name

        if folder.exists():
            pngs = sorted(folder.glob("*.png"))
            if pngs:
                frames = []
                for frame_path in pngs:
                    pixmap = QPixmap(str(frame_path))
                    if not pixmap.isNull():
                        frames.append(pixmap)
                if frames:
                    return frames

        return self._generate_placeholder_frames()

    def _generate_placeholder_frames(self):
        width = 96
        height = 96
        frames = []

        for offset in [0, 4, 0, -4]:
            image = QImage(width, height, QImage.Format_ARGB32)
            image.fill(Qt.transparent)

            painter = QPainter(image)
            painter.setRenderHint(QPainter.Antialiasing)

            painter.setBrush(Qt.yellow)
            painter.setPen(Qt.darkYellow)
            painter.drawEllipse(22 + offset, 18, 40, 38)

            painter.setPen(Qt.black)
            painter.drawEllipse(30 + offset, 28, 7, 7)
            painter.drawEllipse(49 + offset, 28, 7, 7)
            painter.drawLine(38 + offset, 38, 46 + offset, 38)

            painter.setBrush(Qt.darkYellow)
            painter.drawRect(28 + offset, 56, 8, 18)
            painter.drawRect(48 + offset, 56, 8, 18)
            painter.drawLine(62 + offset, 36, 76 + offset, 24)

            painter.end()
            frames.append(QPixmap.fromImage(image))

        return frames
