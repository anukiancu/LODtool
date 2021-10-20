import unreal

def get_lod_UVS(obj):
    lod_no = unreal.EditorStaticMeshLibrary.get_lod_count(obj)
    for lod in range(lod_no):
        uvs = unreal.EditorStaticMeshLibrary.get_num_uv_channels(obj, lod)
        print(f"LOD numer {lod} has {uvs} UV channels.")
    return uvs

if __name__ == "__main__":
    assets = unreal.EditorUtilityLibrary.get_selected_assets()
    for asset in assets:
        get_lod_UVS(asset)