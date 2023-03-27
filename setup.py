import sys
from cx_Freeze import setup, Executable


base = None
if sys.platform == "win32":
    base = "Win32GUI"

executable=[Executable("app.py", base=base)]

setup(
    name="Meu App",
    version="0.1",
    description="Minha 1° Aplicação!",
    executables=executable
)