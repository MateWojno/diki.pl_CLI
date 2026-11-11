from cx_Freeze import setup, Executable

setup(
    name =   'diki',
    version = "1.0.1",
    description = "A lightweight command-line interface tool written in Python that fetches English word translations directly from [diki.pl](https://www.diki.pl/).",
    executables = [Executable("diki.py")]
)