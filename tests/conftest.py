import sys
import os

project_root = os.path.abspath(
    os.path.join(os.path.dirname(__file__), '..')
)

backend_path = os.path.join(project_root, 'backend')

sys.path.insert(0, project_root)
sys.path.insert(0, backend_path)