# Gomoku

Gomoku is an Epitech third-year project that involves developing an AI for the classic board game Gomoku. This project was completed by our team of three:  Eliot GOURDOUX, Lucas RYCHLEWSKI and Arslan TETU.

## Table of Contents

1. [Prerequisites](#prerequisites)
   - [Installing Python](#installing-python)
     - [Windows](#windows)
     - [Linux](#linux)
2. [Installing Dependencies](#installing-dependencies)
3. [Installation and Usage](#installation-and-usage)
   - [Generating the Binary (Linux)](#generating-the-binary-linux)
   - [Generating the Binary (Windows)](#generating-the-binary-windows)
4. [Testing the AI](#testing-the-ai)
5. [List of Commands](#list-of-commands)
   - [Mandatory Commands](#mandatory-commands)
   - [Optional Commands](#optional-commands)
   - [Communication Example](#communication-example)
6. [Contributors](#contributors)


## Prerequisites

Make sure you have Python 3 installed on your system.

### Installing Python

### Windows

If Python is not installed on your Windows machine, follow these steps:

1. Download the installer from the official Python website: [here](https://www.python.org/downloads/).
2. Run the installer and make sure to check the option **"Add Python to PATH" during installation.**
3. Verify the installation by opening PowerShell and typing:

```bash
python --version
```

### Linux

If Python is not installed on your Linux machine, you can install it using the package manager for your distribution:

- **Ubuntu/Debian**:

```bash
sudo apt update
sudo apt install python3 python3-pip
```
Verify the installation by typing:

```bash
python3 --version
```
- **Fedora**

```bash
sudo dnf update 
sudo dnf install python3 python3-pip
```

Verify the installation by typing:

```bash
python3 --version
```

## Installing Dependencies

Once Python is installed, you can install the required dependencies:

1. Install `pyinstaller` by running:

```bash
pip install pyinstaller
```
2. Alternatively, you can install all necessary dependencies by running:

```bash
pip install -r requirements.txt
```

## Installation and Usage

**Cloning the Repository**

Before proceeding, clone the repository to your local machine:

```bash
git clone git@github.com:Wavitoo/Gomoku.git
```

Once cloned, navigate to the project folder:

```bash
cd Gomoku
```

### Generating the Binary (Linux)

```bash
make
```

**Cleaning Generated Files**

```bash
make fclean
```

### Generating the Binary (Windows)

```bash
pyinstaller --onefile --noconsole --name gomoku src/main.py
```

If you are on Windows and using PowerShell, you can use the script `build.ps1` to automate the build process:

```bash
./build.ps1
```

**Cleaning Generated Files**

After building the binary, you may want to clean up the generated files such as the `build/`, `dist/` directories and the `.spec` file. This can be done using the `clean.ps1` script. Run the following command in PowerShell:

```bash
powershell -ExecutionPolicy Bypass -File clean.ps1
```

This will remove the build files and output directories, ensuring your environment is clean for the next build.

## Testing the AI

Once the binary is generated, you can test the AI using the Piskvork interface available [here](https://sourceforge.net/projects/piskvork/).

## List of Commands

The AI communicates with the game manager using a series of predefined commands. These commands include:

- **START [size]**: Initializes the AI with a specified board size.
- **BEGIN**: Indicates that the AI should start a new match.
- **BOARD**: Provides the board state to the AI.
- **TURN [X,Y]**: Sends the opponent's move.
- **END**: End the program.

### Gomoku AI Protocol

The AI uses a set of mandatory and optional commands to communicate with the game manager. Below is a detailed list of commands and their expected behavior:

### Mandatory Commands:

1. **START [size]**: The AI initializes the board based on the given size.
2. **TURN [X],[Y]**: The AI responds with its move after receiving the opponent's move.
3. **BEGIN**: The AI starts the match and provides its first move.
4. **BOARD**: Provides the full board state.
5. **INFO [key] [value]**: Information sent from the manager to the AI, which the AI can ignore.
6. **END**: The AI terminates its process.

### Optional Commands:

1. **RECTSTART [width],[height]**: Starts the game with a rectangular board.
2. **RESTART**: Restarts the match.
3. **TAKEBACK [X],[Y]**: Undoes the previous move.

### Communication Example:

1. **START 20**

- The manager sends: `START 20`
- The AI responds: `OK - everything is good`

2. **TURN 10,10**

- The manager sends: `TURN 10,10`
- The AI responds: `11,10`

3. **BEGIN**

- The manager sends: `BEGIN`
- The AI responds: `10,10`

4. **END**

- The manager sends: `END`
- The AI responds: `None`

5. **RECTSTART 30,20**

- The manager sends: `RECTSTART 30,20`
- The AI responds: `OK - parameters are good`

6. **RESTART**

- The manager sends: `RESTART`
- The AI responds: `OK`

7. **TAKEBACK 10,10**

- The manager sends: `TAKEBACK 10,10`
- The AI responds: `OK`

8. **INFO timeout_match 300000**
- The manager sends: INFO timeout_match 300000
- The AI responds: None<br>
*(The AI receives the time limit for the match (5 minutes), but doesn't need to send any response.)*

## Contributors

This project was developed as part of our coursework at Epitech. For any inquiries, please feel free to reach out to us:

- Eliot GOURDOUX eliot.gourdoux@epitech.eu
- Lucas RYCHLEWSKI lucas.rychlewski@epitech.eu
- Arslan TETU arslan.tetu@epitech.eu