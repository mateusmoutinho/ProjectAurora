

from aurora.entrys import get_entrys
from aurora.execution import run_comands
from aurora.log import treat_log,create_log_yaml
from sys import exit




def main():
    acumulated_log = []
    try:
        entrys = get_entrys(acumulated_log)
    except Exception as e:
        treat_log(acumulated_log, e,quiet=False,error=True)
        exit(1)
 
    repository_path = entrys['repository']
    time_wait = entrys['timewait']
    comands = entrys['comands']
    quiet = entrys['quiet']
    log_file = entrys['logfile']
  
   
    try:
        run_comands(acumulated_log,quiet,comands,time_wait,repository_path)
    except KeyboardInterrupt:
        treat_log(acumulated_log, 'KeyboardInterrupt',quiet=quiet)

        if log_file:
            treat_log(acumulated_log, f'Log saved in {log_file}.json',quiet=quiet)
            log_file = log_file.split('.')[0]
            
            log_content = create_log_yaml(acumulated_log,entrys)
            with open(f'{log_file}.yaml', 'w') as f:
                f.write(log_content)
        exit(1)

if __name__ == '__main__':
    
    main()