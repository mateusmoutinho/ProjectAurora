from cli_args_system import Args
from os import getcwd


def get_inputs()->dict:
    """Get the inputs from the user."""
    args = Args()
    #Getting Repository
    repo = args.flag_str('repo','r','repository')
    if not repo:
        repo = getcwd()
    
    #Getting Comand
    comand = args.flags_content('comand','c','comand')

    if not comand.exist():
        comand = None 
        print('Warnning, No comand specified')
    else:
        comand = ' '.join(comand.flags())
    
    #Getting Time
    time = args.flag_str('time','t','time')
    if not time:
        time = 10
    else:
        try:
            time = int(time)     
        except:
            print('Invalid time specified. Exiting...')
            raise Exception('Invalid time specified')


    return {
        'repository':repo,
        'comand':comand,
        'time':time
    }    