import unreal

def get_lod_screen_size(obj):
    lod_no = unreal.EditorStaticMeshLibrary.get_lod_count(obj)
    lod_screen_sizes = []
    for lod in range(lod_no):
        lod_screen_size = unreal.EditorStaticMeshLibrary.get_lod_screen_sizes(obj)
        lod_screen_size_dict = {"lod_number": lod, "screen_size": lod_screen_size}
        lod_screen_sizes.append(lod_screen_size_dict)

    for lod_screen_size_dict in lod_screen_sizes:
        print(
            f"LOD number {lod_screen_size_dict.get('lod_number')} of mesh {obj.get_name()} has a screen size of {lod_screen_size_dict.get('screen_size')}")
        
    return lod_screen_sizes

if __name__ == "__main__":
    assets = unreal.EditorUtilityLibrary.get_selected_assets()
    for asset in assets:
        get_lod_screen_size(asset)