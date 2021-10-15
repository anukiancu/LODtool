import unreal
asset_path = "/Game/Meshes"

def get_selected_asset():
    all_assets = unreal.EditorAssetLibrary.list_assets(asset_path)
    static_mesh = unreal.StaticMeshComponent.static_mesh
    all_assets_loaded = [unreal.EditorAssetLibrary.load_asset(a) for a in all_assets]
    static_mesh_assets = unreal.EditorFilterLibrary.by_class(
        all_assets_loaded, unreal.StaticMesh
    )
    selected_obj = unreal.EditorUtilityLibrary.get_selected_assets()[0]
    return static_mesh_assets
    

def get_num_mesh_materials(obj):
    num_of_materials = unreal.EditorStaticMeshLibrary.get_number_materials(obj)
    return(num_of_materials)


selected_assets = get_selected_asset()

for asset in selected_assets:
    num_of_mats = get_num_mesh_materials(asset)
    print(num_of_mats)



#selected_obj = unreal.EditorUtilityLibrary.get_selected_asset_data()[0]

#selected_actor = selected_obj.get_asset()

#num_of_materials = unreal.EditorStaticMeshLibrary.get_number_materials(selected_actor)

