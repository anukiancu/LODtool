import unreal

def remove_lods(static_mesh):
    lod_no = unreal.EditorStaticMeshLibrary.get_lod_count(static_mesh)
    print(lod_no)
    
    if lod_no == 1:
        print(f"Mesh {static_mesh.get_name()} does not have any LODs.")

    elif lod_no >= 2:
        unreal.EditorStaticMeshLibrary.remove_lods(static_mesh)
        print(f"LODs for mesh {static_mesh.get_name()} removed.")

if __name__ == "__main__":
    assets = unreal.EditorUtilityLibrary.get_selected_assets()
    for asset in assets:
        remove_lods(asset)