import unreal
from Test2 import get_num_mesh_materials

asset_path = "/Game/Meshes"

assets = unreal.EditorUtilityLibrary.get_selected_assets()

if __name__ == "__main__":
    for asset in assets:
        get_num_mesh_materials(asset)