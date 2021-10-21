import unreal
asset_path = "/Game/Meshes"

def vertex_colors(obj):
    vertex_colors = unreal.EditorStaticMeshLibrary.has_vertex_colors(obj)
    print(f"Mesh has vertex colours: {vertex_colors}")
    return vertex_colors

if __name__ == "__main__":
    assets = unreal.EditorUtilityLibrary.get_selected_assets()
    for asset in assets:
        vertex_colors(asset)