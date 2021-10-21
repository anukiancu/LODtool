import unreal
from pathlib import Path

def get_path():
    path = unreal.Paths.get_project_file_path()
    path_obj = Path(path)
    file_name = path_obj.parent
    print(file_name)

get_path()