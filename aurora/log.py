from time import time 
import traceback
import datetime
import yaml

def print_log_if_not_quiet(quiet:bool,values:str):
    """Prints the log to the console. if quiet is False"""
    if quiet:
        return 
    print(values)

def create_log_yaml(acumulated_log:list,entrys:list)->str:
    """Formats the log to yaml string"""
    return yaml.dump({
        'entrys':entrys,
        'log':acumulated_log
    })

def add_log(acumulated_log:list, mensage:str,error:bool):
    
    now = time()
    now_in_data = datetime.datetime.fromtimestamp(now).strftime('%Y-%m-%d %H:%M:%S')
    if error:
        acumulated_log.append({
            'time':now_in_data,
            'event':'error',
            'message':mensage,
            'traceback':traceback.format_exc()
        })
    else:
        acumulated_log.append({
            'time':now_in_data,
            'event':'action',
            'message':mensage
        })



def treat_log(acumulated_log:list,mensage:str,quiet:bool,error:bool=False):
    """Treats the log and prints it to the console. if quiet is False"""
    print_log_if_not_quiet(quiet,mensage)
    add_log(acumulated_log,mensage,error)
