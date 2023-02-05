from cli_args_system import Args

from aurora.general import print_if_not_quiet
from os import getcwd
import json 
import yaml



def get_entrys_from_cli(args:Args,quiet:bool)->dict:
    """Get the entrys from the user."""

    repo = args.flag_str('repo','r','repository')
    if not repo:
        repo = 'current'

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
            time_wait = int(time_flag)
        except ValueError:
            print_if_not_quiet(quiet,'The time flag is not a number.')
            raise ValueError('The time flag is not a number.')
    
    return [{ 
                'repository':repo,
                'comands':comands,
                'timewait':time_wait 
            }]

def load_config_file(config_file:str,quiet:bool)->dict:
    """Load the config file."""
    extension = config_file.split('.')[-1]
    with open(config_file,'r') as file:
        config_content = file.read()
        if extension == 'json':
            try:
                config = json.loads(config_content)
            except json.decoder.JSONDecodeError:
                print_if_not_quiet(quiet,'The config file is not a json file.')
                raise ValueError('The config file is not a json file.')

        elif extension in ['yaml','yml']:
            try:
                config = yaml.load(config_content)
            except yaml.YAMLError:
                print_if_not_quiet(quiet,'The config file is not a yaml file.')
                raise ValueError('The config file is not a yaml file.')
        else:
            print_if_not_quiet(quiet,'The config file is not a json or yaml file.')
            raise ValueError('The config file is not a json or yaml file.')
    return config


def get_entrys_from_config(config_file:str,quiet:bool)->dict:
    """Get the entrys from the config file."""
    config_content = load_config_file(config_file,quiet)
    print(config_content)
    
def get_entrys()->dict:
    args = Args()
    quiet = args.flag_str('quiet','q','quiet')
    quiet = True if quiet.exists() else False
    
    config_file = args.flag_str('config','f','config')
    if config_file.exists():
        pass
    else:
        repositorys = get_entrys_from_cli(args,quiet)
    
    return {
        'quiet':quiet,
        'repositorys':repositorys
    }