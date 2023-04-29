from Handlers.FileHandler import FileHandler
from Constants.FilePaths import FilePaths
import importlib
import subprocess

class DependencyHandler:
    @staticmethod
    def install_package(package_name):
        try:
            subprocess.check_call(['pip', 'install', package_name])
        except subprocess.CalledProcessError as e:
            print(f"Error: failed to install {package_name}. Please install it manually using 'pip install {package_name}'")
            exit(1)

    @staticmethod
    def check_dependencies():
        print("Checking if you have dependencies to run script")
        packages = FileHandler.get_array_from_file(file_path=FilePaths.IMPORT_REQUIREMENTS.value, 
                                                   delimiter='\n'
        )
        for package_name in packages:
            try:
                importlib.import_module(package_name)
            except ImportError:
                DependencyHandler.install_package(package_name)