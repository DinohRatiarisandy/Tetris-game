import sys
from cx_Freeze import setup, Executable

# Chemin vers l'icône
icon_path = "icon.png"

# Nom de votre fichier exécutable
exe_name = "play Tetris"

# Paramètres de configuration de Cx_Freeze
build_exe_options = {
    "packages": ["pygame"],
    "excludes": [
        'PyQt6', 'scipy', 'numpy', 'jupyter', 'altgraph', 'asyncio', \
        'cffi', 'concurrent', 'ctypes', 'distutils', 'email', 'html', \
        'http', 'jinja2', 'json', 'lib2to3', 'logging', 'markupsafe', \
        'multiprocessing', 'ordlookup', 'packaging', 'pkg_resources', \
        'pycparser', 'pydoc_data', 'PyInstaller', 'pyparsing', 'pywin32_system32', \
        'setuptools', 'tcl8', 'test', 'tk8.6', 'tkinter', 'unittest', \
        'urillib', 'win32com', 'win32ctypes', 'xml', 'xmlrpc', 'zipp'
    ],
    "include_files": [icon_path, 'mario_font.ttf']
}

# Création de l'exécutable
base = None
if sys.platform == "win32":
    base = "Win32GUI"

exe = Executable(script="main.py", base=base, target_name=exe_name, icon=icon_path)

setup(name="Tetris on windows",
      version="1.0",
      description="Tetris build with Pygame",
      options={"build_exe": build_exe_options},
      executables=[exe])
