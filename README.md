# ArcPy3 Ansible

This project provides a Docker-based solution for downloading Python packages (specifically Ansible and its dependencies) that are compatible with ArcGIS Pro 3.5's Python 3.11.11 environment on Windows.

![Tech Stacks](https://skillicons.dev/icons?i=ansible,docker,python,windows)

## Overview

ArcGIS Pro 3.5 comes with a specific Python 3.11.11 environment that may have limited internet access or package installation restrictions in enterprise environments. This tool allows you to:

1. Download all required Ansible packages for Windows Python 3.11.11 using Docker
2. Transfer the downloaded packages to your ArcGIS Pro VM
3. Install them offline in a virtual environment

## Architecture

```
Host Machine (with Docker)     →     VM (ArcGIS Pro 3.5 - No Docker needed)
┌─────────────────────────┐           ┌──────────────────────────────┐
│ docker compose up       │   copy    │ Python 3.11.11 venv         │
│ Downloads .whl packages │    →      │ pip install --find-links .  │
│ to ./ansible_packages/  │           │ ansible-navigator run        │
└─────────────────────────┘           └──────────────────────────────┘
```

**Key Point**: Docker is only used for downloading packages. Your VM doesn't need Docker installed.

## Download Packages

Run the project to download packages:

```bash
cd arcpy3-ansible
docker compose up
```
OR
```bash
podman compose up
```

The packages will be downloaded to the `./ansible_packages` directory and automatically listed.

## VM Setup (Windows with ArcGIS Pro)

### 1. Prepare Virtual Environment

Navigate to your ArcGIS Pro Python environment and create a new virtual environment:

```cmd
C:\Users\macminiowner\AppData\Local\Programs\ArcGIS\Pro\bin\Python\envs\arcgispro-py3>python -m venv C:\venvs\ansible-env
```

### 2. Activate the Virtual Environment

```cmd
C:\Users\macminiowner\AppData\Local\Programs\ArcGIS\Pro\bin\Python\envs\arcgispro-py3>C:\venvs\ansible-env\Scripts\activate

(ansible-env) C:\Users\macminiowner\AppData\Local\Programs\ArcGIS\Pro\bin\Python\envs\arcgispro-py3>
```

### 3. Transfer Downloaded Packages

Copy the `ansible_packages` folder from your Docker host to your Windows VM. You can use:
- Network share
- USB drive
- SCP/SFTP
- Any file transfer method available in your environment

### 4. Install Packages Offline

Once you have the packages on your VM and your virtual environment activated:

```cmd
(ansible-env) C:\> cd path\to\ansible_packages

(ansible-env) C:\path\to\ansible_packages> pip install --find-links . --no-index ansible
```

This will install Ansible and all its dependencies from the local package directory without requiring internet access.

## Verify Installation

Test that Ansible and Ansible Navigator are properly installed:

```cmd
(ansible-env) C:\> ansible --version
(ansible-env) C:\> ansible-navigator --version
(ansible-env) C:\> python -c "import ansible; print('Ansible successfully installed')"
```

## Using with Ansible Navigator

Once installed, you can use Ansible Navigator for a modern TUI experience:

```cmd
(ansible-env) C:\> ansible-navigator run playbook.yml
(ansible-env) C:\> ansible-navigator inventory --host all
(ansible-env) C:\> ansible-navigator collections
```

**Note**: Docker is only used on your host machine to download packages. The VM doesn't need Docker - it just uses the offline-installed Python packages.

## Package Contents

The downloaded packages include:
- **ansible** - Main Ansible package  
- **ansible-core** - Core Ansible functionality
- **ansible-navigator** - Text-based user interface for Ansible
- **paramiko** - SSH client library
- **PyYAML** - YAML parser
- **Jinja2** - Template engine
- **cryptography** - Cryptographic library
- **packaging** - Core utilities for Python packages
- **requests** - HTTP library
- And all their dependencies

## Features

- **Platform-specific**: Packages downloaded specifically for Windows x64 platform
- **Version-matched**: Compatible with ArcGIS Pro 3.5's Python 3.11.11
- **Offline installation**: No internet required on target VM
- **Complete dependency set**: All required dependencies included
- **Docker-based**: Clean, reproducible download environment

## Troubleshooting
