import unreal

def get_lod_screen_size(obj):
    lod_no = unreal.EditorStaticMeshLibrary.get_lod_count(obj)
    lod_screen_sizes = []
    for lod in range(lod_no):
        lod_screen_size = unreal.EditorStaticMeshLibrary.get_lod_screen_sizes(obj)
        lod_index = lod
        print(f"Lod number {lod_index} has a screen size of {lod_screen_size}")
        
    return lod_screen_size

if __name__ == "__main__":
    assets = unreal.EditorUtilityLibrary.get_selected_assets()
    for asset in assets:
        get_lod_screen_size(asset)