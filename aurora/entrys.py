from cli_args_system import Args
from os import getcwd

def get_inputs()->dict:
    """Get the inputs from the user."""
    args = Args()
    repo = args.flag_str('repo','r','repository')
    if not repo:
        repo = getcwd()
    comand = args.flags_content('comand','c','comand')
    comand = ' '.join(comand.flags())

    time = args.flag_str('time','t','time')
    if not time:
        time = 10
    else:
        try:
            time = int(time)     
        except:
            print('Invalid time specified. Exiting...')
            raise Exception('Invalid time specified')

    if not comand:
        print('No comand specified. Exiting...')
        raise Exception('No comand specified')

    return {
        'repository':repo,
        'comand':comand,
        'time':time
    }    