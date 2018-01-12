import sys
from cx_Freeze import setup, Executable

setup(
    name = "SnakeGame",
    version = "1.0",
    description = "Classic snake game",
    executables = [Executable("SnakeGame.py")])