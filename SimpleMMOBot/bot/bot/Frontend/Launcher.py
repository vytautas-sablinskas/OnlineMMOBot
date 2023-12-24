import sys
import os
backend_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'Backend'))
sys.path.append(backend_dir)

from Handlers.DependencyHandler import DependencyHandler
from Handlers.FileHandler import FileHandler
from Constants.FilePaths import FilePaths

def lauch_bot_panel():
    current_directory = os.path.dirname(os.path.abspath(__file__))
    panel_path = os.path.join(current_directory, "Panel.py")
    os.system(f"streamlit run {panel_path}")

if __name__ == "__main__":
    DependencyHandler.check_dependencies()
    FileHandler.write_into_file(FilePaths.PANEL_BOT_STATUS.value, "Stopped")
    lauch_bot_panel()