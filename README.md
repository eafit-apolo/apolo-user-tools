# Apolo-User-Tools
This repository contains useful commands, aliases and tools that are available for all users in Apolo. 

Feel free to add new commands, aliases. Check out our [contribution guidelines](CONTRIBUTING.md)

## Repository structure
The repo contains two main directories: 
`bash-tools` and `src`

* `bash-tools`:
contains aliases or functions that are written in *Bash*.
If you plan to add aliases put it in the file `default-aliases` in the section related with purpose of the alias. If more complex commands are needed, include it using another file in the same directory with a clear title.

* `src`:
contains directories with more complex commands that are written in any language, we specially encourage the use of *Python*. The directories inside `src` are application-specific, e.g: slurm, ansible, file-system, etc.
   
   * `application-specific`: these directories contain the different scripts that will become available commands to our users.  These scripts could be in single files or directories. Commands in the same `application-specific` directory share the same environnement and language, libraries or other requisites. Each `application-specific` directory contains a single file that specifies these requisites, feel free to modify it.

This is an example of the directory structure: 
```
apolo-user-tools/
├── bash-tools
│   ├── default-aliases
│   ├── default-functions
│   └── learning-users-aliases
├── CONTRIBUTING.md
├── LICENSE
├── README.md
└── src
    ├── file-system
    │   ├── command2.py
    │   ├── quotas
    │   │   ├── command1.py
    │   │   └── vars_file.py
    │   └── requirements.txt
    └── slurm
        ├── requirements.txt
        └── squeue-stats.py
```
