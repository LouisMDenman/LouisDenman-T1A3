# Terminal Application: Gallo 24 Car Garage

Welcome! the following terminal application functions as a booking and information system for the Gallo 24 Car Garage. Users can add, remove and view vehicle bookings, as well as view information about vehicles in the Gallo 24 database, and finally play a guessing game trying to detirmine a vehicle based off of its metrics.

## Application Help

### Pre-requisites:

    - Python Version 3
    - Git
    - Bash

### Installation Instruction:

1. If you are operating on windows, install the Windows Subsystem for Linux [(WSL)](https://learn.microsoft.com/en-us/windows/wsl/install).

2. On windows open a WSL terminal, or for other operating systems open a standard terminal.

3. Clone the git repository found [here](https://github.com/LouisMDenman/LouisDenman-T1A3) to an appropriate location on your machine, using the git clone command:
```sh
git clone git@github.com:LouisMDenman/LouisDenman-T1A3.git
```

4. Allow the system_checks.sh script to have execute permission and run the file as a script by entering the following command in the terminal:
```sh 
chmod +x system_checks.sh
```

5. Run the command:
```sh
./system_checks.sh
```

6. in the terminal, and the application should begin.

### Dependancies:

- Colored: Colored is an external package that is responsible for adding color to text-based terminal interfaces. The installation of this package is handled by the run_gallo_24_garage.sh, which is run in the process of starting the terminal application via the system_checks.sh script, as explained above.
