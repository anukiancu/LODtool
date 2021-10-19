import unreal

asset_path = "/Game/Meshes"


def check_lods(static_mesh):
    # Checks number of LODs for each mesh
    lod_no = unreal.EditorStaticMeshLibrary.get_lod_count(static_mesh)
    print(f"Current LOD count for this mesh: {lod_no}")
    return lod_no

assets = unreal.EditorUtilityLibrary.get_selected_assets()

if __name__ == "__main__":
    for asset in assets:
         check_lods(asset)