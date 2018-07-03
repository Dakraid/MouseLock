from cx_Freeze import setup, Executable

base = None    

executables = [Executable("MouseLock.py", base=base)]

packages = ["idna"]
options = {
    'build_exe': {    
        'packages':["win32gui","time","getopt","sys"],
        'optimize': 2
    },    
}

target = Executable(
    script="MouseLock.py",
    icon="icon.ico"
)

setup(
    name = "MouseLock",
    options = options,
    version = "1.2.3",
    description = 'MouseLock limits your mouse cursor to one area/screen',
    executables = [target]
)
