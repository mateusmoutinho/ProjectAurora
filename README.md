### Introducing Project Aurora
Introducing Project Aurora, the open source solution for automating your Git workflow on cloud virtual machines or remote severs.

Our goal with Project Aurora is to help developers by providing a tool that streamlines the process of updating and running commands on your Git repositories in a cloud environment. With Project Aurora, you can easily set it up on a virtual machine in the cloud and let it automatically update your servers or run build scripts every time you make a commit to your repository.

We believe that automation should be accessible to everyone, and with Project Aurora, you can easily set it up on a cloud virtual machine and let it take care of the updates and scripts while you focus on development. Join us in making the development process more efficient with Project Aurora.

## Installation


#### Binary Instalation
If you dont want to deal with dependencys you can download the single binary of the program in the path **outputs/binarys/aurora** for linux and **outputs/binarys/aurora.exe** for windows 

For making a full binary instalation follow the comands:

Linux:

~~~shell
#download the binary
wget  https://github.com/mateusmoutinho/ProjectAurora/raw/main/outputs/binarys/Aurora
#give binary permission of execution 
sudo chmod +x Aurora
#move the Binary to usr/bin 
sudo mv  Aurora /usr/bin/Aurora
~~~


#### Interpreted Instalation
If have Python3 and Pip instaled on your machine, you can install the program in the interpreted version  with the comand:
~~~~bash
pip install git+https://github.com/mateusmoutinho/ProjectAurora.git
~~~~

and than, run the program with the comand: **python3 -m aurora.main** 

exemple of runing the interpreted version:
~~~~bash
python3 -m aurora.main --repository test/ -comands 'flask --app  test/main.py run --port=5001'
~~~~








## Usage
### Comand line usage
The comand line  usage of Project Aurora is to run the command **python3 -m aurora.run** followed by the options you want to use.

#### Repository
You can specify the repository you want to use with the **-repo** or **-r** option. If you are already inside the repository, you don't need to specify the repository path.

Example passing the repository:
~~~~bash 
Aurora --repository test/ -comands 'flask --app  test/main.py run --port=5001'
~~~~

Example hiding the repository (it will take the current folder as the repository):
~~~~bash 
Aurora -comands 'flask --app  main.py run --port=5001'
~~~~

#### Commands
You can specify the commands you want to run with the **-comands** or **-c** option. You can pass multiple commands by separating them with spaces.

Exemple of running the flask aplication in tree diferents ports:
~~~~bash 
Aurora -comands 'flask --app  main.py run --port=5001' 'flask --app  main.py run --port=5002' 'flask --app  main.py run --port=5003'
~~~~


#### Time
You can specify the time interval between checks for updates with the **-time** or **-t** option. The default is 10 seconds.

Exemple of seting git update time to 50 seconds:
~~~~bash 
Aurora -comands 'flask --app  main.py run --port=5001 -time 50'
~~~~

### Config file usage
Alternativly you can make massive setups by using config files. Project Aurora aceppt json and yaml as markup format, for doing these, you can just pass **-cf** or **-config** in the comand line: 

Exemple of calling Project Aurora with an yaml config file:
~~~~bash 
Aurora -config aurora.yaml
~~~~

Exemple of calling Project Aurora with an json file config file:
~~~~bash 
Aurora -config aurora.json
~~~~
#### The config file structure
The Config file structure is based on arrays of object for each repository you want to track and call comands following the exemple:
Exemple  in yaml:
~~~yaml
- repository: MyFirstProject/
  comands: 
    - flask --app MyFirstProject/main.py run --port 5000
    - flask --app MyFirstProject/main.py run --port 5001
    - flask --app MyFirstProject/main.py run --port 5002

- repository: MySecondProject/
  comands:
    -  python3 build_tool.py 
~~~
Exemple in json:
~~~json
[
    {
        "repository":" MyFirstProject/",
        "comands":[
            "flask --app MyFirstProject/main.py run --port 5000",
            "flask --app MyFirstProject/main.py run --port 5001",
            "flask --app MyFirstProject/main.py run --port 5002"
        ]
    },

    {
        "repository": "MySecondProject/",
        "comands":[
            "python3 build_tool.py"
            
        ]
    }

]
~~~
#### Config Flags 

##### ignore 
You can set **ignore** to true for the current repository be igonored on the list 
ex:
~~~yaml
- repository: MyFirstProject/
  ignore: true
  comands: 
    - flask --app MyFirstProject/main.py run --port 5000
~~~
##### before 
You can create sequencial comands lists to avoid run the comands in paralalel,
when you use the **before** key, all the comands will run in sequence one by one
istead of runs everything in paralalel witch is the default
ex:
~~~yaml
- repository: MySite/
  before:
      - npm install  --prefix MySite/
      - npm run build  --prefix MySite/
  comands:  
      - npm start  --prefix MySite/
~~~

### Extras 
#### Quiet Mode
You can turn on quiet mode with the **-quiet** or **-q** option. This will prevent any log 
messages from being printed to the console.



### Conclusion
Project Aurora is a useful tool for automating the process of syncing and running commands on git repositories. With its simple command line interface and flexible options, it can save you time and make your workflow more efficient. Try it out today!
