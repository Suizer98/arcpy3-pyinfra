from pyinfra.operations import python
import os
import subprocess

# Configuration
VENVS_DIR = "C:/venvs"
VENV_NAME = "pyinfra-venv2"
VENV_PATH = f"{VENVS_DIR}/{VENV_NAME}"

# ArcGIS Pro paths
ARCGIS_PROGRAM_FILES = "C:/Program Files/ArcGIS/Pro/bin/ArcGISPro.exe"
ARCGIS_LOCALAPPDATA = os.path.join(os.environ.get("LOCALAPPDATA", ""), "Programs/ArcGIS/Pro/bin/ArcGISPro.exe")
ARCGIS_PYTHON_PROGRAM_FILES = "C:/Program Files/ArcGIS/Pro/bin/Python/envs/arcgispro-py3/python.exe"
ARCGIS_PYTHON_LOCALAPPDATA = os.path.join(os.environ.get("LOCALAPPDATA", ""), "Programs/ArcGIS/Pro/bin/Python/envs/arcgispro-py3/python.exe")

def check_arcgis_pro():
    paths = [
        ARCGIS_PROGRAM_FILES,
        ARCGIS_LOCALAPPDATA
    ]
    
    found = any(os.path.exists(p) for p in paths)
    if not found:
        raise Exception('ArcGIS Pro not found')
    print("SUCCESS: ArcGIS Pro found")

def create_venv():
    venv_path = VENV_PATH
    if os.path.exists(venv_path):
        print("pyinfra-venv found, checking if pyinfra is installed...")
        # Check if pyinfra is already installed
        pip_path = os.path.join(venv_path, "Scripts", "pip.exe")
        try:
            result = subprocess.run([pip_path, "list"], capture_output=True, text=True, check=True)
            if "pyinfra" in result.stdout:
                print("SUCCESS: pyinfra already installed")
                return True
            else:
                print("Installing pyinfra...")
        except subprocess.CalledProcessError as e:
            print("Installing pyinfra...")
    
    print("Creating virtual environment...")
    
    # Create the venvs directory if it doesn't exist
    if not os.path.exists(VENVS_DIR):
        os.makedirs(VENVS_DIR)
    
    # Create virtual environment using ArcGIS Pro Python
    arcgis_python = None
    python_paths = [
        ARCGIS_PYTHON_PROGRAM_FILES,
        ARCGIS_PYTHON_LOCALAPPDATA
    ]
    
    for python_path in python_paths:
        if os.path.exists(python_path):
            arcgis_python = python_path
            break
    
    if not arcgis_python:
        raise Exception("ArcGIS Pro Python not found - cannot create virtual environment")
    
    # Create virtual environment
    try:
        subprocess.run([arcgis_python, "-m", "venv", venv_path], check=True)
        print("SUCCESS: Virtual environment created")
        
        # Install pyinfra
        pip_path = os.path.join(venv_path, "Scripts", "pip.exe")
        subprocess.run([pip_path, "install", "--find-links", "pyinfra_packages", "--no-index", "pyinfra"], check=True)
        print("SUCCESS: pyinfra installed")
        
        return True
    except subprocess.CalledProcessError as e:
        raise Exception(f"Failed to create virtual environment: {e}")

def check_venv_activation():
    venv_path = VENV_PATH
    if not os.path.exists(venv_path):
        raise Exception("Cannot test activation - venv not found")
    
    checks = [
        os.path.join(venv_path, "Scripts", "activate.bat"),
        os.path.join(venv_path, "Scripts", "python.exe"),
        os.path.join(venv_path, "Lib", "site-packages", "pyinfra")
    ]
    
    if all(os.path.exists(c) for c in checks):
        print("SUCCESS: Venv activation ready")
        return True
    raise Exception("Venv activation failed - missing required components")

# Run all checks
python.call(
    name="Check ArcGIS Pro installation",
    function=check_arcgis_pro,
)

python.call(
    name="Create virtual environment and install pyinfra",
    function=create_venv,
)

python.call(
    name="Check venv activation",
    function=check_venv_activation,
)
