from os import system,remove,makedirs
import shutil
from platform import system as platform



if platform() == 'Windows':
    #build the binary
    system('pyinstaller  --onefile --name=Aurora.exe  aurora/main.py')
    shutil.move('dist/Aurora.exe', 'outputs/binarys/Aurora.exe')

if  platform() == 'Linux':
    #build the binary
    system('pyinstaller  --onefile --name=AuroraLinux  aurora/main.py')
    shutil.move('dist/AuroraLinux', 'outputs/binarys/Aurora')
