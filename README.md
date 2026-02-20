🖥️ Sistema de Inventario de Computadores (Python + JSON)
Este es un proyecto simple pero completo hecho en Python, donde se gestiona un inventario de computadores usando:

Listas
Diccionarios
Sets
Funciones
Manejo de errores
Menú interactivo
Persistencia de datos en JSON

Permite registrar PCs, buscar por serial, mostrar el inventario completo y guardar todo en disco para no perder la información.

🚀 Funcionalidades principales
✔ Registrar PC

Solicita marca, RAM, disco y serial.
Valida que el serial no esté repetido.
Guarda automáticamente el inventario en un archivo JSON.

✔ Buscar PC por serial

Permite encontrar un computador mediante su serial.
Muestra toda la información del equipo si existe.

✔ Mostrar Inventario

Muestra todos los computadores registrados.

✔ Datos persistentes

El inventario se carga automáticamente desde data/inventario.json.
Los cambios se guardan cada vez que registras un PC.


📁 Estructura del Proyecto
inventario_pc/
│
├── src/
│   └── main.py
│
├── data/
│   └── inventario.json
│
└── README.md

src/ → contiene el código principal
data/ → almacena el archivo JSON
README.md → documentación del proyecto

🧠 ¿Qué tecnologías se usaron?

Python 3
Módulo estándar json
Estructuras de datos fundamentales:

list
dict
set


Manejo de errores con try/except
Entrada de usuario con input()


▶️ ¿Cómo ejecutar el proyecto?

Abre una terminal dentro del proyecto.
Ve a la carpeta src/:

cd src


Ejecuta:

python main.py


¡Listo! Te aparecerá el menú interactivo.


🧩 Ejemplo del menú
===== MENÚ INVENTARIO =====
1. Registrar PC
2. Buscar PC por serial
3. Mostrar inventario
4. Salir


💾 ¿Cómo funciona la persistencia de datos?
El inventario se guarda en:
data/inventario.json

Cada vez que registras un PC:

Se actualiza el archivo
Los datos quedan almacenados incluso si cierras el programa

Al abrirlo de nuevo, el programa carga el JSON automáticamente.

🛠 Posibles mejoras futuras

Exportar inventario en CSV
Soporte para borrar o editar equipos
Validación más estricta de datos
Interfaz gráfica
Versión con clases (POO)


👤 Autor
Edwin Hernando Sánchez
Proyecto personal de repaso y portafolio.