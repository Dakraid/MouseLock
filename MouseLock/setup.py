from cx_Freeze import setup, Executable

base = None    

executables = [Executable("MouseLock.py", base=base)]

packages = ["idna"]
options = {
    'build_exe': {    
        'packages':packages,
    },    
}

setup(
    name = "MouseLock",
    options = options,
    version = "1.2.1",
    description = 'MouseLock limits your mouse cursor to one area/screen',
    executables = executables
)
