import subprocess
import sys
from pathlib import Path
import importlib.util
from importlib.metadata import distributions

def check_dependencies():
    required = {'ipykernel', 'jupyter', 'notebook'}
    installed = {dist.metadata['Name'].lower() for dist in distributions()}
    missing = required - installed
    if missing:
        print(f"Missing required packages: {missing}")
        print("Installing missing packages...")
        subprocess.check_call([sys.executable, "-m", "pip", "install", *missing])

def main():
    try:
        # Check dependencies first
        check_dependencies()
        
        # Get the project name from the parent directory name
        project_name = Path(__file__).parent.name
        
        print(f"Using Python interpreter: {sys.executable}")
        print(f"Registering kernel for {project_name}...")
        
        # Register the kernel
        result = subprocess.run([
            sys.executable,
            "-m",
            "ipykernel",
            "install",
            "--user",
            f"--name={project_name}"
        ], check=True, capture_output=True, text=True)
        
        print(f"Kernel registration output: {result.stdout}")
        if result.stderr:
            print(f"Kernel registration stderr: {result.stderr}")
        
        print("Starting Jupyter notebook...")
        # Launch Jupyter notebook
        subprocess.run([
            "jupyter",
            "notebook"
        ], check=True)
    except subprocess.CalledProcessError as e:
        print(f"Error: {e}")
        print(f"Output: {e.stdout if hasattr(e, 'stdout') else 'No stdout'}")
        print(f"Error output: {e.stderr if hasattr(e, 'stderr') else 'No stderr'}")
        sys.exit(1)
    except Exception as e:
        print(f"Unexpected error: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main() 