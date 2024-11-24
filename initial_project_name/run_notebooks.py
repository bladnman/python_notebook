import subprocess
import sys
from pathlib import Path

def check_kernel_installed():
    try:
        import jupyter
        # Check if kernel is installed by importing ipykernel
        import ipykernel
        return True
    except ImportError:
        return False

def main():
    if not check_kernel_installed():
        print("Jupyter kernel not found. Installing...")
        # Import and run the install_notebook script
        from initial_project_name.install_notebook import main as install_notebook
        install_notebook()
    
    print("Starting Jupyter notebook server...")
    subprocess.run(["jupyter", "notebook"], check=True)

if __name__ == "__main__":
    main() 