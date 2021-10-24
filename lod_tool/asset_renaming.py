import unreal

selected_assets = unreal.EditorUtilityLibrary.get_selected_assets()


for sa in selected_assets:
    asset_name = sa.get_name()
    asset_folder = unreal.Paths.get_path(sa.get_path_name())
    if sa.get_class().get_name() == "Texture2D":
        if not asset_name.startswith("T_"):
            if not unreal.EditorAssetLibrary.rename_asset(
                sa.get_path_name(), asset_folder + "/T_" + asset_name
            ):
                unreal.log_error(
                    "Texture asset already named properly" + sa.get_path_name()
                )

    elif sa.get_class().get_name() == "Material":
        if not asset_name.startswith("M_"):
            if not unreal.EditorAssetLibrary.rename_asset(
                sa.get_path_name(), asset_folder + "/M_" + asset_name
            ):
                unreal.log_error(
                    "Material asset already named properly" + sa.get_path_name()
                )

    elif sa.get_class().get_name() == "StaticMesh":
        if not asset_name.startswith("SM_"):
            if not unreal.EditorAssetLibrary.rename_asset(
                sa.get_path_name(), asset_folder + "/SM_" + asset_name
            ):
                unreal.log_error(
                    "Static mesh asset already named properly" + sa.get_path_name()
                )
