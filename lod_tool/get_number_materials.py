import unreal


asset_path = "/Game/Meshes"

def get_num_mesh_materials(obj):
    num_of_materials = unreal.EditorStaticMeshLibrary.get_number_materials(obj)
    print(f"Current number of materials for mesh {obj.get_name()}: {num_of_materials}")
    return num_of_materials

assets = unreal.EditorUtilityLibrary.get_selected_assets()

if __name__ == "__main__":
    for asset in assets:
        get_num_mesh_materials(asset)