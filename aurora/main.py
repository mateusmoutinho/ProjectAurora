#!python3
# -*- coding: utf-8 -*-
import os 
from aurora.entrys import get_entrys
from aurora.execution import generate_repository_actions
import multiprocessing
from sys import exit



def main():

    try:
        entrys = get_entrys()
    except ValueError:
        exit(1)

    quiet = entrys['quiet']
    respositorys = entrys['repositorys']
    #runs "generate_repository_actions" in diferents subprocesses
    
    for respository_props in respositorys:
        
        p = multiprocessing.Process(target=generate_repository_actions, args=(respository_props, quiet))
        
        p.start()
        p.deamon = True
     


if __name__ == '__main__':
    
    main()