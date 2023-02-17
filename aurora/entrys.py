from cli_args_system import Args
import PySchema
from aurora.general import print_if_not_quiet
from os import getcwd
import json 
import yaml
import traceback


def get_entrys_from_cli(args:Args)->dict:
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
            raise ValueError('The time flag is not a number.')
    
    return [{ 
                'repository':repo,
                'comands':comands,
                'timewait':time_wait 
            }]



def load_config_file(config_file:str)->list:
    """Load the config file."""
    extension = config_file.split('.')[-1]
    try:
        with open(config_file,'r') as file:
            config_content = file.read()
    except FileNotFoundError:

        raise FileNotFoundError('The config file does not exist.')

    if extension == 'json':
        try:
            config = json.loads(config_content)
        except json.decoder.JSONDecodeError:

            raise ValueError('The config file is json serializable.')

    elif extension in ['yaml','yml']:
        try:
            #load withoud safe_load because it is not a security problem
            #avoid the warning

            config = yaml.load(config_content,Loader=yaml.FullLoader)
        except yaml.YAMLError:
            raise ValueError('The config file is not yaml serializable')
    else:
        raise ValueError('The config file is not a json or yaml file.')
    

    return config


def validade_and_format_repositorys(repository:dict)->list:
    PySchema.ensure_not_expected_keys_is_present(
            data=repository,
            expected_keys=['repository','comands','ignore','timewait','before']
    )
    
    repository_value = PySchema.treat_and_get_str(
            data=repository,
            key_or_index='repository',
            default=getcwd()
    )
    comands = PySchema.treat_and_get_list(
            data=repository,
            key_or_index='comands',
            default=[]
    )

    PySchema.treat_and_get_all(
            data=comands,
            callable=lambda data,index : PySchema.treat_and_get_str(
                    data=data,
                    key_or_index=index,
            )
    )


    ignore = PySchema.treat_and_get_bool(
            data=repository,
            key_or_index='ignore',
            default=False
    )
    timewait = PySchema.treat_and_get_int(
            data=repository,
            key_or_index='timewait',
            default=10
    )
    before = PySchema.treat_and_get_list(
            data=repository,
            key_or_index='before',
            default=[],
            treater=lambda value: '&&'.join(value) if value else None
    )

    return repository



def validate_and_format_config_content( config_content:list):
    
    
    PySchema.check_type(data=config_content,expected_type=list)
    config_content = PySchema.treat_and_get_all(
        data=config_content,
        callable=lambda data,index : PySchema.treat_and_get_dict(
            data=data,
            key_or_index=index,
            treater=validade_and_format_repositorys
        )
    )

    return config_content
 



def get_entrys()->dict:
    args = Args()
    
    quiet = args.flags_content('quiet','q','quiet')
    quiet = True if quiet.exist() else False
    try:    
        config_file = args.flags_content('config','f','cf')
        
        if config_file.exist_and_empty():
            raise ValueError('The config file is empty.')


        elif config_file.exist():
            config_content = load_config_file(config_file[0])
            repositorys = validate_and_format_config_content(config_content)
        else:
            repositorys = get_entrys_from_cli(args)
    except Exception as e:
        print_if_not_quiet(quiet,e)
        print(traceback.format_exc())
        raise e  

    return {
        'quiet':quiet,
        'repositorys':repositorys
    }
    