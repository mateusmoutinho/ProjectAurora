

from aurora.entrys import get_inputs
from aurora.execution import run_comands
from aurora.log import treat_log
from sys import exit
import json




def main():
    acumulated_log = []
    try:
        inputs = get_inputs(acumulated_log)
    except Exception as e:
        treat_log(acumulated_log, e,quiet=False,error=True)
        exit(1)
 
    repository_path = inputs['repository']
    time_wait = inputs['time']
    comands = inputs['comands']
    quiet = inputs['quiet']
    try:
        run_comands(acumulated_log,quiet,comands,time_wait,repository_path)
    except KeyboardInterrupt:
        with open('log.json', 'w') as f:
            f.write(json.dumps(acumulated_log,ensure_ascii=False,indent=4))

if __name__ == '__main__':
    
    main()