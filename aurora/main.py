#!python3
# -*- coding: utf-8 -*-
import os 
from aurora.entrys import get_entrys
from aurora.execution import generate_repository_actions
from aurora.general import print_if_not_quiet
import multiprocessing
from sys import exit
import json 


def main():

    try:
        entrys = get_entrys()
    except Exception as e:
        exit(1)
    
    '''with open("teste.json", "w") as f:
        json.dump(entrys, f, indent=4)
    return '''
  
    quiet = entrys['quiet']
    respositorys = entrys['repositorys']
    #runs "generate_repository_actions" in diferents subprocesses
    print_if_not_quiet(quiet, 'Starting Project Aurora...')
    for respository_props in respositorys:
        if respository_props['ignore']:
            print_if_not_quiet(quiet, 'Ignoring repository: ' + respository_props['repository'])
            continue
        
        repository_name = respository_props['repository']
        print_if_not_quiet(quiet, 'Starting repository: ' + repository_name)
        p = multiprocessing.Process(target=generate_repository_actions, args=(respository_props, quiet))
        
        p.start()
        p.deamon = True
     


if __name__ == '__main__':
    
    main()