from pathlib import Path
import traceback

from src.application.app import PokemonDesktopApp


def main():
    try:
        root = Path(__file__).resolve().parent.parent
        app = PokemonDesktopApp(root)
        app.run()
    except Exception as exc:
        print("\nERROR: No se pudo iniciar Pokémon Desktop.")
        print(f"Detalle: {exc}\n")
        traceback.print_exc()
        raise


if __name__ == "__main__":
    main()
