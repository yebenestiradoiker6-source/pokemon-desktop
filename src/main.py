from pathlib import Path

from src.application.app import PokemonDesktopApp

if __name__ == "__main__":
    root = Path(__file__).resolve().parent.parent
    app = PokemonDesktopApp(root)
    app.run()
