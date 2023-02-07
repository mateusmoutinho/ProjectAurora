from os import system,remove,makedirs
import shutil
from platform import system as platform

shutil.rmtree('build', ignore_errors=True)
shutil.rmtree('dist', ignore_errors=True)


if platform() == 'Windows':
    #build the binary
    system('pyinstaller  --onefile  aurora/main.py')
    shutil.move('dist/main.exe', 'outputs/binarys/Aurora.exe')

if  platform() == 'Linux':
    #build the binary
    system('pyinstaller --onefile aurora/main.py')
    shutil.move('dist/main', 'outputs/binarys/Aurora')

shutil.rmtree('build', ignore_errors=True)
shutil.rmtree('dist', ignore_errors=True)