import json
from pathlib import Path

RUTA_INVENTARIO = Path("data/inventario.json")


def cargar_inventario() -> list[dict]:
    if not RUTA_INVENTARIO.exists():
        return []

    try:
        with RUTA_INVENTARIO.open("r", encoding="utf-8") as f:
            return  json.load(f)
    except FileNotFoundError:
        print("Archivo de inventario no encontrado. Se iniciará un nuevo inventario.")
        return []
    except json.JSONDecodeError:
        print("Error: El archivo de inventario está corrupto. Se iniciará un nuevo inventario.")
        return []
    
def guardar_inventario(inventario: list[dict]) -> None:
        
    RUTA_INVENTARIO.parent.mkdir(parents=True, exist_ok=True)
    with RUTA_INVENTARIO.open("w", encoding="utf-8") as f:
        json.dump(inventario, f, ensure_ascii=False, indent=4)


