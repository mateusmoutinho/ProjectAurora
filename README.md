### Introducing Project Aurora
Introducing Project Aurora, the open source solution for automating your Git workflow on cloud virtual machines or remote severs.

Our goal with Project Aurora is to help developers by providing a tool that streamlines the process of updating and running commands on your Git repositories in a cloud environment. With Project Aurora, you can easily set it up on a virtual machine in the cloud and let it automatically update your servers or run build scripts every time you make a commit to your repository.

We believe that automation should be accessible to everyone, and with Project Aurora, you can easily set it up on a cloud virtual machine and let it take care of the updates and scripts while you focus on development. Join us in making the development process more efficient with Project Aurora.

### Installation
To install Project Aurora, you need to have pip and python installed
You can then run the following command:

~~~~bash
pip install git+https://github.com/mateusmoutinho/ProjectAurora.git
~~~~
### Basic Usage
The basic usage of Project Aurora is to run the command **python3 -m aurora.run** followed by the options you want to use.

~~~~bash 
python3 -m aurora.run --repository test/ -comand 'flask --app  test/main.py run --port=5001'

~~~~
#### Repository
You can specify the repository you want to use with the **-repo** or **-r** option. If you are already inside the repository, you don't need to specify the repository path.

#### Commands
You can specify the commands you want to run with the **-comand** or **-c** option. You can pass multiple commands by separating them with spaces.

#### Time
You can specify the time interval between checks for updates with the **-time** or **-t** option. The default is 10 seconds.

#### Quiet Mode
You can turn on quiet mode with the **-quiet** or **-q** option. This will prevent any log messages from being printed to the console.

#### Log File
You can specify a log file to write the log messages to with the **-log** or **-l** option.


### Conclusion
Project Aurora is a useful tool for automating the process of syncing and running commands on git repositories. With its simple command line interface and flexible options, it can save you time and make your workflow more efficient. Try it out today!