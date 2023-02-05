from cli_args_system import Args

from aurora.general import print_if_not_quiet
from os import getcwd
import json 
import yaml



def get_entrys_from_cli(args:Args,quiet:bool)->dict:
    """Get the entrys from the user."""

    repo = args.flag_str('repo','r','repository')
    if not repo:
        repo = getcwd()

    #Getting Comand
    comands = list(args.flags_content('comands','c'))
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



def load_config_file(config_file:str,quiet:bool)->list:
    """Load the config file."""
    extension = config_file.split('.')[-1]
    try:
        with open(config_file,'r') as file:
            config_content = file.read()
    except FileNotFoundError:
        print_if_not_quiet(quiet,'The config file does not exist.')
        raise FileNotFoundError('The config file does not exist.')

    if extension == 'json':
        try:
            config = json.loads(config_content)
        except json.decoder.JSONDecodeError:
            print_if_not_quiet(quiet,'The config file is json serializable')
            raise ValueError('The config file is json serializable.')

    elif extension in ['yaml','yml']:
        try:
            config = yaml.load(config_content)
        except yaml.YAMLError:
            print_if_not_quiet(quiet,'The config file is not yaml serializable')
            raise ValueError('The config file is not yaml serializable')
    else:
        print_if_not_quiet(quiet,'The config file is not a json or yaml file.')
        raise ValueError('The config file is not a json or yaml file.')
    

    return config



def validate_and_format_config_content( config_content:list,quiet:bool):
    if not isinstance(config_content,list):
        print_if_not_quiet(quiet,'The config file is not a list.')
        raise ValueError('The config file is not a list.')
    
    for repository in config_content:
        if not isinstance(repository,dict):
            print_if_not_quiet(quiet,'The config file is not a list of dicts.')
            raise ValueError('The config file is not a list of dicts.')
        keys = repository.keys()
        if not 'repository' in keys:
            print_if_not_quiet(quiet,'The repository key is not in the config file.')
            raise ValueError('The repository key is not in the config file.')
       
       
        if repository['repository'] == '.':
            repository['repository'] = getcwd()

        if not 'comands' in keys:
            repository['comands'] = []
        if not 'timewait' in keys:
            repository['timewait'] = 10
        
        if not isinstance(repository['comands'],list):
            print_if_not_quiet(quiet,'The comands key is not a list.')
            raise ValueError('The comands key is not a list.')
        
        if not isinstance(repository['timewait'],int):
            print_if_not_quiet(quiet,'The timewait key is not a int.')
            raise ValueError('The timewait key is not a int.')



def get_entrys_from_config(config_file:str,quiet:bool)->dict:
    """Get the entrys from the config file."""
    config_content = load_config_file(config_file,quiet)
    validate_and_format_config_content(config_content,quiet)
    return config_content


def get_entrys()->dict:
    args = Args()
    quiet = args.flags_content('quiet','q','quiet')
    quiet = True if quiet.exist() else False
    
    config_file = args.flags_content('config','f','cf')
    if config_file.exist_and_empty():
        print_if_not_quiet(quiet,'The config file is empty.')
        raise ValueError('The config file is empty.')
    elif config_file.exist():
        repositorys = get_entrys_from_config(config_file[0],quiet)
    else:
        repositorys = get_entrys_from_cli(args,quiet)
    
    return {
        'quiet':quiet,
        'repositorys':repositorys
    }