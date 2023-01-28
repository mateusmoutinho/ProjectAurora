from cli_args_system import Args
from aurora.log import treat_log
from os import getcwd


def get_entrys(acumulated_log:list)->dict:
    """Get the entrys from the user."""
    args = Args()
    #Getting Repository
    repo = args.flag_str('repo','r','repository')
    if not repo:
        repo = getcwd()
    
    quiet_flag = args.flags_content('quiet','q','quiet')
    if quiet_flag.exist():
        quiet=True
    else:
        quiet=False
    log_file = args.flag_str('l','log','logfile')
    
    #Getting Comand
    comands = list(args.flags_content('comand','c'))
    if not comands:
        comands =[]

    #Getting Time
    time_flag = args.flag_str('time','t','time')
    if not time_flag:
        time_wait = 10
    else:
        try:
            time_wait = int(time_wait)     
        except TypeError:
            treat_log(acumulated_log,'Invalid time specified',quiet,error=True)
            raise TypeError('Invalid time specified')

    return {
        'repository':repo,
        'comands':comands,
        'timewait':time_wait,
        'quiet':quiet,
        'logfile':log_file
    }    