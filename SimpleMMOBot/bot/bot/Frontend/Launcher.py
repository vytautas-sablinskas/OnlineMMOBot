import sys
import os
backend_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'Backend'))
sys.path.append(backend_dir)

from Handlers.DependencyHandler import DependencyHandler

def lauch_bot_panel():
    current_directory = os.path.dirname(os.path.abspath(__file__))
    panel_path = os.path.join(current_directory, "Panel.py")
    os.system(f"streamlit run {panel_path}")

if __name__ == "__main__":
    DependencyHandler.check_dependencies()
    lauch_bot_panel()