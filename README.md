# Pokémon Desktop Tamagotchi

Aplicación de mascota virtual para Windows usando Python + PySide6.

## Requisitos
- Python 3.11+
- Windows 10/11
- PySide6

## Instalación
```bash
python -m venv .venv
# Windows
.venv\Scripts\activate
# Linux/macOS
source .venv/bin/activate

pip install -r requirements.txt
```

## Ejecutar
```bash
python src/main.py
```

## Estructura principal
```text
pokemon-desktop/
├── src/
│   ├── main.py
│   ├── application/
│   ├── animation/
│   ├── desktop/
│   ├── movement/
│   ├── pokemon/
│   └── ui/
├── assets/
│   └── pokemon/
│       └── pikachu/
├── requirements.txt
├── README.md
└── .gitignore
```

## Añadir tus assets
Crea una carpeta como esta:

```text
assets/pokemon/pikachu/
├── idle/
│   ├── 001.png
│   ├── 002.png
│   └── 003.png
├── walk/
│   ├── 001.png
│   ├── 002.png
│   ├── 003.png
│   └── 004.png
```

Si no existen PNG, la app genera un sprite temporal para que no falle.

## Nota
Esta es una base MVP funcional para empezar a desarrollar una mascota virtual sobre el escritorio.
