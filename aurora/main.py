#!python3
# -*- coding: utf-8 -*-
import os 
from aurora.entrys import get_entrys
from aurora.execution import generate_repository_actions
from aurora.general import print_if_not_quiet
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
    print_if_not_quiet(quiet, 'Starting Project Aurora...')
    for respository_props in respositorys:
        repository_name = respository_props['repository']
        print_if_not_quiet(quiet, 'Starting repository: ' + repository_name)
        p = multiprocessing.Process(target=generate_repository_actions, args=(respository_props, quiet))
        
        p.start()
        p.deamon = True
     


if __name__ == '__main__':
    
    main()