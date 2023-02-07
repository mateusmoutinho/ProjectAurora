from os import system,remove
import shutil
system('pyinstaller  --onefile --name=AuroraLinux  ../aurora/run.py')
#move the executable to the bin folder
shutil.move('dist/AuroraLinux', '../binarys/AuroraLinux')
#remove the build folder
shutil.rmtree('build')
#remove the dist folder
shutil.rmtree('dist')
#remove the spec file
remove('Aurora.spec')
#remove the AuroraLinux.sepec
remove('AuroraLinux.spec')