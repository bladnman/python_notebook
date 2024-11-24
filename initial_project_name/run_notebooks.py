import subprocess
import sys

def main():
    try:
        # Try using jupyter-lab instead, which tends to be more stable
        print("Starting Jupyter lab server...")
        subprocess.run(["jupyter", "lab"], check=True)
    except subprocess.CalledProcessError:
        print("Error starting Jupyter lab. Trying notebook as fallback...")
        try:
            subprocess.run(["jupyter", "notebook", "--NotebookApp.contents_manager_class='notebook.services.contents.largefilemanager.LargeFileManager'"], check=True)
        except subprocess.CalledProcessError as e:
            print(f"Error starting Jupyter notebook: {e}")
            sys.exit(1)

if __name__ == "__main__":
    main()