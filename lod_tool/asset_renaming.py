import unreal

sel_assets = unreal.EditorUtilityLibrary.get_selected_assets()


for sa in sel_assets:    
    asset_name = sa.get_name()    
    asset_folder = unreal.Paths.get_path(sa.get_path_name())
    #Check if this asset is a Texture. Then check if it's name starts with T_. If not, prepend T_ to the name.
    if sa.get_class().get_name() == "Texture2D":
        if not asset_name.startswith("T_"):
            if not unreal.EditorAssetLibrary.rename_asset(sa.get_path_name(), asset_folder + "/T_" + asset_name):
                unreal.log_error("Could not rename: " + sa.get_path_name())

    elif sa.get_class().get_name() == "Material":
        if not asset_name.startswith("M_"):
            if not unreal.EditorAssetLibrary.rename_asset(sa.get_path_name(), asset_folder + "/M_" + asset_name):
                unreal.log_error('Could not rename' + sa.get_path_name())