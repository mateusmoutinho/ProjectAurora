from cli_args_system import Args
from aurora.log import treat_log
from os import getcwd


def get_inputs(acumulated_log:list)->dict:
    """Get the inputs from the user."""
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

    #Getting Comand
    comands = args.flags_content('comand','c','comand')

    if not comands:
        comands =[]
    #Getting Time
    time = args.flag_str('time','t','time')
    if not time:
        time = 10
    else:
        try:
            time = int(time)     
        except TypeError:
            treat_log(acumulated_log,'Invalid time specified',quiet,error=True)
            raise TypeError('Invalid time specified')



    return {
        'repository':repo,
        'comands':comands,
        'time':time,
        'quiet':quiet
    }    