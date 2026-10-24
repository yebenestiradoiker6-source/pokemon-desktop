from pathlib import Path
import sys
import traceback

PROJECT_ROOT = Path(__file__).resolve().parent.parent
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))

from src.application.app import PokemonDesktopApp


def main():
    try:
        app = PokemonDesktopApp(PROJECT_ROOT)
        app.run()
    except Exception as exc:
        print("\nERROR: No se pudo iniciar Pokémon Desktop.")
        print(f"Detalle: {exc}\n")
        traceback.print_exc()
        raise


if __name__ == "__main__":
    main()
