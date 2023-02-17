from shutil import copyfile
from platform import system as platform
from distutils.core import setup

setup(
    name='Aurora',
    version='1.0',
    packages=['aurora'],
    requirements=[
        'gitpython',
        'psutil',
        'cli-args-system'
        'git+https://github.com/mateusmoutinho/PySchema'
        ],
    url='https://github.com/mateusmoutinho/Aurora',
    license='MIT',
    author='Mateus Moutinho',
    author_email='mateusmoutinho01@gmial.com',
    description=''
)

