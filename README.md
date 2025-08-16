# ArcPy3 PyInfra

![Tech Stacks](https://skillicons.dev/icons?i=python,docker,windows,git)

## Overview

In production environment, we may have encountered where we need to install ArcGIS Pro 3.1.2 with Python 3.9.16 environment in a hardened vm. However, that vm may have limited internet access or package installation restrictions in enterprise environments. This tool allows you to:

1. Download all required PyInfra packages for Windows Python 3.9.16 using Docker
2. Transfer the downloaded packages to your ArcGIS Pro VM
3. Install them offline in a virtual environment
4. Run automated environment checks with a user-friendly TUI (Text User Interface)

## Quick Start

### Download Packages

```bash
cd arcpy3-pyinfra
docker compose up --build
OR
podman compose up --build
```

The packages will be downloaded to the `./pyinfra_packages` directory.

### Install on Windows VM

#### 1. Prepare Virtual Environment

Navigate to your ArcGIS Pro Python environment and create a new virtual environment (using Program Files as example):

```cmd
C:\Program Files\ArcGIS\Pro\bin\Python\envs\arcgispro-py3>python -m venv pyinfra-venv C:\venvs\pyinfra-venv
```

#### 2. Activate the Virtual Environment

```cmd
C:\Program Files\ArcGIS\Pro\bin\Python\envs\arcgispro-py3>C:\venvs\pyinfra-venv\Scripts\activate

(pyinfra-venv) C:\Program Files\ArcGIS\Pro\bin\Python\envs\arcgispro-py3>
```

#### 3. Transfer Downloaded Packages

Copy the `pyinfra_packages` folder from your Docker host to your Windows VM. You can use any file transfer method available in your environment.

#### 4. Install Packages Offline

Once you have the packages on your VM and your virtual environment activated:

```cmd
(pyinfra-venv) C:\> cd path\to\pyinfra_packages

(pyinfra-venv) C:\path\to\pyinfra_packages> pip install --find-links . --no-index pyinfra
```

### Verify Installation

```cmd
pyinfra --version
```

## Running Environment Checks

After installing pyinfra, you can run environment checks to verify your setup:

```bash
pyinfra @local env_checks.py
```

This will check:
- ArcGIS Pro installation in common locations
- pyinfra-venv virtual environment existence
- Virtual environment activation readiness

## Why PyInfra?

- **Better Windows Compatibility**: Unlike Ansible or Salt cannot be hosted on Window machine
- **Simpler Dependencies**: Fewer system-level dependencies
- **ArcGIS Pro Friendly**: Better integration with Python-based GIS workflows

## Version Compatibility

### ArcGIS Pro 3.1.2
**Important**: If you're using ArcGIS Pro 3.1.2, you must use **pyinfra < 3.0** due to compatibility issues with the Python environment in that version.

```bash
pip install "pyinfra<3.0"
```

### ArcGIS Pro 3.5
For ArcGIS Pro 3.5 and later versions, you can use the latest pyinfra version (3.x) as they have improved Python 3.11.11 support.
