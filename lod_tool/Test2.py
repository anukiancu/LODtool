import unreal

selected_obj = unreal.EditorUtilityLibrary.get_selected_asset_data()[0]

selected_actor = selected_obj.get_asset()

num_of_materials = unreal.EditorStaticMeshLibrary.get_number_materials(selected_actor)

print(num_of_materials)